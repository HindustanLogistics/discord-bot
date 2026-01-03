import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ===== BOT READY =====
@bot.event
async def on_ready():
    print(f"✅ Bot logged in as {bot.user}")

# ===== WELCOME + AUTO ROLE =====
@bot.event
async def on_member_join(member):
    # Welcome channel
    channel = discord.utils.get(member.guild.text_channels, name="welcome")

    # Auto role
    role = discord.utils.get(member.guild.roles, name="Member")
    if role:
        await member.add_roles(role)

    if channel:
        embed = discord.Embed(
            title="👋 Welcome!",
            description=f"Welcome {member.mention} to **{member.guild.name}** 🚛\n\n"
                        "Please read the rules and enjoy trucking!",
            color=0x00ff00
        )
        embed.set_footer(text="Drive safe & follow rules")
        await channel.send(embed=embed)

# ===== BASIC COMMANDS =====
@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong! Bot is online.")

# ===== VTC COMMANDS =====
@bot.command()
async def vtc(ctx):
    await ctx.send(
        "**🚚 Legacy Transport [LTVTC]**\n"
        "🌍 International Virtual Trucking Company\n"
        "🎮 TruckersMP Supported\n"
        "📌 Drive safe & respect everyone"
    )

@bot.command()
async def rules(ctx):
    await ctx.send(
        "📜 **Server Rules**\n"
        "1️⃣ Respect everyone\n"
        "2️⃣ No spam\n"
        "3️⃣ Follow TruckersMP rules\n"
        "4️⃣ No reckless driving"
    )

@bot.command()
async def apply(ctx):
    await ctx.send(
        "📝 **Apply for LTVTC**\n"
        "Join our Discord and open an application ticket.\n"
        "We are happy to have you 🚛"
    )

@bot.command()
async def truckersmp(ctx):
    await ctx.send(
        "🎮 **TruckersMP Info**\n"
        "Website: https://truckersmp.com\n"
        "Follow all TMP rules while driving."
    )

# ===== STAFF ANNOUNCEMENT (ADMIN ONLY) =====
@bot.command()
@commands.has_permissions(administrator=True)
async def announce(ctx, *, message):
    embed = discord.Embed(
        title="📢 ANNOUNCEMENT",
        description=message,
        color=0xff0000
    )
    await ctx.send(embed=embed)

@announce.error
async def announce_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("❌ You don't have permission to use this command.")

# ===== RUN BOT =====
import os
bot.run(os.getenv("TOKEN"))