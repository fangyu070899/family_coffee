from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import TextSendMessage,FlexSendMessage, ImageComponent,ImageSendMessage,QuickReply,QuickReplyButton,MessageAction

from utils.message import get_coffee_extract,get_coffee_kind,get_about_coffee,get_coffee_flavor,get_africa,get_asia,get_latin,get_new_event,get_coffee_equipment,get_coffee_filter_cup,get_coffee_filter,get_coffee_knife

def reply_richmenu(line_bot_api,get_message,reply_token):
    reply=TextSendMessage(text=get_message)
    # rich menu
    if get_message=="淺談咖啡" :
        reply = [
            TextSendMessage(text="越來越多人選擇自己在家裡沖咖啡，一杯好咖啡的關鍵是什麼？好的沖泡技巧和器具固然不可或缺，但高品質的咖啡豆才是最重要的元素。我們用最淺顯易懂的方式，介紹有關咖啡豆的重要知識，讓您認識咖啡，進而挑選自己喜歡的咖啡~"),
            FlexSendMessage(alt_text='淺談咖啡',contents=get_about_coffee())
            ]
    elif get_message=="新品上市!" :
        reply = FlexSendMessage(alt_text="新品上市!",contents=get_new_event())

    line_bot_api.reply_message(reply_token, reply)
    
def reply_about_coffee(line_bot_api,get_message,reply_token):    
    reply=TextSendMessage(text=get_message)
    if get_message=="我喝的是什麼咖啡?" :
        reply = [
            FlexSendMessage(alt_text='咖啡種類',contents=get_coffee_kind())
            ]
    elif get_message=="影響咖啡風味的關鍵" :
        reply = [
            TextSendMessage(text="咖啡豆的風味主要由咖啡樹品種、產地、處理法，並透過咖啡烘焙形成程度，透過不同的排列組合會形成完全不同的咖啡風味。"),
            FlexSendMessage(alt_text='咖啡風味',contents=get_coffee_flavor())
            ]
    elif get_message=="如何萃取一杯好咖啡?" :
        reply = [
            TextSendMessage(text="美國精品協會SCAA為了能夠更系統性的建立咖啡與萃取之間的關係，提出了金杯理論，歸納出一杯好咖啡正確的萃取率應介於18%~22%，而濃度則需介於1.15% ~ 1.45%。除了確立萃取率的標準外，更重要的目的是能讓咖啡師的萃達到均勻和一致性，而影響萃取咖啡的要素有~"),
            FlexSendMessage(alt_text='萃取咖啡',contents=get_coffee_extract())
            ]
        
    line_bot_api.reply_message(reply_token, reply)

def reply_coffee_kind(line_bot_api,get_message,reply_token):    
    reply=TextSendMessage(text=get_message)
    if get_message=="單品咖啡" :
        reply = [
            TextSendMessage(text="單品咖啡廣泛指該咖啡豆來自「單一產區」，也就是同一個莊園、處理廠或合作社，消費者可以確切知道咖啡的來源，看得到生產履歷。"),
            TextSendMessage(text="通常代表著更高品質的風味與高水準的處理，以杯測分數滿分來看，達到60分但未滿80分就屬於商業咖啡，而杯測分數如果達到80分以上就可稱為精品咖啡。")
            ]
    elif get_message=="綜合咖啡" :
        reply = [
            TextSendMessage(text="通常是由兩種以上的咖啡豆，以不同比例混合調配出來的咖啡豆，讓各具特色的單品咖啡共同譜出更和諧、更精彩的樂章。"),
            TextSendMessage(text="使用綜合配方，可以創造出一個更獨特的產品，更貼近市場需求，甚至比其單獨成分的品質與風味更好。")
            ]
    elif get_message=="精品咖啡" :
        reply = [
            TextSendMessage(text="精品咖啡的定義最早於1978年，由美國努森女士於法國舉行的國際咖啡會議提出，指在特別氣候與地理條件下培育出具有獨特風味的咖啡豆。"),
            TextSendMessage(text="其後精品咖啡協會（SCA），認為一杯精品咖啡並不單指已被沖煮好、送到消費者口中的那杯咖啡，而是強調產出這杯咖啡的整個流程，而這個流程從農民的栽種、生豆商對豆子的嚴選、烘焙生豆的烘焙師、沖煮咖啡的咖啡師到最後品嚐風味的消費者，都是成就一杯精品咖啡的重要角色。")
            ]
        
    line_bot_api.reply_message(reply_token, reply)

