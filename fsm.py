from transitions.extensions import GraphMachine
import random

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs	
        )
    def is_going_to_state1(self, update):
        mes=update.message
        text = mes.text
        return text == '/北部'

    def is_going_to_state2(self, update):
        mes=update.message
        text = mes.text
        return text == '/中部'
       
    def is_going_to_state3(self, update):
        mes=update.message
        text = mes.text
        return text == '/南部'

    def is_going_to_state4(self, update):
        mes=update.message
        text = mes.text
        return text == '/東部'
       
    def is_going_to_state5(self, update):
        mes=update.message
        text = mes.text
        return text == '/外島'

    def is_going_to_state6(self, update):
        mes=update.message
        text = mes.text
        return text== '/我的最愛'
       
    def is_going_to_state7(self, update):
        mes=update.message
        text = mes.text
        return text == '/推薦'

    def is_going_to_state8(self, update):
        mes=update.message
        text = mes.text
        return text == '/新北'
       
    def is_going_to_state9(self, update):
        mes=update.message
        text = mes.text
        return text == '/台北'

    def is_going_to_state10(self, update):
        mes=update.message   
        text = mes.text
        return text == '/桃園'
       
    def is_going_to_state11(self, update):
        mes=update.message   
        text = mes.text
        return text == '/新竹'

    def is_going_to_state12(self, update):
        mes=update.message   
        text = mes.text
        return text == '/苗栗'
       
    def is_going_to_state13(self, update):
        mes=update.message   
        text = mes.text
        return text == '/台中'

    def is_going_to_state14(self, update):
        mes=update.message   
        text = mes.text
        return text == '/彰化'
       
    def is_going_to_state15(self, update):
        mes=update.message   
        text = mes.text
        return text == '/南投'

    def is_going_to_state16(self, update):
        mes=update.message   
        text = mes.text
        return text == '/嘉義'

    def is_going_to_state17(self, update):
        mes=update.message   
        text = mes.text
        return text == '/台南'
       
    def is_going_to_state18(self, update):
        mes=update.message   
        text = mes.text
        return text == '/高雄'

    def is_going_to_state19(self, update):
        mes=update.message
        text = mes.text
        return text == '/屏東'
       
    def is_going_to_state20(self, update):
        mes=update.message   
        text = mes.text
        return text == '/台東'

    def is_going_to_state21(self, update):
        mes=update.message
        text = mes.text
        return text == '/花蓮'
       
    def is_going_to_state22(self, update):
        mes=update.message
        text = mes.text
        return text == '/宜蘭'

    def is_going_to_state23(self, update):
        mes=update.message
        text = mes.text
        return text == '/add'


    def on_enter_state1(self, update):
        update.message.reply_text("輸入縣市\n/新北\n/台北\n/桃園\n/新竹\n/苗栗\n")
        
    def on_exit_state1(self, update):
        print('Leaving state1')

    def on_enter_state2(self, update):
        update.message.reply_text("輸入縣市\n/台中\n/彰化\n/南投\n")        

    def on_exit_state2(self, update):
        print('Leaving state2')

    def on_enter_state3(self, update):
        update.message.reply_text("輸入縣市\n/嘉義\n/台南\n/高雄\n/屏東\n")
        
    def on_exit_state3(self, update):
        print('Leaving state3')

    def on_enter_state4(self, update):
        update.message.reply_text("輸入縣市\n/台東\n/花蓮\n/宜蘭\n")        

    def on_exit_state4(self, update):
        print('Leaving state4')

    def on_enter_state5(self, update):
        update.message.reply_text("綠島-樂達統祥大飯店http://www.tour365.tw/tour365tw/?p=439")
        
    def on_exit_state5(self, update):
        print('Leaving state5')

    def on_enter_state6(self, update):
        update.message.reply_text("我的最愛....")
        

    def on_exit_state6(self, update):
        print('Leaving state6')

    def on_enter_state7(self, update):
        update.message.reply_text("推薦行程...")
        u = random.randint(0,7)
        if u==0:
            self.photo=open('image/photo1.jpg','rb')
            update.message.reply_photo(self.photo)
        elif u==1:
            self.photo=open('image/photo2.jpg','rb')
            update.message.reply_photo(self.photo)
        elif u==2:
            self.photo=open('image/photo3.jpg','rb')
            update.message.reply_photo(self.photo)
        elif u==3:
            self.photo=open('image/photo4.jpg','rb')
            update.message.reply_photo(self.photo)
        elif u==4:
            self.photo=open('image/photo5.jpg','rb')
            update.message.reply_photo(self.photo)
        elif u==5:
            self.photo=open('image/photo6.jpg','rb')
            update.message.reply_photo(self.photo)
        elif u==6:
            self.photo=open('image/photo7.jpg','rb')
            update.message.reply_photo(self.photo)
        elif u==7:
            self.photo=open('image/photo8.jpg','rb')
            update.message.reply_photo(self.photo)
        
    def on_exit_state7(self, update):
        print('Leaving state7')

    def on_enter_state8(self, update):
        update.message.reply_text("新北土城-艾蔓精緻旅館【一般聯盟飯店】http://www.tour365.tw/tour365tw/?p=2334\n新北新店-矽谷溫泉會館http://www.tour365.tw/tour365tw/?p=6228\n新北新店-美麗春天大飯店http://www.tour365.tw/tour365tw/?p=2315\n新北淡水-亞太飯店http://www.tour365.tw/tour365tw/?p=2387\n新北萬里-翡翠灣福華渡假飯店http://www.tour365.tw/tour365tw/?p=2345\n新北金山-金山海灣溫泉會館http://www.tour365.tw/tour365tw/?p=2376\n輸入: /back 回到上一頁\n輸入: /add+想增加的訊息 加進我的最愛\n")        

    def on_exit_state8(self, update):
        print('Leaving state8')

    def on_enter_state9(self, update):
        update.message.reply_text("台北-北投熱海溫泉大飯店(2018無代理)http://www.tour365.tw/tour365tw/?p=24364\n台北松山-碧瑤飯店http://www.tour365.tw/tour365tw/?p=2418\n台北萬華-禾順商旅http://www.tour365.tw/tour365tw/?p=21047\n台北萬華-豪景大酒店【一般聯盟飯店】http://www.tour365.tw/tour365tw/?p=18276\n輸入: /back 回到上一頁\n輸入: /add+想增加的訊息 加進我的最愛\n")
        
    def on_exit_state9(self, update):
        print('Leaving state9')

    def on_enter_state10(self, update):
        update.message.reply_text("桃園中壢-中壢大飯店【一般聯盟飯店】http://www.tour365.tw/tour365tw/?p=2292\n桃園中壢-凱都大飯店http://www.tour365.tw/tour365tw/?p=2282\n桃園中壢-桃企大飯店http://www.tour365.tw/tour365tw/?p=2274\n桃園中壢-米堤大飯店http://www.tour365.tw/tour365tw/?p=9639\n桃園市-國道二號精品商旅http://www.tour365.tw/tour365tw/?p=17227\n桃園市-歐帝花園商務旅館http://www.tour365.tw/tour365tw/?p=22671\n桃園復興-景盛渡假山莊http://www.tour365.tw/tour365tw/?p=2242\n桃園楊梅-中華人才培訓中心【一般聯盟飯店】http://www.tour365.tw/tour365tw/?p=8966\n桃園楊梅-東森山林渡假飯店【一般聯盟飯店】http://www.tour365.tw/tour365tw/?p=9998\n桃園龍潭-石門水庫福華渡假飯店 http://www.tour365.tw/tour365tw/?p=2250\n輸入: /back 回到上一頁\n輸入: /add+想增加的訊息 加進我的最愛\n")        

    def on_exit_state10(self, update):
        print('Leaving state10')

    def on_enter_state11(self, update):
        update.message.reply_text("新竹市-卡爾登飯店-中華館http://www.tour365.tw/tour365tw/?p=8748\n新竹市-卡爾登飯店-北大館http://www.tour365.tw/tour365tw/?p=8732\n新竹市-福宏商務旅館http://www.tour365.tw/tour365tw/?p=2189\n新竹市-福泰商務飯店【一般聯盟飯店】http://www.tour365.tw/tour365tw/?p=2212\n新竹市-風信子生活旅店http://www.tour365.tw/tour365tw/?p=2203\n新竹東區-悅豪大飯店http://www.tour365.tw/tour365tw/?p=9816\n新竹竹北-悅豪大飯店 http://www.tour365.tw/tour365tw/?p=5796\n輸入: /back 回到上一頁\n輸入: /add+想增加的訊息 加進我的最愛\n")
        
    def on_exit_state11(self, update):
        print('Leaving state11')

    def on_enter_state12(self, update):
        update.message.reply_text("苗栗三義-櫻花渡假會館【一般聯盟飯店】http://www.tour365.tw/tour365tw/?p=16854\n苗栗頭份-尚順君樂飯店http://www.tour365.tw/tour365tw/?p=16914 \n輸入: /back 回到上一頁\n輸入: /add+想增加的訊息 加進我的最愛\n")        

    def on_exit_state12(self, update):
        print('Leaving state12')

    def on_enter_state13(self, update):
        update.message.reply_text("台中(逢甲夜市)-塔木德飯店原德館【一般聯盟飯店】http://www.tour365.tw/tour365tw/?p=2053\n台中(逢甲夜市)-碧根行館【一般聯盟飯店】http://www.tour365.tw/tour365tw/?p=6146\n台中中區-塔木德飯店中山館http://www.tour365.tw/tour365tw/?p=20177\n台中中區-星動銀河旅站【一般聯盟飯店】http://www.tour365.tw/tour365tw/?p=21908\n台中北區-塔木德飯店一中館http://www.tour365.tw/tour365tw/?p=2043\n台中北區-塔木德飯店公園館http://www.tour365.tw/tour365tw/?p=10990\n台中北屯-世聯商旅【一般聯盟飯店】http://www.tour365.tw/tour365tw/?p=16933\n台中北屯-橋王花園酒店【一般聯盟飯店】http://www.tour365.tw/tour365tw/?p=2101\n台中和平-龍谷觀光飯店http://www.tour365.tw/tour365tw/?p=8455\n台中大雅-威汀城市酒店【一般聯盟飯店】http://www.tour365.tw/tour365tw/?p=9573\n台中太平-賀緹酒店http://www.tour365.tw/tour365tw/?p=8412\n台中市-F商旅-台中麗加園邸http://www.tour365.tw/tour365tw/?p=2133\n台中市-富王大飯店http://www.tour365.tw/tour365tw/?p=2063\n台中東區-香富大飯店【一般聯盟飯店】http://www.tour365.tw/tour365tw/?p=18126\n台中豐原-新都大飯店【一般聯盟飯店】http://www.tour365.tw/tour365tw/?p=7144\n輸入: /back 回到上一頁\n輸入: /add+想增加的訊息 加進我的最愛\n ")
        
    def on_exit_state13(self, update):
        print('Leaving state13')

    def on_enter_state14(self, update):
        update.message.reply_text("彰化市-福泰商務飯店【一般聯盟飯店】http://www.tour365.tw/tour365tw/?p=1993\n彰化花壇-日華大飯店http://www.tour365.tw/tour365tw/?p=1961\n彰化鹿港-統一渡假村-鹿港文創會館 http://www.tour365.tw/tour365tw/?p=21529\n輸入: /back 回到上一頁\n輸入: /add+想增加的訊息 加進我的最愛\n")        

    def on_exit_state14(self, update):
        print('Leaving state14')

    def on_enter_state15(self, update):
        update.message.reply_text("南投-名人渡假村(2018無代理)http://www.tour365.tw/tour365tw/?p=244889\n南投信義-勝華溫泉飯店【一般聯盟飯店】http://www.tour365.tw/tour365tw/?p=7371\n南投信義-帝綸溫泉飯店http://www.tour365.tw/tour365tw/?p=22837\n南投國姓-北港溪沙八渡假村http://www.tour365.tw/tour365tw/?p=1883\n南投埔里-冠月精品旅館http://www.tour365.tw/tour365tw/?p=14142\n南投埔里-箱根溫泉生活館http://www.tour365.tw/tour365tw/?p=1842\n南投埔里-鎮寶大飯店http://www.tour365.tw/tour365tw/?p=1860\n南投日月潭-景聖樓飯店http://www.tour365.tw/tour365tw/?p=1809\n南投清境-依默騎馬渡假莊園http://www.tour365.tw/tour365tw/?p=21856\n南投清境-嶺仙花園渡假山莊http://www.tour365.tw/tour365tw/?p=1926\n南投清境-雲之瀑休閒景觀渡假村http://www.tour365.tw/tour365tw/?p=1911\n南投溪頭-夏緹飯店【一般聯盟飯店】http://www.tour365.tw/tour365tw/?p=1791\n南投溪頭-立德飯店南http://www.tour365.tw/tour365tw/?p=1776\n投竹山-大鞍清境民宿【一般聯盟飯店】http://www.tour365.tw/tour365tw/?p=21196\n南投草屯-寶旺萊6號花園酒店http://www.tour365.tw/tour365tw/?p=8599 \n輸入: /back 回到上一頁\n輸入: /add+想增加的訊息 加進我的最愛\n")        

    def on_exit_state15(self, update):
        print('Leaving state15')

    def on_enter_state16(self, update):
        update.message.reply_text("嘉義太保-佳仕堡商務飯店【一般聯盟飯店】http://www.tour365.tw/tour365tw/?p=18374\n嘉義市-王子去旅行http://www.tour365.tw/tour365tw/?p=1684\n嘉義市-金龍海悅大飯店http://www.tour365.tw/tour365tw/?p=16725\n嘉義市-香湖國際大飯店http://www.tour365.tw/tour365tw/?p=1708\n嘉義東區-鈺通大飯店http://www.tour365.tw/tour365tw/?p=1731\n嘉義番路-F HOTELhttp://www.tour365.tw/tour365tw/?p=10947\n嘉義館嘉義西區-冠閣商務大飯店http://www.tour365.tw/tour365tw/?p=1743\n嘉義西區-嘉禾玉山國際大飯店http://www.tour365.tw/tour365tw/?p=1718\n嘉義西區-夏禾國際行館http://www.tour365.tw/tour365tw/?p=21737\n嘉義西區-德爾芙快捷酒店(原永琦商旅)【一般聯盟飯店】http://www.tour365.tw/tour365tw/?p=23582\n嘉義西區-皇品國際酒店http://www.tour365.tw/tour365tw/?p=1756\n嘉義西區-福泰桔子商旅-嘉義店【一般聯盟飯店】http://www.tour365.tw/tour365tw/?p=19254\n嘉義西區-蘭桂坊花園酒店http://www.tour365.tw/tour365tw/?p=21873\n輸入: /back 回到上一頁\n輸入: /add+想增加的訊息 加進我的最愛\n")
        
    def on_exit_state16(self, update):
        print('Leaving state16')

    def on_enter_state17(self, update):
        update.message.reply_text("台南中西區-HOTEL COZZI和逸台南西門館http://www.tour365.tw/tour365tw/?p=20728\n台南中西區-碳佐麻里(捷喬)商務旅館http://www.tour365.tw/tour365tw/?p=23028\n台南中西區-郡象商旅http://www.tour365.tw/tour365tw/?p=19204\n台南北區-富信大飯店http://www.tour365.tw/tour365tw/?p=23126\n台南南區-揚悅精緻大飯店【一般聯盟飯店】http://www.tour365.tw/tour365tw/?p=23107\n台南善化-南科贊美酒店(原南科商旅)http://www.tour365.tw/tour365tw/?p=1415\n台南大內-走馬瀨農場http://www.tour365.tw/tour365tw/?p=1484\n台南市-F HOTEL 台南館http://www.tour365.tw/tour365tw/?p=1642\n台南市-劍橋連鎖飯店－台南館http://www.tour365.tw/tour365tw/?p=1619\n台南市-塔木德飯店台南會館http://www.tour365.tw/tour365tw/?p=1578\n台南市-家新大飯店http://www.tour365.tw/tour365tw/?p=1667\n台南市-愛客發商務旅館-台南館http://www.tour365.tw/tour365tw/?p=1591\n台南市-星象商旅http://www.tour365.tw/tour365tw/?p=1632\n台南市-林肯飯店http://www.tour365.tw/tour365tw/?p=1603\n台南新市-迎嘉花園酒店【一般聯盟飯店】http://www.tour365.tw/tour365tw/?p=1552\n台南新營-世洋商務會館http://www.tour365.tw/tour365tw/?p=1525\n台南新營-歐堡商務汽車旅館http://www.tour365.tw/tour365tw/?p=1511\n台南柳營-尖山埤江南渡假村【一般聯盟飯店】http://www.tour365.tw/tour365tw/?p=1452\n台南永康-台南桂田酒店http://www.tour365.tw/tour365tw/?p=23634\n台南烏山頭-湖境渡假會館http://www.tour365.tw/tour365tw/?p=1427\n台南關子嶺-湯泉美地溫泉會館【一般聯盟飯店】http://www.tour365.tw/tour365tw/?p=5860\n輸入: /back 回到上一頁\n輸入: /add+想增加的訊息 加進我的最愛\n")        

    def on_exit_state17(self, update):
        print('Leaving state17')

    def on_enter_state18(self, update):
        update.message.reply_text("高雄-悠然山莊(2018無代理)http://www.tour365.tw/tour365tw/?p=24573\n高雄-皇家尊龍大酒店(2018無代理)http://www.tour365.tw/tour365tw/?p=24567\n高雄-龍華旅館(2018無代理)http://www.tour365.tw/tour365tw/?p=24571\n高雄三民區-京城大飯店http://www.tour365.tw/tour365tw/?p=22204\n高雄三民區-希望殿堂 精緻商旅【一般聯盟飯店】http://www.tour365.tw/tour365tw/?p=18099\n高雄三民區-旅行家商旅【一般聯盟飯店】http://www.tour365.tw/tour365tw/?p=1132\n高雄前金區-WO HOTEL・窩飯店【一般聯盟飯店】http://www.tour365.tw/tour365tw/?p=9836\n高雄前金區-南海商務飯店http://www.tour365.tw/tour365tw/?p=1159\n高雄前金區-國賓大飯店http://www.tour365.tw/tour365tw/?p=10446\n高雄前金區-華園飯店http://www.tour365.tw/tour365tw/?p=1310\n高雄前鎮區-HOTEL COZZI和逸高雄中山館http://www.tour365.tw/tour365tw/?p=20709\n高雄小港區-高雄國際會館【一般聯盟飯店】http://www.tour365.tw/tour365tw/?p=21437\n高雄左營區-蓮潭國際會館http://www.tour365.tw/tour365tw/?p=21423\n高雄新興區-大通大飯店http://www.tour365.tw/tour365tw/?p=1100\n高雄新興區-福泰桔子商旅-六合店【一般聯盟飯店】http://www.tour365.tw/tour365tw/?p=18336\n高雄新興區-高雄商旅http://www.tour365.tw/tour365tw/?p=1300\n高雄新興區-麗尊酒店http://www.tour365.tw/tour365tw/?p=10098\n高雄新興區-麗景酒店http://www.tour365.tw/tour365tw/?p=10114\n高雄旗津區-旗津道沙灘酒店http://www.tour365.tw/tour365tw/?p=24443\n高雄苓雅區-君鴻國際酒店http://www.tour365.tw/tour365tw/?p=1355\n高雄苓雅區-寒軒國際大飯店http://www.tour365.tw/tour365tw/?p=1378\n高雄苓雅區-昭來商務旅館http://www.tour365.tw/tour365tw/?p=10519\n高雄鹽埕區-F HOTEL 愛河館http://www.tour365.tw/tour365tw/?p=1344\n高雄鹽埕區-華王大飯店http://www.tour365.tw/tour365tw/?p=4690\n高雄鹽埕區-香富大飯店【一般聯盟飯店】http://www.tour365.tw/tour365tw/?p=20442\n高雄鹽埕區-高雄福容大飯店【一般聯盟飯店】http://www.tour365.tw/tour365tw/?p=24186\n高雄鼓山區-帕可麗酒店http://www.tour365.tw/tour365tw/?p=24583\n輸入: /back 回到上一頁\n輸入: /add+想增加的訊息 加進我的最愛\n ")
        
    def on_exit_state18(self, update):
        print('Leaving state18')

    def on_enter_state19(self, update):
        update.message.reply_text("屏東九如-愛的時尚休閒旅店http://www.tour365.tw/tour365tw/?p=1065\n屏東墾丁-福容大飯店http://www.tour365.tw/tour365tw/?p=20433\n屏東市-鮪魚家族飯店-屏東館(櫻花蝦金品大飯店)http://www.tour365.tw/tour365tw/?p=15461\n屏東恆春-墾丁假期渡假飯店http://www.tour365.tw/tour365tw/?p=1027\n屏東恆春-墾丁菈蜜亞渡假旅店http://www.tour365.tw/tour365tw/?p=996\n屏東恆春-小丑魚度假村http://www.tour365.tw/tour365tw/?p=1007\n屏東恆春-日月光飯店-墾丁店http://www.tour365.tw/tour365tw/?p=15382\n屏東林邊-愛之旅汽車旅館【一般聯盟飯店】http://www.tour365.tw/tour365tw/?p=21706\n屏東滿州-小墾丁渡假村http://www.tour365.tw/tour365tw/?p=22525\n屏東高樹-大路觀樂園酒店http://www.tour365.tw/tour365tw/?p=1077 \n輸入: /back 回到上一頁\n輸入: /add+想增加的訊息 加進我的最愛\n")        

    def on_exit_state19(self, update):
        print('Leaving state19')


    def on_enter_state20(self, update):
        update.message.reply_text("台東-大波池渡假會館(2018無代理)http://www.tour365.tw/tour365tw/?p=24593\n台東南橫-天龍溫泉飯店http://www.tour365.tw/tour365tw/?p=819\n台東太麻里-曙光渡假酒店【一般聯盟飯店】http://www.tour365.tw/tour365tw/?p=23606\n台東市-THE GAYA HOTELhttp://www.tour365.tw/tour365tw/?p=22935\n台東市-三博大飯店【一般聯盟飯店】http://www.tour365.tw/tour365tw/?p=905\n台東市-台東桂田喜來登酒店【一般聯盟飯店】http://www.tour365.tw/tour365tw/?p=7079\n台東市-娜路彎大酒店【一般聯盟飯店】http://www.tour365.tw/tour365tw/?p=915\n台東市-娜路彎花園酒店http://www.tour365.tw/tour365tw/?p=18302\n台東市-娜路彎銀河酒店http://www.tour365.tw/tour365tw/?p=21493\n台東市-旅人驛站-鐵花文創館http://www.tour365.tw/tour365tw/?p=23569\n台東市-鮪魚家族飯店-台東館(旗魚金典商務大飯店)http://www.tour365.tw/tour365tw/?p=8865\n台東成功-東海岸海景渡假飯店http://www.tour365.tw/tour365tw/?p=841\n台東知本-F HOTEL 知本館6169\n台東知本-亞灣溫泉飯店http://www.tour365.tw/tour365tw/?p=871\n台東知本-泓泉溫泉渡假村http://www.tour365.tw/tour365tw/?p=882\n台東知本-知本金聯世紀酒店【一般聯盟飯店】http://www.tour365.tw/tour365tw/?p=892 \n輸入: /back 回到上一頁\n輸入: /add+想增加的訊息 加進我的最愛\n")        

    def on_exit_state20(self, update):
        print('Leaving state20')

    def on_enter_state21(self, update):
        update.message.reply_text("花蓮-星晟棧渡假飯店(2018無代理)http://www.tour365.tw/tour365tw/?p=24613\n花蓮壽豐-理想大地渡假飯店【一般聯盟飯店】http://www.tour365.tw/tour365tw/?p=672\n花蓮壽豐-花蓮遠雄悅來大飯店【一般聯盟飯店】http://www.tour365.tw/tour365tw/?p=15352\n花蓮市-F HOTEL 花蓮館http://www.tour365.tw/tour365tw/?p=727\n花蓮市-亞士都飯店http://www.tour365.tw/tour365tw/?p=712\n花蓮市-奇萊大飯店http://www.tour365.tw/tour365tw/?p=684\n花蓮市-東岸精緻商務旅館http://www.tour365.tw/tour365tw/?p=752\n花蓮市-百事達國際飯店http://www.tour365.tw/tour365tw/?p=776\n花蓮市-福隆大飯店http://www.tour365.tw/tour365tw/?p=738\n花蓮市-經典假日飯店http://www.tour365.tw/tour365tw/?p=793\n花蓮市-鮪魚家族飯店-花蓮館(曼波魚四季大飯店)http://www.tour365.tw/tour365tw/?p=8830\n花蓮市-麗格休閒飯店【一般聯盟飯店】http://www.tour365.tw/tour365tw/?p=19473\n花蓮市-麗軒國際飯店【一般聯盟飯店】http://www.tour365.tw/tour365tw/?p=19486\n輸入: /back 回到上一頁\n輸入: /add+想增加的訊息 加進我的最愛\n ")
        
    def on_exit_state21(self, update):
        print('Leaving state21')

    def on_enter_state22(self, update):
        update.message.reply_text("宜蘭-國城大飯店(2018無代理)http://www.tour365.tw/tour365tw/?p=21617\n宜蘭-大嵌城罋缸雞_新南民宿(2018無代理)http://www.tour365.tw/tour365tw/?p=21621\n宜蘭五結-蘭陽橋休閒渡假民宿http://www.tour365.tw/tour365tw/?p=5655\n宜蘭市-友愛大飯店http://www.tour365.tw/tour365tw/?p=552\n宜蘭礁溪-山泉大飯店【一般聯盟飯店】http://www.tour365.tw/tour365tw/?p=604\n宜蘭礁溪-日月光國際大飯店-礁溪館【一般聯盟飯店】http://www.tour365.tw/tour365tw/?p=12543\n宜蘭礁溪-鳳凰德陽川泉旅http://www.tour365.tw/tour365tw/?p=616\n宜蘭羅東-同榮大飯店http://www.tour365.tw/tour365tw/?p=514\n宜蘭羅東-樂亞香草藝術旅店【一般聯盟飯店】http://www.tour365.tw/tour365tw/?p=18608 \n輸入: /back 回到上一頁\n輸入: /add+想增加的訊息 加進我的最愛\n")
        
    def on_exit_state22(self, update):
        print('Leaving state22')

    def on_enter_state23(self, update):
        update.message.reply_text("i'm entering state23")
        
    def on_exit_state23(self, update):
        print('Leaving state22')
