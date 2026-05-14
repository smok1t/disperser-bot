import discord

from discord.ui import View
from discord.ui import Button

from views.modals import (
    RenameModal,
    LimitModal,
    BitrateModal,
    TransferOwnerModal,
    PermitUserModal,
    DenyUserModal
)

# =========================================

class VoicePanel(View):

    def __init__(self):
        super().__init__(timeout=None)

    # =====================================
    # ADD SLOT
    # =====================================

    @discord.ui.button(
        emoji="<:add_slot:1504538336080035980>",
        style=discord.ButtonStyle.secondary,
        custom_id="add_slot"
    )
    async def add_slot(
        self,
        interaction: discord.Interaction,
        button: Button
    ):

        if not interaction.user.voice:
            return await interaction.response.send_message(
                "❌ Ты не в войсе",
                ephemeral=True
            )

        channel = interaction.user.voice.channel

        limit = channel.user_limit + 1

        await channel.edit(
            user_limit=limit
        )

        await interaction.response.send_message(
            f"<:add_slot:1504538336080035980> Лимит увеличен: {limit}",
            ephemeral=True
        )

    # =====================================
    # REMOVE SLOT
    # =====================================

    @discord.ui.button(
        emoji="<:remove_slot:1504539217147990137>",
        style=discord.ButtonStyle.secondary,
        custom_id="remove_slot"
    )
    async def remove_slot(
        self,
        interaction: discord.Interaction,
        button: Button
    ):

        if not interaction.user.voice:
            return await interaction.response.send_message(
                "❌ Ты не в войсе",
                ephemeral=True
            )

        channel = interaction.user.voice.channel

        limit = max(channel.user_limit - 1, 0)

        await channel.edit(
            user_limit=limit
        )

        await interaction.response.send_message(
            f"<:remove_slot:1504539217147990137> Лимит уменьшен: {limit}",
            ephemeral=True
        )

    # =====================================
    # LOCK ROOM
    # =====================================

    @discord.ui.button(
        emoji="<:close_room:1504540207532343547>",
        style=discord.ButtonStyle.secondary,
        custom_id="close_room"
    )
    async def close_room(
        self,
        interaction: discord.Interaction,
        button: Button
    ):

        if not interaction.user.voice:
            return

        channel = interaction.user.voice.channel

        overwrite = channel.overwrites_for(
            interaction.guild.default_role
        )

        overwrite.connect = False

        await channel.set_permissions(
            interaction.guild.default_role,
            overwrite=overwrite
        )

        await interaction.response.send_message(
            "<:close_room:1504540207532343547> Комната закрыта",
            ephemeral=True
        )

    # =====================================
    # OPEN ROOM
    # =====================================

    @discord.ui.button(
        emoji="<:cloce_room_for_user:1504549635254124635>",
        style=discord.ButtonStyle.secondary,
        custom_id="cloce_room_for_user"
    )
    async def cloce_room_for_user(
        self,
        interaction: discord.Interaction,
        button: Button
    ):

        if not interaction.user.voice:
            return

        channel = interaction.user.voice.channel

        overwrite = channel.overwrites_for(
            interaction.guild.default_role
        )

        overwrite.connect = True

        await channel.set_permissions(
            interaction.guild.default_role,
            overwrite=overwrite
        )

        await interaction.response.send_message(
            "<:cloce_room_for_user:1504549635254124635> Комната открыта",
            ephemeral=True
        )

    # =====================================
    # RENAME
    # =====================================

    @discord.ui.button(
        emoji="<:rename_room:1504548012767187055>",
        style=discord.ButtonStyle.secondary,
        custom_id="rename_room"
    )
    async def rename_room(
        self,
        interaction: discord.Interaction,
        button: Button
    ):

        await interaction.response.send_modal(
            RenameModal()
        )

    # =====================================
    # LIMIT
    # =====================================

    @discord.ui.button(
        emoji="<:limit_slots:1504543630487195818>",
        style=discord.ButtonStyle.secondary,
        custom_id="limit_slots"
    )
    async def limit_slots(
        self,
        interaction: discord.Interaction,
        button: Button
    ):

        await interaction.response.send_modal(
            LimitModal()
        )

    # =====================================
    # BITRATE
    # =====================================

    @discord.ui.button(
        emoji="<:new_bitrate:1504543048237977642>",
        style=discord.ButtonStyle.secondary,
        custom_id="new_bitrate"
    )
    async def new_bitrate(
        self,
        interaction: discord.Interaction,
        button: Button
    ):

        await interaction.response.send_modal(
            BitrateModal()
        )

    # =====================================
    # TRANSFER OWNER
    # =====================================

    @discord.ui.button(
        emoji="<:transfer_rights:1504547267741225061>",
        style=discord.ButtonStyle.secondary,
        custom_id="transfer_rights"
    )
    async def transfer_rights(
        self,
        interaction: discord.Interaction,
        button: Button
    ):

        await interaction.response.send_modal(
            TransferOwnerModal()
        )

    # =====================================
    # MUTE USERS
    # =====================================

    @discord.ui.button(
        emoji="<:prohibit_speak:1504541149837262939>",
        style=discord.ButtonStyle.secondary,
        custom_id="prohibit_speak"
    )
    async def prohibit_speak(
        self,
        interaction: discord.Interaction,
        button: Button
    ):

        if not interaction.user.voice:
            return

        channel = interaction.user.voice.channel

        for member in channel.members:

            if member != interaction.user:

                await member.edit(
                    mute=True
                )

        await interaction.response.send_message(
            "<:prohibit_speak:1504541149837262939> Пользователи заглушены",
            ephemeral=True
        )

    # =====================================
    # KICK USERS
    # =====================================

    @discord.ui.button(
        emoji="<:delete_userr:1504542342726811842>",
        style=discord.ButtonStyle.secondary,
        custom_id="delete_userr"
    )
    async def delete_userr(
        self,
        interaction: discord.Interaction,
        button: Button
    ):

        if not interaction.user.voice:
            return

        channel = interaction.user.voice.channel

        for member in channel.members:

            if member != interaction.user:

                await member.move_to(None)

        await interaction.response.send_message(
            "<:delete_userr:1504542342726811842> Пользователи исключены",
            ephemeral=True
        )