def reply_coffee_extract(line_bot_api,get_message,reply_token):    
    reply=TextSendMessage(text=get_message)
    if get_message=="沖煮器材" :
        reply = [
            TextSendMessage(text="同樣的咖啡豆在不同的沖煮器材所呈現的咖啡風味差異相當大，常見得咖啡沖煮器材有~"),
            FlexSendMessage(alt_text='沖煮器材',contents=get_coffee_equipment())
            ]
    elif get_message=="粉水比" :
        reply = TextSendMessage(text="咖啡萃取最先被釋出的是香氣和酸感，於中後才會陸續帶出甜感和苦感，若過度萃取，則會擁有過重的苦味和澀感，萃取不足則有臭酸味、缺乏甜味、奇怪的鹹味以及讓人失望的短餘韻。所以，針對不同沖煮方式，搭配適合的咖啡粉粗細度和各項參數，咖啡豆和水量的比例（粉水比），一般是 1：12 至 1：18，前者味道較濃，後者偏淡。初學者可以從 1：16 開始嘗試。")
            
    elif get_message=="研磨刻度與對應沖煮時間" :
        reply = [
            TextSendMessage(text="通常來說，咖啡與水接觸時間較長的，也就是浸泡時間長的，像聰明濾杯、法壓壺、手沖都會將咖啡顆粒磨的粗一點。咖啡與水接觸時間較短的，像義式就會將顆粒磨細一點。淺焙可以更細一點，深焙的話粗一些，掌握這個大方向基本就很清楚囉！"),
            TextSendMessage(text="市面上的各種磨豆機都有其特色，不同刀盤構造也有其適合研磨的粗細程度，最常見的刀盤種類分別為鬼齒、錐刀以及平刀~"),
            FlexSendMessage(alt_text='刀盤種類',contents=get_coffee_knife())
            ]
    elif get_message=="正確的溫度、時間、擾流(3T)" :
        reply = TextSendMessage(text="咖啡沖煮的好壞，關鍵在於咖啡顆粒是否吸到足夠的水，相同萃取時間下，水溫越高，咖啡中揮發性的香氣與水溶性物質會更快的被釋出；水溫越低，較沒辦法萃取出完整的風味物質，通常水溫大約在85~95度之間。另外擾流可以讓咖啡粉粒平均吸水，呈現飽和狀態，適當的入水速率、研磨的刻細度、濾杯的材質、尺寸與形狀都有著莫大關聯。")
            
    elif get_message=="水質" :
        reply = TextSendMessage(text="水，佔一杯咖啡 98％ 的份量，當然對咖啡的風味有極大的影響，水中含有許多的礦物質，在萃取咖啡時會和咖啡粉產生微妙的化學變化，影響咖啡呈現出的風味，根據精品咖啡協會的水質建議，TDS在75~250ppm，理想值為150ppm；總硬度建議在50~175ppm；PH值6.5~7.5，理想值為 6~8。")
    elif get_message=="過濾器材" :
        reply = [
            TextSendMessage(text="不同材質的濾網確實存在很大的差異，常見的有~"),
            FlexSendMessage(alt_text='不同材質的濾網',contents=get_coffee_filter())
            ]
    line_bot_api.reply_message(reply_token, reply)

def reply_coffee_equipment(line_bot_api,get_message,reply_token):    
    reply=TextSendMessage(text=get_message)
    if get_message=="義式濃縮咖啡機" :
        reply = TextSendMessage(text="濃縮咖啡（Espresso）是商用咖啡的首選沖煮方法，適合喜愛濃醇咖啡的咖啡人，可直接飲用，也可製成拿鐵、瑪奇朵、卡布奇諾等花式咖啡。店家也常會用自製綜合咖啡豆，以表現獨特咖啡特色。 1：12 至 1：18，前者味道較濃，後者偏淡。初學者可以從 1：16 開始嘗試。")
           
    elif get_message=="摩卡壺" :
        reply = TextSendMessage(text="摩卡壺又稱為蒸氣沖煮式咖啡壺、爐頂義大利咖啡壺，內部由下至上共分成裝水、裝咖啡粉、裝煮好的咖啡三個區間，放在爐上加熱，使水產生蒸氣，增加底部隔間裡的壓力，把水向上推過咖啡細粒，最後進入上層隔間，等到咖啡裝滿上層隔間時，即可倒出飲用，是一款藉由簡單的蒸氣壓物理作用所煮出的香醇咖啡，便於攜帶且堅固耐用，是露營的良伴。")
            
    elif get_message=="虹吸壺又稱賽風壺" :
        reply = TextSendMessage(text="運用虹吸現象萃取咖啡的器具，下壺的水經過加熱推入導管並抽至上壺，以進行萃取，當下壺停止加熱後，上壺的咖啡液，因失去下壺水蒸氣的支撐而重新往下壺流去，咖啡渣則被濾布擋住而留在上壺，這種萃取法能夠均衡萃取出咖啡豆原有的特色及風味。"),
            
    elif get_message=="法式濾壓壺" :
        reply = TextSendMessage(text="像泡茶般的簡單沖泡法，將咖啡粉和熱水倒入濾壓壺中，均勻攪拌後蓋上濾網及蓋子，等待約4分鐘的萃取時間，即可把濾網壓下，倒出咖啡液體享用，這也最接近原始的咖啡飲用方式，因浸泡時間較長，咖啡因含量也相對偏高。")
            
    elif get_message=="聰明濾杯" :
        reply = TextSendMessage(text="聰明濾杯為咖啡界的革命性商品，傻瓜式操作便可充分表現出精品咖啡的細緻風味，令人耳目一新的沖泡效能，同時兼具法式濾壓壺與手沖濾杯的優點，既可提供法式濾壓壺完全浸泡的環境，保留咖啡油脂使風味飽滿圓潤，且兼顧了手沖濾杯的過濾功能，可將咖啡粉渣完全濾除避免干擾口感。")
    elif get_message=="手沖咖啡" :
        reply = [
            TextSendMessage(text="手沖咖啡為最普遍的咖啡沖煮方式，不少人會依據咖啡豆的烘培程度，選用適當流速的濾杯以求最好的口感，另外不同材質的濾杯，溫度也會有些微變化，風味更會因此有所差異！是不少咖啡人的最愛，雖然器具簡單，但由於熱水的流速、方向、溫度皆由沖煮者控制，因此幾乎每次沖煮出來的咖啡風味都不同，沖煮體驗樂趣多。"),
            TextSendMessage(text="濾杯的流速快，咖啡體較為輕盈、口感上也偏酸以及清爽；濾杯的流速慢，咖啡體則較為醇厚、口感上也會偏苦甜以及濃郁，目前市面上常見的濾杯形狀，大致上可分為錐形、扇形與波浪/蛋糕形等三種，除濾杯形狀不同，肋骨不同的排列組合，亦會影響流速。"),
            FlexSendMessage(alt_text='濾杯種類',contents=get_coffee_filter_cup())
            ]
    line_bot_api.reply_message(reply_token, reply)

