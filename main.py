import discord
client = discord.Client(intents=discord.Intents.default())
tree = discord.app_commands.CommandTree(client)
TOKEN = "토큰 넣기"
@client.event
async def on_ready():
    print(f"봇 {client.user} 이 켜졌습니다 현제 셈플 봇 버전 0.01 all copyright to bob_love 저희 셈플을 사용해 주셔서 감사합니다")
    await tree.sync()
    ac=discord.activity.Activity(name="셈플봇!",type=discord.ActivityType.listening)
    await client.change_presence(activity=ac)
client.run(TOKEN)
