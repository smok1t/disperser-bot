import discord

from discord.ext import commands

# =========================================
# НАСТРОЙКА
# =========================================

WELCOME_CHANNEL_ID = 1312473793062637659

TICKET_CHANNEL_ID = 1312473798859292712
HISTORY_CHANNEL_ID = 1504208026750685346

# =========================================
# CUSTOM EMOJI
# =========================================

FAMILY_EMOJI = "<:disperser:1504529172964442275>"

# =========================================
# BANNER
# =========================================

BANNER_URL = "https://media.discordapp.net/attachments/1504206797316165782/1504581667044593774/31E3EAB5-E517-4B91-BFD4-F7EBB99BE315.png?ex=6a07825f&is=6a0630df&hm=2884fd34ca06a0919bafe2fa6a72edda93c0f99860feebb9caaaf7d11fcd285d&=&format=webp&quality=lossless&width=960&height=960"

# =========================================

class Welcome(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # =====================================
    # MEMBER JOIN
    # =====================================

    @commands.Cog.listener()
    async def on_member_join(self, member):

        channel = self.bot.get_channel(
            WELCOME_CHANNEL_ID
        )

        if not channel:
            return

        # =================================
        # EMBED
        # =================================

        embed = discord.Embed(

            title=(
                f"{FAMILY_EMOJI} Новый участник {FAMILY_EMOJI}"
            ),

            description=(

                f"{member.mention} добро пожаловать в "
                f"**𝐃𝐈𝐒𝐏𝐄𝐑𝐒𝐄𝐑**\n\n"

                "### Навигация по серверу\n"

                f"🎫・<#{TICKET_CHANNEL_ID}> "
                f"— подача заявок\n"

                f"📜・<#{HISTORY_CHANNEL_ID}> "
                f"— история семьи\n\n"

                "🔒 Приватные каналы "
                "доступны после получения роли"

            ),

            color=0x1e1f22
        )

        # =================================
        # AUTHOR
        # =================================

        embed.set_author(
            name="𝐃𝐈𝐒𝐏𝐄𝐑𝐒𝐄𝐑 FAMILY"
        )

        # =================================
        # USER AVATAR
        # =================================

        embed.set_thumbnail(
            url=member.display_avatar.url
        )

        # =================================
        # BANNER
        # =================================

        embed.set_image(
            url=BANNER_URL
        )

        # =================================
        # FOOTER
        # =================================

        embed.set_footer(
            text=f"Участник #{member.guild.member_count}"
        )

        # =================================
        # SEND
        # =================================

        await channel.send(
            content=member.mention,
            embed=embed
        )

# =========================================

async def setup(bot):

    await bot.add_cog(
        Welcome(bot)
    )