import discord
from discord.ext import commands

# ตั้ง Prefix คำสั่ง เช่น !add, !remove
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

# เก็บรายชื่อคนที่ต้องเช็คชื่อ
attendance = {}

@bot.event
async def on_ready():
    print(f'✅ บอท {bot.user} ออนไลน์แล้ว!')

@bot.command()
async def add(ctx, name: str):
    """เพิ่มรายชื่อ"""
    if name not in attendance:
        attendance[name] = False
        await ctx.send(f'เพิ่มชื่อ {name} เรียบร้อย ✅')
    else:
        await ctx.send(f'{name} มีอยู่แล้วในระบบ ❗')

@bot.command()
async def remove(ctx, name: str):
    """ลบรายชื่อ"""
    if name in attendance:
        del attendance[name]
        await ctx.send(f'ลบชื่อ {name} แล้ว ❌')
    else:
        await ctx.send(f'ไม่พบชื่อ {name}')

@bot.command()
async def check(ctx, name: str):
    """ติ๊กชื่อว่าเช็คแล้ว"""
    if name in attendance:
        attendance[name] = True
        await ctx.send(f'{name} มาเช็คชื่อแล้ว 🟢')
    else:
        await ctx.send(f'ไม่พบชื่อ {name}')

@bot.command()
async def list(ctx):
    """แสดงรายชื่อทั้งหมด"""
    if not attendance:
        await ctx.send("ยังไม่มีรายชื่อในระบบ 📋")
        return

    report = "\n".join([f"{'🟢' if v else '🔴'} {k}" for k, v in attendance.items()])
    await ctx.send(f"**รายชื่อทั้งหมด:**\n{report}")

# ---- ใส่ Token ของคุณตรงนี้ ----
bot.run("MTQyNTQ3NDczODUwMzAyNDcxMQ.G5iB2J.JQ7wuRdrs34nVgA8MoIZJ5rYGRFGWNgppJsRVs")