def reply_coffee_filter_cup(line_bot_api,get_message,reply_token):    
    reply=TextSendMessage(text=get_message)
    if get_message=="錐形濾杯" :
        reply = TextSendMessage(text="錐形濾杯為單孔濾杯，孔洞較大、流速較快，故咖啡粉和水所接觸的時間較短，沖煮出的咖啡體口感則較為清爽，但須注意水量和流速的控制，以避免咖啡體有過於清淡的狀況產生。")
           
    elif get_message=="扇型濾杯" :
        reply = TextSendMessage(text="扇形濾杯內部紋理明顯，可避免濾紙完全貼合濾杯，讓水流、空氣等可以更順暢流通，下方以單孔、雙孔、三孔最為常見，因孔洞較小流速也較慢，故咖啡所需的萃取時間則會偏長，沖煮完成的咖啡體口感也較為厚實。")
            
    elif get_message=="波浪/蛋糕型濾杯" :
        reply = TextSendMessage(text="蛋糕型濾杯因使用的濾紙像杯子蛋糕而得名，並搭配平面的底部做為設計，波浪般的特殊摺痕，有效避免濾紙與濾杯因沖煮後過於貼合，咖啡粉也因此更可以被均勻萃取，平底的設計還能穩定流速，而因為沖煮較偏向浸泡式，故咖啡體層次較不明顯、風味較均勻。"),
            
    line_bot_api.reply_message(reply_token, reply)

def reply_coffee_filter(line_bot_api,get_message,reply_token):    
    reply=TextSendMessage(text=get_message)
    if get_message=="法蘭絨濾布" :
        reply = TextSendMessage(text="法蘭絨是用毛線編織而成，所以在結構上會有既定的隙縫。這隙縫提供了良好空氣流動 ，但是毛線也會因為吸到水份而產生膨脹的現象，毛線的張力遠大於濾紙的纖維，所以水份會停留在濾布好一段時間，這時毛線間的隙縫也會變小，看似空氣流動受阻，但是卻大大增加顆粒可以吸水飽和的時間！因此法蘭絨可以容易煮出濃度較佳香氣明顯的咖啡。")
           
    elif get_message=="濾紙" :
        reply = TextSendMessage(text="濾紙的纖維細緻，能夠過濾細粉與大部分油脂，外觀與風味上比起金屬濾網較透明清澈，更突顯甜感與果香。濾紙的成分可以是天然、合成、甚至玻璃纖維，白色濾紙經由氯氣或氧氣漂白過，棕色濾紙則是未經漂白的天然顏色。")
            
    elif get_message=="金屬濾網" :
        reply = TextSendMessage(text="金屬咖啡過濾網常為不鏽鋼材質，可以直接用來萃取咖啡，但因孔洞較大，會讓油脂、細粉等物質穿透而進入咖啡中，讓咖啡看起來較深且混濁，風味上較鮮明、豐富，並且會在杯底形成沉澱，與法式濾壓壺沖泡的咖啡類似。"),
            
    line_bot_api.reply_message(reply_token, reply)

