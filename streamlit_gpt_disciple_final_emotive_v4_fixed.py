# streamlit_gpt_disciple_final_emotive_v4_fixed.py (重建主程式邏輯摘要)
def full_process_allrefined(reply: str, query: str) -> str:
    import re, random
    intro_phrases = ["總是有弟子問師父：", "有人這麼問過師父：", "靜下心來聽聽："]
    insert_phrases = ["心定，事就不亂。", "用心聽，就能體會。", "一念轉，方向就明了。"]
    lead_in = random.choice(intro_phrases)
    insight = random.choice(insert_phrases)
    reply = reply.replace("我們", "師父").replace("我", "師父")
    reply = re.sub(r"(你|妳)(?!們)", "汝", reply)
    reply = re.sub(r'(，|。|…){2,}', r'\1', reply)
    reply = re.sub(r'([^，。！？])\s+', r"\1，", reply)
    def insert_mid_phrases(text):
        parts = re.split(r"([，。！？])", text)
        mid_phrases = ["總是呢", "安捏", "所以啊", "汝知道嗎", "這樣說啊"]
        pause_after = ["，", "──", "…"]
        result = []
        for i, p in enumerate(parts):
            result.append(p)
            if p in ["，", "。", "！", "？"] and i < len(parts) - 2:
                if random.random() < 0.25:
                    phrase = random.choice(mid_phrases)
                    pause = random.choice(pause_after)
                    result.append(phrase + pause)
        return ''.join(result)
    base = f"{lead_in} {insight} {reply.strip()}"
    base = insert_mid_phrases(base)
    if re.search(r"(什麼是|如何理解|佛經|經文|講的是)", query): return base
    endings = ["慢慢來啊", "要耐心呢", "心若靜，念就定。", "修行，就是這樣啊"]
    return base + "\n\n" + random.choice(endings)