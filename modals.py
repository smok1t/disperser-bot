import discord

# =========================================
# RENAME MODAL
# =========================================

class RenameModal(
    discord.ui.Modal,
    title="Смена названия"
):

    new_name = discord.ui.TextInput(
        label="Новое название комнаты",
        placeholder="Введите название...",
        max_length=32
    )

    async def on_submit(
        self,
        interaction: discord.Interaction
    ):

        if not interaction.user.voice:
            return await interaction.response.send_message(
                "❌ Ты не в войсе",
                ephemeral=True
            )

        channel = interaction.user.voice.channel

        await channel.edit(
            name=self.new_name.value
        )

        await interaction.response.send_message(
            f"✏️ Название изменено: {self.new_name.value}",
            ephemeral=True
        )

# =========================================
# LIMIT MODAL
# =========================================

class LimitModal(
    discord.ui.Modal,
    title="Изменение лимита"
):

    limit = discord.ui.TextInput(
        label="Введите лимит",
        placeholder="Например: 5",
        max_length=2
    )

    async def on_submit(
        self,
        interaction: discord.Interaction
    ):

        if not interaction.user.voice:
            return await interaction.response.send_message(
                "❌ Ты не в войсе",
                ephemeral=True
            )

        channel = interaction.user.voice.channel

        try:

            limit = int(self.limit.value)

            await channel.edit(
                user_limit=limit
            )

            await interaction.response.send_message(
                f"👥 Лимит изменен: {limit}",
                ephemeral=True
            )

        except:

            await interaction.response.send_message(
                "❌ Введите число",
                ephemeral=True
            )

# =========================================
# BITRATE MODAL
# =========================================

class BitrateModal(
    discord.ui.Modal,
    title="Изменение bitrate"
):

    bitrate = discord.ui.TextInput(
        label="Введите bitrate",
        placeholder="Например: 96",
        max_length=3
    )

    async def on_submit(
        self,
        interaction: discord.Interaction
    ):

        if not interaction.user.voice:
            return await interaction.response.send_message(
                "❌ Ты не в войсе",
                ephemeral=True
            )

        channel = interaction.user.voice.channel

        try:

            bitrate = int(self.bitrate.value)

            await channel.edit(
                bitrate=bitrate * 1000
            )

            await interaction.response.send_message(
                f"📶 Bitrate изменен: {bitrate}",
                ephemeral=True
            )

        except:

            await interaction.response.send_message(
                "❌ Ошибка bitrate",
                ephemeral=True
            )

# =========================================
# TRANSFER OWNER MODAL
# =========================================

class TransferOwnerModal(
    discord.ui.Modal,
    title="Передача владельца"
):

    user_id = discord.ui.TextInput(
        label="ID пользователя",
        placeholder="Введите ID"
    )

    async def on_submit(
        self,
        interaction: discord.Interaction
    ):

        if not interaction.user.voice:
            return await interaction.response.send_message(
                "❌ Ты не в войсе",
                ephemeral=True
            )

        channel = interaction.user.voice.channel

        try:

            member = interaction.guild.get_member(
                int(self.user_id.value)
            )

            if not member:
                return await interaction.response.send_message(
                    "❌ Пользователь не найден",
                    ephemeral=True
                )

            await channel.edit(
                name=f"👑 {member.name}"
            )

            await interaction.response.send_message(
                f"👑 Owner передан: {member.mention}",
                ephemeral=True
            )

        except:

            await interaction.response.send_message(
                "❌ Ошибка передачи owner",
                ephemeral=True
            )

# =========================================
# PERMIT USER MODAL
# =========================================

class PermitUserModal(
    discord.ui.Modal,
    title="Выдать доступ"
):

    user_id = discord.ui.TextInput(
        label="ID пользователя",
        placeholder="Введите ID"
    )

    async def on_submit(
        self,
        interaction: discord.Interaction
    ):

        if not interaction.user.voice:
            return await interaction.response.send_message(
                "❌ Ты не в войсе",
                ephemeral=True
            )

        channel = interaction.user.voice.channel

        try:

            member = interaction.guild.get_member(
                int(self.user_id.value)
            )

            overwrite = channel.overwrites_for(member)

            overwrite.connect = True

            await channel.set_permissions(
                member,
                overwrite=overwrite
            )

            await interaction.response.send_message(
                f"➕ Доступ выдан: {member.mention}",
                ephemeral=True
            )

        except:

            await interaction.response.send_message(
                "❌ Ошибка permit",
                ephemeral=True
            )

# =========================================
# DENY USER MODAL
# =========================================

class DenyUserModal(
    discord.ui.Modal,
    title="Забрать доступ"
):

    user_id = discord.ui.TextInput(
        label="ID пользователя",
        placeholder="Введите ID"
    )

    async def on_submit(
        self,
        interaction: discord.Interaction
    ):

        if not interaction.user.voice:
            return await interaction.response.send_message(
                "❌ Ты не в войсе",
                ephemeral=True
            )

        channel = interaction.user.voice.channel

        try:

            member = interaction.guild.get_member(
                int(self.user_id.value)
            )

            overwrite = channel.overwrites_for(member)

            overwrite.connect = False

            await channel.set_permissions(
                member,
                overwrite=overwrite
            )

            await interaction.response.send_message(
                f"➖ Доступ забран: {member.mention}",
                ephemeral=True
            )

        except:

            await interaction.response.send_message(
                "❌ Ошибка deny",
                ephemeral=True
            )