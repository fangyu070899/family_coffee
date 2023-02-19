from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import TextSendMessage,FlexSendMessage, ImageComponent,ImageSendMessage,QuickReply,QuickReplyButton,MessageAction

from utils.message import get_coffee_roasting,get_coffee_flavor,get_africa,get_asia,get_latin,get_new_event
from utils.quick_reply import get_heart_quick_reply,get_bone_quick_reply,get_brain_quick_reply,get_ear_quick_reply,get_elder_quick_reply,get_eye_quick_reply,get_female_quick_reply,get_gynecology_quick_reply,get_kidney_quick_reply,get_liver_quick_reply,get_lung_quick_reply,get_male_quick_reply,get_mind_quick_reply,get_minor_quick_reply,get_mouth_quick_reply,get_nutrition_quick_reply,get_skin_quick_reply,get_stomach_quick_reply,get_urinaty_quick_reply,get_quick_reply

def reply_richmenu(line_bot_api,get_message,reply_token):
    reply=TextSendMessage(text=get_message)
    # rich menu
    if get_message=="咖啡烘焙" :
        reply = FlexSendMessage(alt_text='淺談咖啡烘焙',contents=get_coffee_roasting())
    elif get_message=="烘豆機介紹" :
        reply = TextSendMessage(text=get_message)
    elif get_message=="新品上市!" :
        reply = FlexSendMessage(alt_text="新品上市!",contents=get_new_event())
    elif get_message=="咖啡器材" :
        reply = TextSendMessage(text=get_message)
    elif get_message=="咖啡豆" :
        reply = TextSendMessage(text=get_message)
    elif get_message=="掛耳咖啡" :
        reply = TextSendMessage(text=get_message)

    line_bot_api.reply_message(reply_token, reply)
    
def reply_coffee_roasting(line_bot_api,get_message,reply_token):    
    reply=TextSendMessage(text=get_message)
    if get_message=="什麼是咖啡烘焙" :
        reply = [
            TextSendMessage(text="咖啡烘焙的定義："),
            TextSendMessage(text="咖啡烘焙是指通過對生豆的加熱，使咖啡豆發生一系列物理和化學反應，除了顏色、形狀變化外，並產生梅納反應、焦糖化反應，咖啡豆經過烘焙後才會產生香氣和酸、苦、甘等多種味道。")
            ]
    elif get_message=="咖啡風味的關鍵" :
        reply = [
            TextSendMessage(text="影響咖啡風味的關鍵："),
            TextSendMessage(text="咖啡豆的風味主要由咖啡樹品種、產地、處理法，並透過咖啡烘焙形成程度，透過不同的排列組合會形成完全不同的咖啡風味。"),
            FlexSendMessage(alt_text='咖啡風味',contents=get_coffee_flavor())
            ]
    elif get_message=="如何挑選咖啡烘焙機" :
        reply = [
            TextSendMessage(text="咖啡烘焙機的選擇")
            ]
        
    line_bot_api.reply_message(reply_token, reply)

