import discord

from discord.ext import commands

from views.voice_panel import VoicePanel

# =========================================
# НАСТРОЙКА
# =========================================

CREATOR_CHANNEL_ID = 1504216902850056293
SETTINGS_CHANNEL_ID = 1504216841093120140

VOICE_CATEGORY_NAME = "𝐏𝐑𝐈𝐕𝐀𝐓𝐄 𝐕𝐎𝐈𝐂𝐄"

# =========================================

class TempVoice(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # =====================================
    # READY
    # =====================================

    @commands.Cog.listener()
    async def on_ready(self):

        self.bot.add_view(
            VoicePanel()
        )

        print("TempVoice система загружена")

    # =====================================
    # CREATE ROOM
    # =====================================

    @commands.Cog.listener()
    async def on_voice_state_update(
        self,
        member,
        before,
        after
    ):

        # =================================
        # СОЗДАНИЕ КОМНАТЫ
        # =================================

        if after.channel and after.channel.id == CREATOR_CHANNEL_ID:

            guild = member.guild

            category = discord.utils.get(
                guild.categories,
                name=VOICE_CATEGORY_NAME
            )

            # =============================
            # СОЗДАНИЕ КАТЕГОРИИ
            # =============================

            if not category:

                category = await guild.create_category(
                    VOICE_CATEGORY_NAME
                )

            # =============================
            # ПРАВА
            # =============================

            overwrites = {

                guild.default_role:
                discord.PermissionOverwrite(
                    connect=True,
                    view_channel=True
                ),

                member:
                discord.PermissionOverwrite(
                    manage_channels=True,
                    mute_members=True,
                    move_members=True,
                    connect=True,
                    speak=True
                )
            }

            # =============================
            # СОЗДАНИЕ ВОЙСА
            # =============================

            channel = await guild.create_voice_channel(
                name=f"👑 {member.name}",
                category=category,
                overwrites=overwrites
            )

            # =============================
            # ПЕРЕНОС ПОЛЬЗОВАТЕЛЯ
            # =============================

            await member.move_to(channel)

        # =================================
        # УДАЛЕНИЕ ПУСТОЙ КОМНАТЫ
        # =================================

if before.channel:

    if before.channel.category:

        if before.channel.category.name == VOICE_CATEGORY_NAME:

            if len(before.channel.members) == 0:

                await before.channel.delete()

    # =====================================
    # SETUP PANEL
    # =====================================

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def setup(self, ctx):

        settings_channel = self.bot.get_channel(
            SETTINGS_CHANNEL_ID
        )

        embed = discord.Embed(
            title="🎛 Управление комнатой",
            description=(

                "### Возможные манипуляции в вашей комнате\n\n"

                "<:add_slot:1504538336080035980> = Добавить слот в комнату\n"
                "<:remove_slot:1504539217147990137> = Убрать слот из комнаты\n"
                "<:close_room:1504540207532343547> = Закрыть комнату\n"
                "<:cloce_room_for_user:1504549635254124635> = Открыть комнату\n"
                "<:prohibit_speak:1504541149837262939> = Заглушить пользователей\n"
                "<:delete_userr:1504542342726811842> = Исключить пользователей\n"
                "<:new_bitrate:1504543048237977642> = Изменить bitrate\n"
                "<:limit_slots:1504543630487195818> = Изменить лимит\n"
                "<:transfer_rights:1504547267741225061> = Передать owner\n"
                "<:rename_room:1504548012767187055> = Переименовать комнату"
            ),
            color=0x1e1f22
        )

        embed.set_footer(
            text="𝐃𝐈𝐒𝐏𝐄𝐑𝐒𝐄𝐑 PREMIUM SYSTEM"
        )

        await settings_channel.send(
            embed=embed,
            view=VoicePanel()
        )

        await ctx.send(
            "✅ Панель управления отправлена"
        )

# =========================================

async def setup(bot):

    await bot.add_cog(
        TempVoice(bot)
    )
