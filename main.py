import requests

# 替换成你的智谱API Key
API_KEY = "7d3620c649994f2499aeb22dbd9ebab9.K1JoT9L18K4BUdt1"

def get_ai_response(prompt):
    """调用智谱GLM-4-Flash API（免费）"""
    url = "https://open.bigmodel.cn/api/paas/v4/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "glm-4-flash",  # 免费模型
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 500
    }
    
    try:
        response = requests.post(url, headers=headers, json=data, timeout=30)
        print("状态码：", response.status_code)  # 调试用
        if response.status_code == 200:
            result = response.json()
            return result['choices'][0]['message']['content']
        else:
            return f"API调用失败：{response.status_code}，{response.text}"
    except Exception as e:
        return f"请求出错：{e}"

def generate_morning_brief(topic):
    """根据话题生成晨报内容"""
    prompt = f"""你是一个专业的晨报编辑。请围绕「{topic}」这个话题，生成一份简短的晨报，格式如下：

【今日关注】
用2-3句话概括这个话题今天最值得关注的动态或趋势

【一句话总结】
用一句话总结这个话题的核心要点

要求：语言简洁有力，信息密度高，适合快速阅读。"""
    
    return get_ai_response(prompt)

def main():
    print("=" * 40)
    print("    AI晨报助手（输入话题生成晨报）")
    print("    （输入 'exit' 退出）")
    print("=" * 40)
    
    while True:
        topic = input("\n请输入话题：").strip()
        
        if topic.lower() == 'exit':
            print("再见！")
            break
        
        if not topic:
            print("话题不能为空，请重新输入")
            continue
        
        print(f"\n正在生成关于「{topic}」的晨报...\n")
        print("-" * 40)
        
        brief = generate_morning_brief(topic)
        print(brief)
        
        print("-" * 40)

if __name__ == "__main__":
    main()