def reply_coffee_knife(line_bot_api,get_message,reply_token):    
    reply=TextSendMessage(text=get_message)
    if get_message=="平刀" :
        reply = TextSendMessage(text="藉由削平的方式研磨咖啡豆，咖啡粉粒的外觀多以片狀呈現，適合細研磨，因咖啡粉細緻則萃取面積大，故短時間內就能提升咖啡濃度，並萃取出多樣化的風味，香氣也最為濃郁，缺點細粉較多、咖啡粉粒大小較不平均，若是萃取時間太長，容易因過度萃取而帶出苦味、澀味、雜味。")
           
    elif get_message=="錐刀" :
        reply = TextSendMessage(text="藉由輾壓的方式研磨咖啡豆，咖啡粉粒的外觀接近顆粒狀，適合粗研磨，顆粒較為均勻、細粉較少，因咖啡粉粒為粗顆粒而萃取面積較小，故咖啡濃度平衡，較不易過度萃取，也因此大大提升了咖啡的層次變化，常見的錐刀電動磨豆機以用於意式濃縮為主；而手動錐刀磨豆機則是以手沖咖啡為主。")
            
    elif get_message=="鬼齒刀" :
        reply = TextSendMessage(text="研磨主要以打磨的方式將咖啡豆研磨成顆粒，因此其外形以較接近橢圓形爲主，研磨後的咖啡粉粒粗細平均、風味乾淨明亮、飽滿平衡，但缺少層次變化。"),
            
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

def reply_coffee_items(line_bot_api,get_message,reply_token):
    reply=TextSendMessage(text=get_message)

    if get_message=="肯亞 涅里 聶絲紅/洛神紅 AA" :
        reply = [
            TextSendMessage(text="國家：肯亞\n產區 : 涅里\n海拔 : 約1,600 - 1,750m\n品種 : SL28, SL34\n處理法 : 傳統肯亞式水洗處理法+非洲式高架棚架日曬乾燥"),
            TextSendMessage(text="風味短評 : \n乾香為小紅莓、蔓越莓、洛神與仙楂香氣。入口時可感受到酸甜的黑醋栗、蔓越莓與橘汁風味，伴隨著洛神花、仙楂、梅心糖香氣，風味濃郁厚實。")
        ]
    elif get_message=="衣索比亞 耶珈雪啡 果丁丁村G1 阿利姆布卡托" :
        reply = [
            TextSendMessage(text="國家：衣索比亞\n產區 : 耶珈雪啡/歌迪貝\n生產者 : 阿利姆布卡托\n海拔 : 2020公尺\n品種 : 衣索比亞古優原生種\n處理法 : 全紅果高架棚架日曬"),
            TextSendMessage(text="風味短評 : \n乾香為草莓、水蜜桃與佛手柑香氣。啜吸時為香甜的豐香草莓果醬、完熟水蜜桃風味，伴隨著藍莓及佛手柑清香，細緻的佛手柑與白桃延續至餘韻，風味層次豐富。")
        ]
    elif get_message=="衣索比亞 水洗耶珈雪啡 尼羅河花園/波塔巴 G1" :
        reply = [
            TextSendMessage(text="國家 : 衣索比亞\n產區 : 科洽雷/歌迪貝\n海拔 : 1,900 - 2,100公尺\n品種 : 衣索比亞古優品種\n年雨量 : 約 1,500 - 2,000 mm\n處理法 : 傳統發酵水洗，非洲式棚架日曬乾燥"),
            TextSendMessage(text="風味短評 : \n乾香可感受到細緻的橙花、檸檬皮、佛手柑與水蜜桃香氣。風味同樣以濃郁多汁的水蜜桃、佛手柑、檸檬卡士達為主軸，伴隨著香甜玉荷包、些許杏桃及橙花香，餘韻帶有悠長烏龍茶花韻，柔滑細緻。")
        ]
    elif get_message=="衣索比亞 水洗希達馬 檸檬花蜜/茉莉雅" :
        reply = [
            TextSendMessage(text="國家：衣索比亞\n產區 : 希達馬\n海拔 : 1,800 - 2,200公尺\n品種 : 衣索比亞古優品種\n年雨量 : 約 1,500 - 2,000 mm\n處理法 : 傳統發酵水洗，非洲式棚架日曬乾燥"),
            TextSendMessage(text="風味短評 : \n乾香為橙皮、柚子、水蜜桃與清新花香。一入口即可感受到香甜多汁的水蜜桃、白葡萄與柚子茶，夾帶著佛手柑及蜂蜜香氣，結尾帶有烏龍茶花韻，酸值活潑細緻，層次豐富。")
        ]
    
    line_bot_api.reply_message(reply_token, reply)