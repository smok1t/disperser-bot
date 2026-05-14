import discord

# =========================================
# ПРОВЕРКА OWNER
# =========================================

async def is_owner(interaction):

    if not interaction.user.voice:
        return False

    channel = interaction.user.voice.channel

    return channel.name.endswith(interaction.user.name)