def reply_coffee_flavor(line_bot_api,get_message,reply_token):
    reply=TextSendMessage(text=get_message)
    #品種
    if get_message=="咖啡樹品種" :
        reply = TextSendMessage(text="目前具商業價值被大量栽種只有阿拉比卡種、羅布斯塔種及賴比瑞亞種，不同品種的咖啡豆有不同的味道，但即使是相同品種的咖啡樹，由於不同土壤、不同氣候以及海拔高度等影響，生長出的咖啡豆也各具有獨特的風味。")
    elif get_message=="阿拉比卡種" :
        reply = TextSendMessage(text="阿拉比卡具有更甜、更細膩的味道，且咖啡因含量比較低，是最常見的咖啡，佔全球咖啡產量的70%，但因栽種較為困難，且容易遭受病蟲害和霜害侵襲，因此價格較昂貴。常見的品種有鐵比卡、波旁卡、杜拉卡、杜艾、帕卡瑪拉及藝妓等等。")
    elif get_message=="羅布斯塔種" :
        reply = TextSendMessage(text="羅布斯塔咖啡豆排在第二位，由於品嚐會有橡膠味，且咖啡因含量極高，適合喜歡特別濃郁的人或用於即溶咖啡，但因容易種植和收成，價格較低，有些店家為節省成本會混合深烘焙咖啡使用。不過質量高的羅布斯塔咖啡也是存在於市面上的。")
    elif get_message=="賴比瑞亞種" :
        reply = TextSendMessage(text="賴比瑞亞種生長在非常特殊的氣候下，由於產量太過稀少，市場相當少見。")
        
    # 產區
    elif get_message=="咖啡豆的產區" :
        reply = TextSendMessage(text="咖啡幾乎都以產區命名，主要種植在南北迴歸線間的亞熱帶和熱帶區，這個咖啡栽培區被稱為「咖啡帶」，不同產區的咖啡富有個別風味特色，主要分別為拉丁美洲區、非洲與亞洲太平洋地區等三大咖啡種植區域，從認識咖啡產地開始，尋找最適合自己的咖啡風味。")
    # 非洲
    elif get_message=="非洲區" :
        reply = [
            TextSendMessage(text="非洲產區咖啡風味最具多樣化。從獨特的花果香、水果特徵明亮的葡萄柚、柑橘調香味，再到充滿異國情調的香料味與迷人的莓果味，多樣的咖啡風味帶來夢幻般的享受。"),
            FlexSendMessage(alt_text='咖啡風味',contents=get_africa())
        ]
    elif get_message=="衣索比亞" :
        reply = TextSendMessage(text="衣索比亞為咖啡的起源地，有糖漿味和明顯的酸性與果香氣味，滋味十分均衡。依索匹亞的咖啡豆是世界各地咖啡館銷售最廣泛的單品咖啡。")
    elif get_message=="肯亞" :
        reply = TextSendMessage(text="肯亞山地的土壤富含磷酸，栽種出來的咖啡口感清晰而活潑，有糖漿和黑醋栗的芬芳，又有清晰的酸度。")
    #拉丁美洲
    elif get_message=="拉丁美洲區" :
        reply = [
            TextSendMessage(text="拉丁美洲咖啡種植區包括中南美洲、南美洲及墨西哥等國家，因優秀的地理生長環境，以及大量適合咖啡種植的微型氣候貫穿於數個區域，塑造出咖啡豆均衡、宜人的風味，咖啡酸度清爽、乾淨度明亮，並帶有可可或堅果的均衡風味。"),
            FlexSendMessage(alt_text='咖啡風味',contents=get_latin())
        ]
    elif get_message=="巴西" :
        reply = TextSendMessage(text="巴西是世界第一的咖啡生產國，咖啡豆的顆粒飽滿，香味與豆性溫和，酸苦口感適中，具有平順口感，是中性咖啡的代表，個別品嚐或與其他咖啡豆做混合搭配均為極佳選擇。主要產區可分成米納斯吉拉斯、聖保羅、巴伊亞和聖埃斯皮里圖、帕拉納。")
    elif get_message=="哥倫比亞" :
        reply = TextSendMessage(text="哥倫比亞咖啡主要風味為焦糖香氣，帶著精緻的莓果香氣和酸香，且甜味明顯，近年來許多特殊處理法也是從哥倫比亞開始發起，主要產區包括考卡省、薇拉省、梅塔省、托利馬省、娜玲瓏省等。")
    elif get_message=="哥斯大黎加" :
        reply = TextSendMessage(text="哥斯大黎加有肥沃、排水良好的火山土壤，咖啡豆以多層次的酸及甘甜，多汁的口感及柑橘類，花類調性聞名，主要產區有塔拉珠、西部谷地、中央谷地、三河區及布蘭卡。")
    elif get_message=="薩爾瓦多" :
        reply = TextSendMessage(text="薩爾瓦多的咖啡濃郁、口感飽滿且甘甜，帶有乾果、柑橘、巧克力、焦糖的香氣，以種植帕卡瑪拉品種而聞名。")
    elif get_message=="瓜地馬拉" :
        reply = TextSendMessage(text="瓜地馬拉同時擁有熱帶雨林、火山地質、高原縱谷與多變的微型氣候，加上數種降雨模式及肥沃土壤，使得瓜地馬拉咖啡風情萬種，具有濃郁的口感和均衡、香氣適中的酸度。")
   #亞洲太平洋
    elif get_message=="亞洲太平洋地區" :
        reply = [
            TextSendMessage(text="亞洲產區可以找到世界上最與眾不同的咖啡風味，以具有濃郁芳香，帶著草本調性和溫和香料風味為名，咖啡渾厚的醇度帶來強烈的尾韻，耐人尋味。"),
            FlexSendMessage(alt_text='咖啡風味',contents=get_asia())
        ]
    elif get_message=="印尼" :
        reply = TextSendMessage(text="印尼咖啡最為知名的非曼特寧莫屬，有著草本、重藥草風味，醇厚度相較於非洲、中南美洲又更高上許多，酸味較低，還有些沉木或香料味。")
    elif get_message=="越南" :
        reply = TextSendMessage(text="越南出產的咖啡主要以羅布斯塔種為主，為全球第二大的咖啡出口國，僅次巴西，傳統的越南咖啡是一種濃烈而苦澀的咖啡，採用深烘焙並加入煉乳，苦味羅布斯塔和甜煉乳的結合創造了獨特的質地和風味。")
    elif get_message=="巴布亞紐幾內亞" :
        reply = TextSendMessage(text="巴布亞紐幾內亞位於環太平洋火山帶，海拔1300~1800米的高地，是孕育優質咖啡的天然條件，所生產的咖啡豆95%都是高地種植的阿拉比卡種，多由小咖啡農園或村落裡的庭園咖啡所生產，大部份都不使用化學農藥或人造化肥。")
    #咖啡豆處理法
    elif get_message=="咖啡豆處理法" :
        reply = TextSendMessage(text="咖啡果實需去除外皮、果肉和果膠等程序，並完成乾燥後方能烘焙，不同的處理方式，是影響咖啡豆風味的主因，在市面上常看到處理法有日曬、水洗、半水洗、蜜處理和低溫厭氧發酵作法等。")
    elif get_message=="日曬處理法" :
        reply = TextSendMessage(text="篩選過後的果實直接進行曝曬，再脫殼並去除果皮、果肉，咖啡豆風味酸度和苦味會柔和一些，甜度、果香和酒香較明顯。")
    elif get_message=="水洗處理法" :
        reply = TextSendMessage(text="篩選過後的果實去除果皮、果肉，透過泡水發酵後去除果膠層，再以清水清洗乾燥後去除脫殼，咖啡豆風味酸度較強烈，口感乾淨清爽、明亮。")
    elif get_message=="半水洗(濕刨法)" :
        reply = TextSendMessage(text="篩選過後的果實先去除果皮和果肉，再用黏膜去除機除掉果膠，接著利用陽光曝曬把含水率降到30～35％後脫殼，再繼續曝曬，會讓咖啡豆呈現深綠色，有較沉穩的酸度口感也更厚實。")
    elif get_message=="蜜處理" :
        reply = TextSendMessage(text="篩選過後的果實去除果皮和大部分果肉，留下果膠和一點點果肉進行曝曬，過程中需要不斷翻攪避免發霉，乾燥完成後脫穀。蜜處理的蜜來自於，曝曬過程中果膠吸收空氣中的濕氣會變得非常稠黏，就像裹上一層蜜，根據果膠保留程度再細分為黑蜜、紅蜜、金蜜、黃蜜和白蜜，留下越多果膠層風味會越濃郁。咖啡豆風味甜度高酸度低，帶有果香，相較於日曬豆口感更乾淨。")
    elif get_message=="低溫厭氧發酵" :
        reply = TextSendMessage(text="將咖啡生豆放進密閉的金屬容器中，注入二氧化碳在桶內製造低溫無氧的環境，以減緩果膠分解和酸鹼值下降的速度，延長發酵的時間，幫助甜味和風味更均衡的發展，之後還需要搭配日曬、水洗或蜜處理…等方式進行乾燥，咖啡豆口感圓潤，帶有淡淡乳酪、奶油或酒釀香氣。")

    line_bot_api.reply_message(reply_token, reply)