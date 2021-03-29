# -*- coding: utf-8 -*-
import urllib,urllib2,re,xbmcplugin,xbmcgui,os,sys,datetime
from resources.lib.common_variables import *
from resources.lib.directory import *
from resources.lib.youtubewrapper import *
from resources.lib.watched import * 

fanart = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.Serviceil', 'fanart.jpg'))
art = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.Serviceil/resources/img', ''))

def CATEGORIES():
        addDir('[B][COLOR aqua]  •[/COLOR][/B][B][COLOR white]ת [/COLOR][/B][B][COLOR aqua]ו [/COLOR][/B][B][COLOR white]ר [/COLOR][/B][B][COLOR aqua]י [/COLOR][/B][B][COLOR white]ש [/COLOR][/B][B][COLOR aqua] •[/COLOR][/B]','url',194,art + 'Serviceil.png')

        addDir('[COLOR aqua]ערוצים בקליק [/COLOR]','url',7777776,'https://cdn.imgbin.com/5/7/10/imgbin-adam-sandler-click-film-poster-michael-newman-adam-sandler-6D9Ka94946DkP4diMLBF2CkPH.jpg')
        addDir('[COLOR aqua]סרטים בקליק [/COLOR]','url',7777777,'https://cdn.imgbin.com/5/7/10/imgbin-adam-sandler-click-film-poster-michael-newman-adam-sandler-6D9Ka94946DkP4diMLBF2CkPH.jpg')
        addDir('[COLOR aqua]הכול דרך יוטיוב (המקורי) [/COLOR]','url',987652002122,art + 'youtube.png')
        addDir('[COLOR aqua]אינדקס [/COLOR]','url',8134256789,'https://iconfair.com/wp-content/uploads/2020/10/Artboard-10-7.png')



def index():
        addDir('[COLOR aqua]סרטים [/COLOR]','url',18134256789,'http://ngarba.xyz/adds/yos/15.jpg')
        addDir('[COLOR aqua]סדרות [/COLOR]','url',28134256789,'http://ngarba.xyz/adds/yos/19.jpg')
        addDir('[COLOR aqua]ילדים [/COLOR]','url',38134256789,'http://ngarba.xyz/adds/yos/13.jpg')

def index1():
        addDir3('[COLOR aqua]1080P [/COLOR]',"http://www.dhakamovie.com/server1/Movies/1080p%20HD/Hollywood/",35,'http://ngarba.xyz/adds/yos/15.jpg')
        addDir3('[COLOR aqua]MOVIES TOP-250-IMDB [/COLOR]',"http://www.dhakamovie.com/server1/Movies/Top-250-IMDB/",35,'http://ngarba.xyz/adds/yos/15.jpg')
        addDir3('[COLOR aqua]MOVIES 2020 [/COLOR]',"http://www.dhakamovie.com/server1/Movies/Hollywood/2020/",35,'http://ngarba.xyz/adds/yos/15.jpg')
        addDir3('[COLOR aqua]MOVIES 2019 [/COLOR]',"http://www.dhakamovie.com/server1/Movies/Hollywood/2019/",35,'http://ngarba.xyz/adds/yos/15.jpg')
        addDir3('[COLOR aqua]MOVIES 2018 [/COLOR]',"http://www.dhakamovie.com/server1/Movies/Hollywood/2018/",35,'http://ngarba.xyz/adds/yos/15.jpg')
        addDir3('[COLOR aqua]MOVIES 2017 [/COLOR]',"http://www.dhakamovie.com/server1/Movies/Hollywood/2017/",35,'http://ngarba.xyz/adds/yos/15.jpg')
        addDir3('[COLOR aqua]MOVIES 2015-2016 [/COLOR]',"http://www.dhakamovie.com/server1/Movies/Hollywood/2015_2016/",35,'http://ngarba.xyz/adds/yos/15.jpg')
        addDir3('[COLOR aqua]MOVIES 2013-2014 [/COLOR]',"http://www.dhakamovie.com/server1/Movies/Hollywood/2013_2014/",35,'http://ngarba.xyz/adds/yos/15.jpg')
        addDir3('[COLOR aqua]MOVIES 2011-2012 [/COLOR]',"http://www.dhakamovie.com/server1/Movies/Hollywood/2011-2012/",35,'http://ngarba.xyz/adds/yos/15.jpg')
        addDir3('[COLOR aqua]MOVIES 2009-2010 [/COLOR]',"http://www.dhakamovie.com/server1/Movies/Hollywood/2009_2010/",35,'http://ngarba.xyz/adds/yos/15.jpg')
        addDir3('[COLOR aqua]MOVIES 2006-2008 [/COLOR]',"http://www.dhakamovie.com/server1/Movies/Hollywood/2006_2008/",35,'http://ngarba.xyz/adds/yos/15.jpg')
        addDir3('[COLOR aqua]MOVIES 2000-2005 [/COLOR]',"http://www.dhakamovie.com/server1/Movies/Hollywood/2000_2005/",35,'http://ngarba.xyz/adds/yos/15.jpg')
        addDir3('[COLOR aqua]MOVIES 1957-1999 [/COLOR]',"http://www.dhakamovie.com/server1/Movies/Hollywood/1957_1999/",35,'http://ngarba.xyz/adds/yos/15.jpg')
        addDir3('[COLOR aqua]MOVIES BY YEAR [/COLOR]',"http://103.133.135.242/Data/movies/hollywood/ ",35,'http://ngarba.xyz/adds/yos/15.jpg')
        addDir3('[COLOR aqua]WORLD MOVIES [/COLOR]',"http://103.133.135.242/Data/movies/World%20Movie/ ",35,'http://ngarba.xyz/adds/yos/15.jpg')
        addDir3('[COLOR aqua]ITALIAN MOVIES [/COLOR]',"http://103.133.135.242/Data/movies/Italian%20Movie/ ",35,'http://ngarba.xyz/adds/yos/15.jpg')
        addDir3('[COLOR aqua]BOLLYWOOD MOVIES BY YEAR [/COLOR]',"http://www.dhakamovie.com/server1/Movies/Bollywood/",35,'http://ngarba.xyz/adds/yos/15.jpg')
        addDir3('[COLOR aqua]CHINESE MOVIES BY YEAR [/COLOR]',"http://www.dhakamovie.com/server1/Movies/Chinese/",35,'http://ngarba.xyz/adds/yos/15.jpg')
        addDir3('[COLOR aqua]INDIAN MOVIES BY YEAR [/COLOR]',"http://www.dhakamovie.com/server1/Movies/Indian_Bangla/",35,'http://ngarba.xyz/adds/yos/15.jpg')
        addDir3('[COLOR aqua]TAMIL MOVIES BY YEAR [/COLOR]',"http://www.dhakamovie.com/server1/Movies/Tamil/",35,'http://ngarba.xyz/adds/yos/15.jpg')
        addDir3('[COLOR aqua]KOREAN MOVIES BY YEAR [/COLOR]',"http://www.dhakamovie.com/server1/Movies/Korean/",35,'http://ngarba.xyz/adds/yos/15.jpg')
        addDir3('[COLOR aqua]JAPANESE MOVIES BY YEAR [/COLOR]',"http://www.dhakamovie.com/server1/Movies/Japanese/",35,'http://ngarba.xyz/adds/yos/15.jpg')
        addDir3('[COLOR aqua]SOUTH INDIAN MOVIES BY YEAR [/COLOR]',"http://www.dhakamovie.com/server1/Movies/South_Indian/",35,'http://ngarba.xyz/adds/yos/15.jpg')
        addDir3('[COLOR aqua]HINDI DUBBED MOVIES BY YEAR [/COLOR]',"http://103.133.135.242/Data/movies/Hindi%20Dubbed/",35,'http://ngarba.xyz/adds/yos/15.jpg')


def index2():
        addDir3('[COLOR aqua]English TV-1 [/COLOR]',"http://103.133.135.242/Data/TV%20SERIES/",35,'http://ngarba.xyz/adds/yos/19.jpg')
        addDir3('[COLOR aqua]English TV-2 [/COLOR]',"http://www.dhakamovie.com/server1/TV_Series/English%20TV%20Shows/",35,'http://ngarba.xyz/adds/yos/19.jpg')
        addDir3('[COLOR aqua]Series_2020 [/COLOR]',"http://www.dhakamovie.com/server1/TV_Series/Tv_Series_2020/",35,'http://ngarba.xyz/adds/yos/19.jpg')
        addDir3('[COLOR aqua]ASIAN TV SHOWS-1(Bengal) [/COLOR]',"http://www.dhakamovie.com/server1/TV_Series/Bengali%20Tv%20Shows/",35,'http://ngarba.xyz/adds/yos/19.jpg')
        addDir3('[COLOR aqua]ASIAN TV SHOWS-2(Hindi) [/COLOR]',"http://www.dhakamovie.com/server1/TV_Series/Hindi%20TV%20Shows/",35,'http://ngarba.xyz/adds/yos/19.jpg')
        addDir3('[COLOR aqua]ASIAN TV SHOWS-3(Korean) [/COLOR]',"http://www.dhakamovie.com/server1/TV_Series/Korean/",35,'http://ngarba.xyz/adds/yos/19.jpg')






def index3():
        addDir3('[COLOR aqua]1CLICK KIDS 1080P [/COLOR]',"http://www.dhakamovie.com/server1/Movies/1080p%20HD/Animation/",35,'http://ngarba.xyz/adds/yos/13.jpg')
        addDir3('[COLOR aqua]1CLICK KIDS BY YEAR [/COLOR]',"http://103.133.135.242/Data/movies/ANIMATION/",35,'http://ngarba.xyz/adds/yos/13.jpg')
        addDir3('[COLOR aqua]1CLICK KIDS BY YEAR-2 [/COLOR]',"http://www.dhakamovie.com/server1/Movies/Animation/",35,'http://ngarba.xyz/adds/yos/13.jpg')

        addDir3('[COLOR aqua]דרגון מנדו [/COLOR]',"plugin://plugin.video.mando/?all_w=%7b%7d&data=%20&dates=%20&description=Master&eng_name=%20&episode=%20&fanart=http%3a%2f%2fngarba.xyz%2fadds%2fyos%2fa1a40.jpg&fav_status=false&heb_name=%20&iconimage=http%3a%2f%2fngarba.xyz%2fadds%2fyos%2fa1a41.jpg&id=%20&image_master&isr=0&last_id&mode=193&name=%5bB%5d%5bCOLORred%5dDragonFRD%5b%2fCOLOR%5d%5b%2fB%5d&original_title=%20&search_db&season=%20&show_original_year=%20&tmdbid=%20&url=https%3A%2F%2Fgithub.com%2Fdvidnikk%2Fnkk%2Fblob%2Fmain%2FAA.txt%3Fraw%3Dtrue&video_data=%7b%22rating%22%3a%20%220%22%2c%20%22episode%22%3a%200%2c%20%22title%22%3a%20%22%5bB%5d%5bCOLORred%5dDragonFRD%5b%2fCOLOR%5d%5b%2fB%5d%22%2c%20%22season%22%3a%200%2c%20%22TVshowtitle%22%3a%20%22%22%2c%20%22mediatype%22%3a%20%22movie%22%2c%20%22plot%22%3a%20%22Master%22%2c%20%22OriginalTitle%22%3a%20%22%20%22%2c%20%22Tag%22%3a%20%22None%22%2c%20%22id%22%3a%20%22%20%22%7d",35,'http://ngarba.xyz/adds/yos/13.jpg')

        addDir3('[COLOR aqua]חתול מנדו [/COLOR]',"plugin://plugin.video.mando/?all_w=%7b%7d&data=%20&dates=%20&description=Master&eng_name=%20&episode=%20&fanart=https://wallpaperaccess.com/full/1791505.png&fav_status=false&heb_name=%20&iconimage=https://freepikpsd.com/wp-content/uploads/2019/10/flash-tv-logo-png-1.png&id=%20&image_master&isr=0&last_id&mode=193&name=%FlashTV&original_title=%20&search_db&season=%20&show_original_year=%20&tmdbid=%20&url=https://kcat123.github.io/FTV/Public/FlashTV.txt&video_data=%7b%22rating%22%3a%20%220%22%2c%20%22episode%22%3a%200%2c%20%22title%22%3a%20%22%FlashTV%22%2c%20%22season%22%3a%200%2c%20%22TVshowtitle%22%3a%20%22%22%2c%20%22mediatype%22%3a%20%22movie%22%2c%20%22plot%22%3a%20%22Master%22%2c%20%22OriginalTitle%22%3a%20%22%20%22%2c%20%22Tag%22%3a%20%22None%22%2c%20%22id%22%3a%20%22%20%22%7d",35,'http://ngarba.xyz/adds/yos/13.jpg')

        addDir3('[COLOR aqua]ציקו מנדו [/COLOR]',"plugin://plugin.video.mando/?all_w=%7b%7d&data=%20&dates=%20&description=Master&eng_name=%20&episode=%20&fanart=https://wallpaperaccess.com/full/1791505.png&fav_status=false&heb_name=%20&iconimage=https://freepikpsd.com/wp-content/uploads/2019/10/flash-tv-logo-png-1.png&id=%20&image_master&isr=0&last_id&mode=193&name=%CHICCO&original_title=%20&search_db&season=%20&show_original_year=%20&tmdbid=%20&url=https://github.com/moris0371/CHICCO/raw/master/moris.txt&video_data=%7b%22rating%22%3a%20%220%22%2c%20%22episode%22%3a%200%2c%20%22title%22%3a%20%22%CHICCO%22%2c%20%22season%22%3a%200%2c%20%22TVshowtitle%22%3a%20%22%22%2c%20%22mediatype%22%3a%20%22movie%22%2c%20%22plot%22%3a%20%22Master%22%2c%20%22OriginalTitle%22%3a%20%22%20%22%2c%20%22Tag%22%3a%20%22None%22%2c%20%22id%22%3a%20%22%20%22%7d",35,'http://ngarba.xyz/adds/yos/13.jpg')

        addDir3('[COLOR aqua]סרוויס-מנדו [/COLOR]',"plugin://plugin.video.mando/?description=&mode=191&url=https://github.com/yonni55555/AB/raw/main/7000-1.txt",35,'http://ngarba.xyz/adds/yos/13.jpg')











 











def srbc():
        addDir3('[COLOR aqua]'+translate(70000003)+'[/COLOR]',"plugin://plugin.video.live.streamspro/?fanart=https%3a%2f%2fi.imgur.com%2fcaTYLyO.jpg&mode=1&name=%5bCOLOR%20blue%5d%5bCOLOR%20deepskyblue%5d%20MOVIE%20TempTV%5b%2fCOLOR%5d&url=https%3a%2f%2fpastebin.com%2fraw%2fyzK4xCtE",35,'https://cdn.imgbin.com/5/7/10/imgbin-adam-sandler-click-film-poster-michael-newman-adam-sandler-6D9Ka94946DkP4diMLBF2CkPH.jpg')
 

def srbc2():
        addDir3('[COLOR aqua]'+translate(70000004)+'[/COLOR]',"plugin://plugin.video.live.streamspro/?url=https%3a%2f%2fpastebin.com%2fraw%2fQYKCtZqs&mode=1",35,'https://cdn.imgbin.com/5/7/10/imgbin-adam-sandler-click-film-poster-michael-newman-adam-sandler-6D9Ka94946DkP4diMLBF2CkPH.jpg')

def Bildglllll():
        addDir('[COLOR aqua]סרטים [/COLOR]','url',1929192910091,'http://ngarba.xyz/adds/yos/15.jpg')
        addDir('[COLOR aqua]סדרות [/COLOR]','url',1929192910092,'http://ngarba.xyz/adds/yos/19.jpg')
        addDir('[COLOR aqua]ילדים [/COLOR]','url',1929192910093,'http://ngarba.xyz/adds/yos/13.jpg')
        addDir('[COLOR aqua]טלויזיה [/COLOR]','url',1929192910094,'http://ngarba.xyz/adds/yos/3.jpg')
        addDir('[COLOR aqua]מוזיקה [/COLOR]','url',1929192910095,'http://ngarba.xyz/adds/yos/12.jpg')
        addDir('[COLOR aqua]ספורט [/COLOR]','url',1929192910096,'http://ngarba.xyz/adds/yos/17.jpg')
        addDir3('[COLOR aqua]המעודפים שלי [/COLOR]',"plugin://script.skin.helper.widgets/?action=favourites&mediatype",35,'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTGifA4RM62yA5Gd5puJd5hYEKNToughMg75mNFuFpm-CfaR_cL')


        addDir('[B][COLOR aqua]תחזוקה [/COLOR][/B]','url',20008,'https://p7.hiclipart.com/preview/175/230/518/plug-in-computer-icons-add-on-wordpress-kodi-wordpress.jpg')

        addDir3('[B][COLOR red]כבוי לקודי [/COLOR][/B]',"plugin://plugin.close.kodi/?description&fanart=i\addons\plugin.close.kodi\fanart.jpg&iconimage=\addons\plugin.close.kodi\resources\art\force.png&mode=4&name=Insta Kill (Warning Kills The MediaCenter Instantly)&url=fclose",35,'https://www.ivid.it/blog/wp-content/uploads/2018/03/cropped-ivid-promo-512x512.jpg')



def Bildglllll1():
        addDir('[COLOR aqua]thecrew [/COLOR]','url',19291929177701,'http://ngarba.xyz/adds/yos/15.jpg')
        addDir('[COLOR aqua]mando [/COLOR]','url',19291929177702,'http://ngarba.xyz/adds/yos/15.jpg')
        addDir('[COLOR aqua]movixws [/COLOR]','url',19291929177703,'http://ngarba.xyz/adds/yos/15.jpg')
        addDir('[COLOR aqua]telemedia [/COLOR]','url',19291929177704,'http://ngarba.xyz/adds/yos/15.jpg')
        addDir('[COLOR aqua]Serviceil [/COLOR]','url',19291929177705,'http://ngarba.xyz/adds/yos/15.jpg')
        addDir('[COLOR aqua]CHICCO [/COLOR]','url',19291929177706,'http://ngarba.xyz/adds/yos/15.jpg')
        addDir('[COLOR aqua]FlashTV [/COLOR]','url',19291929177707,'http://ngarba.xyz/adds/yos/15.jpg')

def Bildglllll2():
        addDir('[COLOR aqua]עידן+ [/COLOR]','url',192919291777011,'http://ngarba.xyz/adds/yos/19.jpg')
        addDir('[COLOR aqua]סדרות-טיוי [/COLOR]','url',192919291777012,'http://ngarba.xyz/adds/yos/19.jpg')
        addDir('[COLOR aqua]thecrew [/COLOR]','url',192919291777013,'http://ngarba.xyz/adds/yos/19.jpg')
        addDir('[COLOR aqua]mando [/COLOR]','url',192919291777014,'http://ngarba.xyz/adds/yos/19.jpg')
        addDir('[COLOR aqua]telemedia [/COLOR]','url',192919291777016,'http://ngarba.xyz/adds/yos/19.jpg')
        addDir('[COLOR aqua]CHICCO [/COLOR]','url',192919291777017,'http://ngarba.xyz/adds/yos/19.jpg')
        addDir('[COLOR aqua]FlashTV [/COLOR]','url',192919291777018,'http://ngarba.xyz/adds/yos/19.jpg')

def Bildglllll3():
        addDir('[COLOR aqua]עידן+ [/COLOR]','url',292919291777011,'http://ngarba.xyz/adds/yos/13.jpg')
        addDir('[COLOR aqua]סדרות-טיוי [/COLOR]','url',1941948080,'http://ngarba.xyz/adds/yos/13.jpg')
        addDir('[COLOR aqua]Serviceil(יוטיוב) [/COLOR]','url',9876512,'http://ngarba.xyz/adds/yos/13.jpg')
        addDir('[COLOR aqua]thecrew [/COLOR]','url',292919291777013,'http://ngarba.xyz/adds/yos/13.jpg')
        addDir('[COLOR aqua]mando [/COLOR]','url',292919291777014,'http://ngarba.xyz/adds/yos/13.jpg')
        addDir('[COLOR aqua]telemedia [/COLOR]','url',292919291777015,'http://ngarba.xyz/adds/yos/13.jpg')
        addDir('[COLOR aqua]CHICCO [/COLOR]','url',292919291777016,'http://ngarba.xyz/adds/yos/13.jpg')
        addDir('[COLOR aqua]FlashTV [/COLOR]','url',292919291777017,'http://ngarba.xyz/adds/yos/13.jpg')

def Bildglllll4():
        addDir('[COLOR aqua]עידן+ [/COLOR]','url',392919291777017,'http://ngarba.xyz/adds/yos/3.jpg')
        addDir('[COLOR aqua]Serviceil [/COLOR]','url',392919291777018,'http://ngarba.xyz/adds/yos/3.jpg')
        addDir('[COLOR aqua]thecrew [/COLOR]','url',392919291777019,'http://ngarba.xyz/adds/yos/3.jpg')

def Bildglllll5():
        addDir('[COLOR aqua]Youtube Music [/COLOR]','url',492919291777011,'http://ngarba.xyz/adds/yos/12.jpg')
        addDir('[COLOR aqua]Serviceil [/COLOR]','url',492919291777012,'http://ngarba.xyz/adds/yos/12.jpg')
        addDir('[COLOR aqua]עידן+ [/COLOR]','url',492919291777013,'http://ngarba.xyz/adds/yos/12.jpg')


def Bildglllll6():
        addDir('[COLOR aqua]SportHD [/COLOR]','url',592919291777011,'http://ngarba.xyz/adds/yos/17.jpg')
        addDir('[COLOR aqua]thecrew [/COLOR]','url',592919291777012,'http://ngarba.xyz/adds/yos/17.jpg')
        addDir('[COLOR aqua]Serviceil [/COLOR]','url',592919291777013,'http://ngarba.xyz/adds/yos/17.jpg')
        addDir('[COLOR aqua]עידן+ [/COLOR]','url',592919291777014,'http://ngarba.xyz/adds/yos/17.jpg')





def Bthecrew1():
        addDir3('[COLOR aqua]סרטים כללי[/COLOR]',"plugin://plugin.video.thecrew/?action=movieNavigator&quot;",35,'http://ngarba.xyz/adds/yos/15.jpg')
        addDir3('[COLOR aqua]סרטים בקליק[/COLOR]',"plugin://plugin.video.thecrew/?action=directory&amp;content=0&amp;url=https%3a%2f%2fbitbucket.org%2fthrew%2fgreenhat%2fraw%2fmaster%2fgreenhat%2f1click%2fseries9%2ftest9.xml&quot;",35,'http://ngarba.xyz/adds/yos/15.jpg')
        addDir3('[COLOR aqua]חיפוש באנגלית[/COLOR]',"plugin://plugin.video.thecrew/?action=movieSearchnew;",35,'http://ngarba.xyz/adds/yos/15.jpg')

def Bmando2():
        addDir3('[COLOR aqua]סרטים כללי[/COLOR]',"plugin://plugin.video.mando/?all_w=%7b%7d&data=%20&dates=%20&description=Movies&eng_name=%20&episode=%20&fanart=https%3a%2f%2ftownsquare.media%2fsite%2f295%2ffiles%2f2019%2f12%2f2020-movies-collage.jpg%3fw%3d980%26q%3d75&fav_status=false&heb_name=%20&iconimage=C%3a%5cUsers%5cUser%5cAppData%5cRoaming%5cKodi%5caddons%5cplugin.video.mando%5cresources%5cartwork%2fmovies.png&id=%20&image_master&isr=0&last_id&mode=2&name=%d7%a1%d7%a8%d7%98%d7%99%d7%9d&original_title=%20&season=%20&show_original_year=%20&tmdbid=%20&url=www&video_data=%7b%22rating%22%3a%20%220%22%2c%20%22episode%22%3a%200%2c%20%22title%22%3a%20%22%5cu05e1%5cu05e8%5cu05d8%5cu05d9%5cu05dd%22%2c%20%22season%22%3a%200%2c%20%22TVshowtitle%22%3a%20%22%22%2c%20%22mediatype%22%3a%20%22movie%22%2c%20%22plot%22%3a%20%22Movies%22%2c%20%22OriginalTitle%22%3a%20%22%20%22%2c%20%22Tag%22%3a%20%22None%22%2c%20%22id%22%3a%20%22%20%22%7dt;",35,'http://ngarba.xyz/adds/yos/15.jpg')
        addDir3('[COLOR aqua]חיפוש [/COLOR]',"plugin://plugin.video.mando/?all_w=%7b%7d&data=%20&dates=%20&description=Tmdb&eng_name=%20&episode=%20&fanart=http%3a%2f%2fwww.videomotion.co.il%2fwp-content%2fuploads%2fwhatwedo-Pic-small.jpg&fav_status=false&heb_name=%20&iconimage=C%3a%5cUsers%5cUser%5cAppData%5cRoaming%5cKodi%5caddons%5cplugin.video.mando%5cresources%5cartwork%2fsearch_m.png&id=%20&image_master&isr=0&last_id&mode=14&name=%d7%97%d7%99%d7%a4%d7%95%d7%a9%20%d7%a1%d7%a8%d7%98&original_title=%20&season=%20&show_original_year=%20&tmdbid=%20&url=http%3a%2f%2fapi.themoviedb.org%2f3%2fsearch%2fmovie%3fapi_key%3d34142515d9d23817496eeb4ff1d223d0%26query%3d%25s%26language%3dhe%26append_to_response%3dorigin_country%26page%3d1&video_data=%7b%22rating%22%3a%20%220%22%2c%20%22episode%22%3a%200%2c%20%22title%22%3a%20%22%5cu05d7%5cu05d9%5cu05e4%5cu05d5%5cu05e9%20%5cu05e1%5cu05e8%5cu05d8%22%2c%20%22season%22%3a%200%2c%20%22TVshowtitle%22%3a%20%22%22%2c%20%22mediatype%22%3a%20%22movie%22%2c%20%22plot%22%3a%20%22Tmdb%22%2c%20%22OriginalTitle%22%3a%20%22%20%22%2c%20%22Tag%22%3a%20%222%22%2c%20%22id%22%3a%20%22%20%22%7d;",35,'http://ngarba.xyz/adds/yos/15.jpg')

def Bmovixws3():
        addDir3('[COLOR aqua]סרטים כללי[/COLOR]',"plugin://plugin.video.movixws/?description=%d7%a1%d7%a8%d7%98%d7%99%d7%9d&fanart=C%3a%5cUsers%5cUser%5cAppData%5cRoaming%5cKodi%5caddons%5cplugin.video.movixws%5cresources%5clogo%2fmovies.png&iconimage=C%3a%5cUsers%5cUser%5cAppData%5cRoaming%5cKodi%5caddons%5cplugin.video.movixws%5cresources%5clogo%2fmovies.png&mode=2&name=%d7%a1%d7%a8%d7%98%d7%99%d7%9d&url=https%3a%2f%2fmovix.live%2fmovies%2f;",35,'http://ngarba.xyz/adds/yos/15.jpg')
        addDir3('[COLOR aqua]קטגוריות[/COLOR]',"plugin://plugin.video.movixws/;",35,'http://ngarba.xyz/adds/yos/15.jpg')
        addDir3('[COLOR aqua]חיפוש[/COLOR]',"plugin://plugin.video.movixws/?description=%d7%97%d7%99%d7%a4%d7%95%d7%a9&fanart=C%3a%5cUsers%5cUser%5cAppData%5cRoaming%5cKodi%5caddons%5cplugin.video.movixws%5cresources%5clogo%2fsearch.png&iconimage=C%3a%5cUsers%5cUser%5cAppData%5cRoaming%5cKodi%5caddons%5cplugin.video.movixws%5cresources%5clogo%2fsearch.png&mode=5&name=%5bCOLOR%20aqua%5d%5bI%5d%d7%97%d7%99%d7%a4%d7%95%d7%a9%5b%2fI%5d%5b%2fCOLOR%5d&url=www;",35,'http://ngarba.xyz/adds/yos/15.jpg')


def Btelemedia4():
        addDir3('[COLOR aqua]סרטים כללי[/COLOR]',"plugin://plugin.video.telemedia/?data=%20&dates=%20&description=Movies&eng_name=%20&episode=%20&fanart=https%3a%2f%2fwww.ubackground.com%2f_ph%2f22%2f269562231.jpg&fav_status=false&groups_id=0&heb_name=%20&iconimage=special%3a%2f%2fhome%2faddons%2fplugin.video.telemedia%2ftele%2fmovies.png&id=%20&image_master&isr=0&last_id&mode=10&name=%5bCOLOR%20blue%5d%d7%a1%d7%a8%d7%98%d7%99%d7%9d%5b%2fCOLOR%5d&original_title=%20&season=%20&show_original_year=%20&tmdbid=%20&url=%20;",35,'http://ngarba.xyz/adds/yos/15.jpg')
        addDir3('[COLOR aqua]חיפוש[/COLOR]',"plugin://plugin.video.telemedia/?mode=14&name=חפש סרט&image_master=&heb_name= &last_id=&dates= &data= &original_title= &id= &season= &episode= &tmdbid= &eng_name= &show_original_year= &isr=0&fanart=http%3A%2F%2Fwww.videomotion.co.il%2Fwp-content%2Fuploads%2Fwhatwedo-Pic-small.jpg&url=http%3A%2F%2Fapi.themoviedb.org%2F3%2Fsearch%2Fmovie%3Fapi_key%3D34142515d9d23817496eeb4ff1d223d0%26query%3D%25s%26language%3Dhe%26append_to_response%3Dorigin_country%26page%3D1&iconimage=special%3A%2F%2Fhome%2Faddons%2Fplugin.video.telemedia%2Ftele%2FMovies%2Fmovie_search.png&description=Tmdb&fav_status=false&groups_id=0;",35,'http://ngarba.xyz/adds/yos/15.jpg')

def BServiceil5():
        addDir3('[COLOR aqua]'+translate(70000003)+'[/COLOR]',"plugin://plugin.video.live.streamspro/?fanart=https%3a%2f%2fi.imgur.com%2fcaTYLyO.jpg&mode=1&name=%5bCOLOR%20blue%5d%5bCOLOR%20deepskyblue%5d%20MOVIE%20TempTV%5b%2fCOLOR%5d&url=https%3a%2f%2fpastebin.com%2fraw%2fyzK4xCtE",35,'https://cdn.imgbin.com/5/7/10/imgbin-adam-sandler-click-film-poster-michael-newman-adam-sandler-6D9Ka94946DkP4diMLBF2CkPH.jpg')
        addDir('[COLOR aqua]סרטים(יוטיוב) [/COLOR]','url',9876538,'http://ngarba.xyz/adds/yos/15.jpg')

def BCHICCO6():
        addDir3('[COLOR aqua]סרטים כללי[/COLOR]',"plugin://plugin.video.CHICCO/?cat_level=%20&count=0&description=%20&fanart=https%3a%2f%2fimages.globes.co.il%2fimages%2fNewGlobes%2ffeeder%2f2015%2fe01_84-800.jpg&iconimage=https%3a%2f%2fimages.globes.co.il%2fimages%2fNewGlobes%2ffeeder%2f2015%2fe01_84-800.jpg&index_depth=0&lang=eng&mode=5&name=%d7%a1%d7%a8%d7%98%d7%99%d7%9d&page&selected_list=%20&url=%d7%a1%d7%a8%d7%98%d7%99%d7%9d",35,'http://ngarba.xyz/adds/yos/15.jpg')
        addDir3('[COLOR aqua]נוספו לאחרונה[/COLOR]',"plugin://plugin.video.CHICCO/?cat_level=%20&count=0&description&fanart=http%3a%2f%2fsf.co.ua%2f12%2f09%2fwallpaper-2230830.jpg&iconimage=http%3a%2f%2fngarba.xyz%2fadds%2fyos%2f16.jpg&index_depth=0&lang=%20&mode=18&name=%5bB%5d%5bCOLOR%20burlywood%5d-%d7%90%d7%97%d7%a8%d7%95%d7%a0%d7%99%d7%9d%20%5b%2fCOLOR%5d%5b%2fB%5d%5bB%5d%5bCOLOR%20aqua%5d%d7%a1%d7%a8%d7%98%d7%99%d7%9d-%20%5b%2fCOLOR%5d%5b%2fB%5d&page&selected_list=%20&url=movie",35,'http://ngarba.xyz/adds/yos/15.jpg')
        addDir3('[COLOR aqua]חיפוש[/COLOR]',"plugin://plugin.video.CHICCO/?cat_level=%20&count=0&description&fanart=http%3a%2f%2fb2acpa.com%2f%7ebairdcpa%2fimages%2fTerminator.jpg&iconimage=http%3a%2f%2fngarba.xyz%2fadds%2fyos%2f8.jpg&index_depth=0&lang=%20&mode=6&name=%5bB%5d%5bCOLOR%20burlywood%5d%d7%a4%d7%95%d7%a9%5b%2fCOLOR%5d%5b%2fB%5d%5bB%5d%5bCOLOR%20aqua%5d%d7%97%d7%99%5b%2fCOLOR%5d%5b%2fB%5d&page&selected_list=%20&url=movie;",35,'http://ngarba.xyz/adds/yos/15.jpg')

def BFlash7():
        addDir3('[COLOR aqua]סרטים כללי[/COLOR]',"plugin://plugin.video.FlashTV/?cat_level=%20&count=0&description=%20&fanart&iconimage=https%3a%2f%2fi.imgur.com%2f0diDf1j.jpg&index_depth=0&lang=eng&mode=5&name=%d7%a1%d7%a8%d7%98%d7%99%d7%9d&page&selected_list=%20&url=%d7%a1%d7%a8%d7%98%d7%99%d7%9d",35,'http://ngarba.xyz/adds/yos/15.jpg')
        addDir3('[COLOR aqua]נוספו לאחרונה[/COLOR]',"plugin://plugin.video.FlashTV/?cat_level= &count=0&description&mode=18&page&selected_list= &url=movie",35,'http://ngarba.xyz/adds/yos/15.jpg')
        addDir3('[COLOR aqua]חיפוש[/COLOR]',"plugin://plugin.video.FlashTV/?cat_level=%20&count=0&description&fanart=http%3a%2f%2fb2acpa.com%2f%7ebairdcpa%2fimages%2fTerminator.jpg&iconimage=http%3a%2f%2fngarba.xyz%2fadds%2fyos%2f8.jpg&index_depth=0&lang=%20&mode=6&name=%5bB%5d%5bCOLOR%20burlywood%5d%d7%a4%d7%95%d7%a9%5b%2fCOLOR%5d%5b%2fB%5d%5bB%5d%5bCOLOR%20aqua%5d%d7%97%d7%99%5b%2fCOLOR%5d%5b%2fB%5d&page&selected_list=%20&url=movie;",35,'http://ngarba.xyz/adds/yos/15.jpg')



def Cidanplus1():
        addDir3('[COLOR aqua]כאן-11[/COLOR]',"plugin://plugin.video.idanplus/?iconimage=C%253A%255CUsers%255CUser%255CAppData%255CRoaming%255CKodi%255Caddons%255Cplugin.video.idanplus%255Cresources%255Cimages%255Ckan.jpg&mode=1&module=kan&moredata=%25D7%259B%25D7%2590%25D7%259F%2b11&name=%5bB%5d%d7%9b%d7%9c%20%d7%94%d7%aa%d7%95%d7%9b%d7%a0%d7%99%d7%95%d7%aa%5b%2fB%5d&url=https%253A%252F%252Fwww.kan.org.il%252Fpage.aspx%253FlandingpageId%253D1039;",35,'http://ngarba.xyz/adds/yos/19.jpg')
        addDir3('[COLOR aqua]VOD-12[/COLOR]',"plugin://plugin.video.idanplus/?iconimage=C%253A%255CUsers%255CUser%255CAppData%255CRoaming%255CKodi%255Caddons%255Cplugin.video.idanplus%255Cresources%255Cimages%255Cvod.jpg&mode=1&module=keshet&moredata&name=%5bB%5d%d7%aa%d7%9b%d7%a0%d7%99%d7%95%d7%aa%20MakoTV%5b%2fB%5d&url=https%253A%252F%252Fwww.mako.co.il%252Fmako-vod-index;",35,'http://ngarba.xyz/adds/yos/19.jpg')
        addDir3('[COLOR aqua]VOD-13[/COLOR]',"plugin://plugin.video.idanplus/?iconimage=C%253A%255CUsers%255CUser%255CAppData%255CRoaming%255CKodi%255Caddons%255Cplugin.video.idanplus%255Cresources%255Cimages%255C13.png&mode=0&module=reshet&moredata&name=%5bB%5d%d7%9b%d7%9c%20%d7%94%d7%aa%d7%9b%d7%a0%d7%99%d7%95%d7%aa%5b%2fB%5d&url;",35,'http://ngarba.xyz/adds/yos/19.jpg')
        addDir3('[COLOR aqua]VOD-20[/COLOR]',"plugin://plugin.video.idanplus/?iconimage=C%253A%255CUsers%255CUser%255CAppData%255CRoaming%255CKodi%255Caddons%255Cplugin.video.idanplus%255Cresources%255Cimages%255C20.png&mode=0&module=twenty&moredata&name=%5bB%5d%d7%9b%d7%9c%20%d7%94%d7%aa%d7%9b%d7%a0%d7%99%d7%95%d7%aa%5b%2fB%5d&url;",35,'http://ngarba.xyz/adds/yos/19.jpg')
        addDir3('[COLOR aqua]VOD-23 חינוכית[/COLOR]',"plugin://plugin.video.idanplus/?iconimage=C%253A%255CUsers%255CUser%255CAppData%255CRoaming%255CKodi%255Caddons%255Cplugin.video.idanplus%255Cresources%255Cimages%255C23tv.jpg&mode=5&module=kan&moredata&name=%5bB%5d%d7%9b%d7%90%d7%9f%20%d7%97%d7%99%d7%a0%d7%95%d7%9b%d7%99%d7%aa%2023%5b%2fB%5d&url=https%253A%252F%252Fwww.kankids.org.il;",35,'http://ngarba.xyz/adds/yos/19.jpg')
        addDir3('[COLOR aqua]VOD-24-מוזיקה[/COLOR]',"plugin://plugin.video.idanplus/?iconimage=C%253A%255CUsers%255CUser%255CAppData%255CRoaming%255CKodi%255Caddons%255Cplugin.video.idanplus%255Cresources%255Cimages%255C24telad.png&mode=1&module=keshet&moredata&name=%5bB%5d%d7%a2%d7%a8%d7%95%d7%a5%2024%20%d7%94%d7%97%d7%93%d7%a9%5b%2fB%5d&url=http%253A%252F%252Fwww.mako.co.il%252Fmako-vod-music24;",35,'http://ngarba.xyz/adds/yos/19.jpg')
        addDir3('[COLOR aqua]VOD-9-רוסית[/COLOR]',"plugin://plugin.video.idanplus/?iconimage=C%253A%255CUsers%255CUser%255CAppData%255CRoaming%255CKodi%255Caddons%255Cplugin.video.idanplus%255Cresources%255Cimages%255C9tv.png&mode=0&module=9tv&moredata&name=%5bB%5d%d7%a2%d7%a8%d7%95%d7%a5%209%5b%2fB%5d&url;",35,'http://ngarba.xyz/adds/yos/19.jpg')
        addDir3('[COLOR aqua]חיפוש[/COLOR]',"plugin://plugin.video.idanplus/?iconimage=C%253A%255CUsers%255CUser%255CAppData%255CRoaming%255CKodi%255Caddons%255Cplugin.video.idanplus%255Cicon.png&mode=4&module&moredata&name=%5bB%5d%d7%97%d7%99%d7%a4%d7%95%d7%a9%20%d7%aa%d7%9b%d7%a0%d7%99%d7%95%d7%aa%5b%2fB%5d&url;",35,'http://ngarba.xyz/adds/yos/19.jpg')

def Csdarottv2():
        addDir3('[COLOR aqua]סדרות כללי[/COLOR]',"plugin://plugin.video.sdarot.tv/",35,'http://ngarba.xyz/adds/yos/19.jpg')
        addDir3('[COLOR aqua]חיפוש[/COLOR]',"plugin://plugin.video.sdarot.tv/search/0",35,'http://ngarba.xyz/adds/yos/19.jpg')


def Cthecrew3():
        addDir3('[COLOR aqua]סדרות כללי[/COLOR]',"plugin://plugin.video.thecrew/?action=tvNavigator;",35,'http://ngarba.xyz/adds/yos/19.jpg')
        addDir3('[COLOR aqua]סדרות בקליק[/COLOR]',"plugin://plugin.video.thecrew/?action=directory&content=addons&url=https%3a%2f%2fbitbucket.org%2fthrew%2fgreenhat%2fraw%2fmaster%2fgreenhat%2f1click%2fseries9%2ftvshows9.xml;",35,'http://ngarba.xyz/adds/yos/19.jpg')
        addDir3('[COLOR aqua]חיפוש באנגלית[/COLOR]',"plugin://plugin.video.thecrew/?action=tvSearchnew;",35,'http://ngarba.xyz/adds/yos/19.jpg')

def Cmando4():
        addDir3('[COLOR aqua]סדרות כללי[/COLOR]',"plugin://plugin.video.mando/?all_w=%7b%7d&data=%20&dates=%20&description=TV&eng_name=%20&episode=%20&fanart=https%3a%2f%2fcdn.mos.cms.futurecdn.net%2fqCD39X4DjbpgxD7ZFW63eG.jpg&fav_status=false&heb_name=%20&iconimage=C%3a%5cUsers%5cUser%5cAppData%5cRoaming%5cKodi%5caddons%5cplugin.video.mando%5cresources%5cartwork%2ftv.png&id=%20&image_master&isr=0&last_id&mode=3&name=%d7%a1%d7%93%d7%a8%d7%95%d7%aa&original_title=%20&season=%20&show_original_year=%20&tmdbid=%20&url=www&video_data=%7b%22rating%22%3a%20%220%22%2c%20%22episode%22%3a%200%2c%20%22title%22%3a%20%22%5cu05e1%5cu05d3%5cu05e8%5cu05d5%5cu05ea%22%2c%20%22season%22%3a%200%2c%20%22TVshowtitle%22%3a%20%22%22%2c%20%22mediatype%22%3a%20%22movie%22%2c%20%22plot%22%3a%20%22TV%22%2c%20%22OriginalTitle%22%3a%20%22%20%22%2c%20%22Tag%22%3a%20%22None%22%2c%20%22id%22%3a%20%22%20%22%7dt;",35,'http://ngarba.xyz/adds/yos/19.jpg')
        addDir3('[COLOR aqua]חיפוש [/COLOR]',"plugin://plugin.video.mando/?all_w=%7b%7d&data=%20&dates=%20&description=TMDB&eng_name=%20&episode=%20&fanart=https%3a%2f%2fsearchengineland.com%2ffigz%2fwp-content%2fseloads%2f2017%2f12%2fcompare-seo-ss-1920-800x450.jpg&fav_status=false&heb_name=%20&iconimage=C%3a%5cUsers%5cUser%5cAppData%5cRoaming%5cKodi%5caddons%5cplugin.video.mando%5cresources%5cartwork%2fsearch.png&id=%20&image_master&isr=0&last_id&mode=14&name=%d7%97%d7%99%d7%a4%d7%95%d7%a9&original_title=%20&season=%20&show_original_year=%20&tmdbid=%20&url=http%3a%2f%2fapi.themoviedb.org%2f3%2fsearch%2ftv%3fapi_key%3d34142515d9d23817496eeb4ff1d223d0%26query%3d%25s%26language%3dhe%26page%3d1&video_data=%7b%22rating%22%3a%20%220%22%2c%20%22episode%22%3a%200%2c%20%22title%22%3a%20%22%5cu05d7%5cu05d9%5cu05e4%5cu05d5%5cu05e9%22%2c%20%22season%22%3a%200%2c%20%22TVshowtitle%22%3a%20%22%22%2c%20%22mediatype%22%3a%20%22movie%22%2c%20%22plot%22%3a%20%22TMDB%22%2c%20%22OriginalTitle%22%3a%20%22%20%22%2c%20%22Tag%22%3a%20%223%22%2c%20%22id%22%3a%20%22%20%22%7d;",35,'http://ngarba.xyz/adds/yos/19.jpg')




def Ctelemedia6():
        addDir3('[COLOR aqua]סדרות כללי[/COLOR]',"plugin://plugin.video.telemedia/?data=%20&dates=%20&description=Tv%20Shows&eng_name=%20&episode=%20&fanart=https%3a%2f%2fstatic.highsnobiety.com%2fthumbor%2fR8JPAdy4hlfFhZj9_YqCQfcNsZ0%3d%2ffit-in%2f800x480%2fsmart%2fstatic.highsnobiety.com%2fwp-content%2fuploads%2f2019%2f02%2f28155224%2fgame-of-thrones-season-8-posters-001.jpg&fav_status=false&groups_id=0&heb_name=%20&iconimage=special%3a%2f%2fhome%2faddons%2fplugin.video.telemedia%2ftele%2ftvshows.png&id=%20&image_master&isr=0&last_id&mode=11&name=%5bCOLOR%20blue%5d%d7%a1%d7%93%d7%a8%d7%95%d7%aa%5b%2fCOLOR%5d&original_title=%20&season=%20&show_original_year=%20&tmdbid=%20&url=%20;",35,'http://ngarba.xyz/adds/yos/19.jpg')
        addDir3('[COLOR aqua]חיפוש[/COLOR]',"plugin://plugin.video.telemedia/?mode=14&name=חפש סידרה&image_master=&heb_name= &last_id=&dates= &data= &original_title= &id= &season= &episode= &tmdbid= &eng_name= &show_original_year= &isr=0&fanart=http%3A%2F%2Ff.frogi.co.il%2Fnews%2F640x300%2F010170efc8f.jpg&url=http%3A%2F%2Fapi.themoviedb.org%2F3%2Fsearch%2Ftv%3Fapi_key%3D34142515d9d23817496eeb4ff1d223d0%26query%3D%25s%26language%3Dhe%26page%3D1&iconimage=special%3A%2F%2Fhome%2Faddons%2Fplugin.video.telemedia%2Ftele%2FTv_Show%2Fsearch.png&description=TMDB&fav_status=false&groups_id=0;",35,'http://ngarba.xyz/adds/yos/19.jpg')



def CCHICCO7():
        addDir3('[COLOR aqua]סדרות כללי[/COLOR]',"plugin://plugin.video.CHICCO/?cat_level=%20&count=0&description=%d7%a1%d7%93%d7%a8%d7%95%d7%aa%20%d7%9e%d7%97%d7%95%d7%9c&fanart=https%3a%2f%2f3.bp.blogspot.com%2f-ua674nSzp-w%2fWgyhVc-31FI%2fAAAAAAAAHh8%2fTxirlq_NgeIa_o_GL9DUYrIqFgzLaxmnQCLcBGAs%2fs1600%2f10%252Bgreat%252Btv%252Bshows%252Bwe%252Blost%252Bin%252B2017.jpeg&iconimage=https%3a%2f%2f3.bp.blogspot.com%2f-ua674nSzp-w%2fWgyhVc-31FI%2fAAAAAAAAHh8%2fTxirlq_NgeIa_o_GL9DUYrIqFgzLaxmnQCLcBGAs%2fs1600%2f10%252Bgreat%252Btv%252Bshows%252Bwe%252Blost%252Bin%252B2017.jpeg&index_depth=0&lang=eng&mode=5&name=%d7%a1%d7%93%d7%a8%d7%95%d7%aa&page&selected_list=%20&url=%d7%a1%d7%93%d7%a8%d7%95%d7%aa",35,'http://ngarba.xyz/adds/yos/19.jpg')
        addDir3('[COLOR aqua]נוספו לאחרונה[/COLOR]',"plugin://plugin.video.CHICCO/?cat_level=%20&count=0&description&fanart=https%3a%2f%2fwpblink.com%2fsites%2fdefault%2ffiles%2fwallpaper%2fmovie%2f72098%2favatar-wallpapers-hd-72098-5294999.png&iconimage=http%3a%2f%2fngarba.xyz%2fadds%2fyos%2f24.jpg&index_depth=0&lang=%20&mode=18&name=%5bB%5d%5bCOLOR%20burlywood%5d-%d7%90%d7%97%d7%a8%d7%95%d7%a0%d7%99%d7%9d%20%5b%2fCOLOR%5d%5b%2fB%5d%5bB%5d%5bCOLOR%20aqua%5d%d7%a4%d7%a8%d7%a7%d7%99%d7%9d-%20%5b%2fCOLOR%5d%5b%2fB%5d&page&selected_list=%20&url=tv",35,'http://ngarba.xyz/adds/yos/19.jpg')
        addDir3('[COLOR aqua]חיפוש[/COLOR]',"plugin://plugin.video.CHICCO/?cat_level=%20&count=0&description&fanart=http%3a%2f%2fb2acpa.com%2f%7ebairdcpa%2fimages%2fTerminator.jpg&iconimage=http%3a%2f%2fngarba.xyz%2fadds%2fyos%2f8.jpg&index_depth=0&lang=%20&mode=6&name=%5bB%5d%5bCOLOR%20burlywood%5d%d7%a4%d7%95%d7%a9%5b%2fCOLOR%5d%5b%2fB%5d%5bB%5d%5bCOLOR%20aqua%5d%d7%97%d7%99%5b%2fCOLOR%5d%5b%2fB%5d&page&selected_list=%20&url=movie;",35,'http://ngarba.xyz/adds/yos/19.jpg')

def CFlash8():
        addDir3('[COLOR aqua]סדרות כללי[/COLOR]',"plugin://plugin.video.FlashTV/?cat_level=%20&count=0&description=%20&fanart&iconimage=https%3a%2f%2fi.imgur.com%2f9hRleTP.jpg&index_depth=0&lang=eng&mode=5&name=%d7%a1%d7%93%d7%a8%d7%95%d7%aa&page&selected_list=%20&url=%d7%a1%d7%93%d7%a8%d7%95%d7%aa",35,'http://ngarba.xyz/adds/yos/19.jpg')
        addDir3('[COLOR aqua]נוספו לאחרונה[/COLOR]',"plugin://plugin.video.FlashTV/?cat_level=%20&count=0&description&fanart=https%3a%2f%2fimages.hdqwalls.com%2fdownload%2fassassins-creed-valhalla-female-eivor-axe-8k-bn-1920x1080.jpg&iconimage=http%3a%2f%2fngarba.xyz%2fadds%2fyos%2f24.jpg&index_depth=0&lang=%20&mode=18&name=%5bB%5d%5bCOLOR%20burlywood%5d-%d7%90%d7%97%d7%a8%d7%95%d7%a0%d7%99%d7%9d%20%5b%2fCOLOR%5d%5b%2fB%5d%5bB%5d%5bCOLOR%20aqua%5d%d7%a4%d7%a8%d7%a7%d7%99%d7%9d-%20%5b%2fCOLOR%5d%5b%2fB%5d&page&selected_list=%20&url=tv",35,'http://ngarba.xyz/adds/yos/19.jpg')
        addDir3('[COLOR aqua]חיפוש[/COLOR]',"plugin://plugin.video.FlashTV/?cat_level=%20&count=0&description&fanart=http%3a%2f%2fb2acpa.com%2f%7ebairdcpa%2fimages%2fTerminator.jpg&iconimage=http%3a%2f%2fngarba.xyz%2fadds%2fyos%2f8.jpg&index_depth=0&lang=%20&mode=6&name=%5bB%5d%5bCOLOR%20burlywood%5d%d7%a4%d7%95%d7%a9%5b%2fCOLOR%5d%5b%2fB%5d%5bB%5d%5bCOLOR%20aqua%5d%d7%97%d7%99%5b%2fCOLOR%5d%5b%2fB%5d&page&selected_list=%20&url=movie;",35,'http://ngarba.xyz/adds/yos/19.jpg')




def Didanplus1():
        addDir3('[COLOR aqua]ילדים ונוער[/COLOR]',"plugin://plugin.video.idanplus/?iconimage=https%253A%252F%252Fkanweb.blob.core.windows.net%252Fdownload%252Fpictures%252Fline2307879_lineIcon_2.png&mode=1&module=kan&moredata&name=%5bCOLOR%20orange%5d%5bB%5d%d7%99%d7%9c%d7%93%d7%99%d7%9d%20%d7%95%d7%a0%d7%95%d7%a2%d7%a8%5b%2fB%5d%5b%2fCOLOR%5d&url=https%253A%252F%252Fwww.kankids.org.il%252Fpage.aspx%253FlandingPageId%253D1273",35,'http://ngarba.xyz/adds/yos/13.jpg')
        addDir3('[COLOR aqua]קלטות ילדים[/COLOR]',"plugin://plugin.video.idanplus/?iconimage=C%253A%255CUsers%255CUser%255CAppData%255CRoaming%255CKodi%255Caddons%255Cplugin.video.idanplus%255Cresources%255Cimages%255Ckids.jpg&mode=1&module=keshet&moredata&name=%5bB%5d%d7%a7%d7%9c%d7%98%d7%95%d7%aa%20%d7%99%d7%9c%d7%93%d7%99%d7%9d%5b%2fB%5d&url=https%253A%252F%252Fwww.mako.co.il%252Fmako-vod-kids",35,'http://ngarba.xyz/adds/yos/13.jpg')

def Dsdarottv2():
        addDir3('[COLOR aqua]סדרות כללי[/COLOR]',"@@@",35,'http://ngarba.xyz/adds/yos/13.jpg')
        addDir3('[COLOR aqua]חיפוש[/COLOR]',"@@@",35,'http://ngarba.xyz/adds/yos/13.jpg')


def Dthecrew3():
        addDir3('[COLOR aqua]ילדים כללי[/COLOR]',"plugin://plugin.video.thecrew/?action=kidsgreyNavigator",35,'http://ngarba.xyz/adds/yos/13.jpg')
        addDir3('[COLOR aqua]חיפוש באנגלית[/COLOR]',"plugin://plugin.video.thecrew/?action=movieSearchnew",35,'http://ngarba.xyz/adds/yos/13.jpg')

def Dmando4():
        addDir3('[COLOR aqua]סירטי אנימציה[/COLOR]',"plugin://plugin.video.mando/?all_w=%7b%7d&data=%20&dates=%20&description=%d7%90%d7%a0%d7%99%d7%9e%d7%a6%d7%99%d7%94&eng_name=%20&episode=%20&fanart=https%3a%2f%2fwordsfromjalynn.files.wordpress.com%2f2014%2f12%2fmovie-genres-1.png&fav_status=false&heb_name=%20&iconimage=https%3a%2f%2fwordsfromjalynn.files.wordpress.com%2f2014%2f12%2fmovie-genres-1.png&id=%20&image_master&isr=0&last_id&mode=14&name=%d7%90%d7%a0%d7%99%d7%9e%d7%a6%d7%99%d7%94&original_title=%20&season=%20&show_original_year=%20&tmdbid=%20&url=http%3a%2f%2fapi.themoviedb.org%2f3%2fgenre%2f16%2fmovies%3fapi_key%3d34142515d9d23817496eeb4ff1d223d0%26language%3dhe%26page%3d1&video_data=%7b%22rating%22%3a%20%220%22%2c%20%22episode%22%3a%200%2c%20%22title%22%3a%20%22%5cu05d0%5cu05e0%5cu05d9%5cu05de%5cu05e6%5cu05d9%5cu05d4%22%2c%20%22season%22%3a%200%2c%20%22TVshowtitle%22%3a%20%22%22%2c%20%22mediatype%22%3a%20%22movie%22%2c%20%22plot%22%3a%20%22%5cu05d0%5cu05e0%5cu05d9%5cu05de%5cu05e6%5cu05d9%5cu05d4%22%2c%20%22OriginalTitle%22%3a%20%22%20%22%2c%20%22Tag%22%3a%20%2218%22%2c%20%22id%22%3a%20%22%20%22%7d",35,'http://ngarba.xyz/adds/yos/13.jpg')
        addDir3('[COLOR aqua]סדרות אנימציה[/COLOR]',"plugin://plugin.video.mando/?all_w=%7b%7d&data=%20&dates=%20&description=%d7%90%d7%a0%d7%99%d7%9e%d7%a6%d7%99%d7%94&eng_name=%20&episode=%20&fanart=https%3a%2f%2fwordsfromjalynn.files.wordpress.com%2f2014%2f12%2fmovie-genres-1.png&fav_status=false&heb_name=%20&iconimage=https%3a%2f%2fwordsfromjalynn.files.wordpress.com%2f2014%2f12%2fmovie-genres-1.png&id=%20&image_master&isr=0&last_id&mode=14&name=%d7%90%d7%a0%d7%99%d7%9e%d7%a6%d7%99%d7%94&original_title=%20&season=%20&show_original_year=%20&tmdbid=%20&url=http%3a%2f%2fapi.themoviedb.org%2f3%2fdiscover%2ftv%3fapi_key%3d34142515d9d23817496eeb4ff1d223d0%26sort_by%3dpopularity.desc%26with_genres%3d16%26language%3dhe%26page%3d1&video_data=%7b%22rating%22%3a%20%220%22%2c%20%22episode%22%3a%200%2c%20%22title%22%3a%20%22%5cu05d0%5cu05e0%5cu05d9%5cu05de%5cu05e6%5cu05d9%5cu05d4%22%2c%20%22season%22%3a%200%2c%20%22TVshowtitle%22%3a%20%22%22%2c%20%22mediatype%22%3a%20%22movie%22%2c%20%22plot%22%3a%20%22%5cu05d0%5cu05e0%5cu05d9%5cu05de%5cu05e6%5cu05d9%5cu05d4%22%2c%20%22OriginalTitle%22%3a%20%22%20%22%2c%20%22Tag%22%3a%20%2218%22%2c%20%22id%22%3a%20%22%20%22%7d",35,'http://ngarba.xyz/adds/yos/13.jpg')
        addDir3('[COLOR aqua]חיפוש[/COLOR]',"plugin://plugin.video.mando/?all_w=%7b%7d&data=%20&dates=%20&description=Search&eng_name=%20&episode=%20&fanart=https%3a%2f%2fsearchengineland.com%2ffigz%2fwp-content%2fseloads%2f2017%2f12%2fcompare-seo-ss-1920-800x450.jpg&fav_status=false&heb_name=%20&iconimage=C%3a%5cUsers%5cUser%5cAppData%5cRoaming%5cKodi%5caddons%5cplugin.video.mando%5cresources%5cartwork%2fsearch.png&id=%20&image_master&isr=0&last_id&mode=5&name=%d7%97%d7%99%d7%a4%d7%95%d7%a9&original_title=%20&season=%20&show_original_year=%20&tmdbid=%20&url=www&video_data=%7b%22rating%22%3a%20%220%22%2c%20%22episode%22%3a%200%2c%20%22title%22%3a%20%22%5cu05d7%5cu05d9%5cu05e4%5cu05d5%5cu05e9%22%2c%20%22season%22%3a%200%2c%20%22TVshowtitle%22%3a%20%22%22%2c%20%22mediatype%22%3a%20%22movie%22%2c%20%22plot%22%3a%20%22Search%22%2c%20%22OriginalTitle%22%3a%20%22%20%22%2c%20%22Tag%22%3a%20%22None%22%2c%20%22id%22%3a%20%22%20%22%7d",35,'http://ngarba.xyz/adds/yos/13.jpg')




def Dtelemedia5():
        addDir3('[COLOR aqua]סרטי אנימציה[/COLOR]',"plugin://plugin.video.telemedia/?data=%20&dates=%20&description=%d7%90%d7%a0%d7%99%d7%9e%d7%a6%d7%99%d7%94&eng_name=%20&episode=%20&fanart=http%3a%2f%2fwww.printime.co.il%2fimage%2fusers%2f16584%2fftp%2fmy_files%2fsmileynumbers1we.jpg&fav_status=false&groups_id=0&heb_name=%20&iconimage=http%3a%2f%2fwww.printime.co.il%2fimage%2fusers%2f16584%2fftp%2fmy_files%2fsmileynumbers1we.jpg&id=%20&image_master&isr=0&last_id&mode=14&name=%d7%90%d7%a0%d7%99%d7%9e%d7%a6%d7%99%d7%94&original_title=%20&season=%20&show_original_year=%20&tmdbid=%20&url=http%3a%2f%2fapi.themoviedb.org%2f3%2fgenre%2f16%2fmovies%3fapi_key%3d34142515d9d23817496eeb4ff1d223d0%26language%3dhe%26page%3d1",35,'http://ngarba.xyz/adds/yos/13.jpg')
        addDir3('[COLOR aqua]עולם הילדים[/COLOR]',"plugin://plugin.video.telemedia/?data=-1001195519301&dates=%20&description=%d7%a2%d7%95%d7%9c%d7%9d%20%d7%94%d7%99%d7%9c%d7%93%d7%99%d7%9d&eng_name=%20&episode=%20&fanart=https%3a%2f%2finsidethemagic-119e2.kxcdn.com%2fwp-content%2fuploads%2f2018%2f08%2fExpo19_11x16_Poster_KeyArt_72dpi-1-792x400.jpg&fav_status=false&groups_id=0&heb_name=%20&iconimage=special%3a%2f%2fhome%2faddons%2fplugin.video.telemedia%2ftele%2fkids.png&id=%20&image_master&isr=0&last_id&mode=31&name=%5bCOLOR%20blue%5d%d7%a2%d7%95%d7%9c%d7%9d%20%d7%94%d7%99%d7%9c%d7%93%d7%99%d7%9d%5b%2fCOLOR%5d&original_title=%20&season=%20&show_original_year=%20&tmdbid=%20&url=www",35,'http://ngarba.xyz/adds/yos/13.jpg')
        addDir3('[COLOR aqua]סדרות אנימציה[/COLOR]',"plugin://plugin.video.telemedia/?data=%20&dates=%20&description=%d7%90%d7%a0%d7%99%d7%9e%d7%a6%d7%99%d7%94&eng_name=%20&episode=%20&fanart=http%3a%2f%2fwww.printime.co.il%2fimage%2fusers%2f16584%2fftp%2fmy_files%2fsmileynumbers1we.jpg&fav_status=false&groups_id=0&heb_name=%20&iconimage=http%3a%2f%2fwww.printime.co.il%2fimage%2fusers%2f16584%2fftp%2fmy_files%2fsmileynumbers1we.jpg&id=%20&image_master&isr=0&last_id&mode=14&name=%d7%90%d7%a0%d7%99%d7%9e%d7%a6%d7%99%d7%94&original_title=%20&season=%20&show_original_year=%20&tmdbid=%20&url=http%3a%2f%2fapi.themoviedb.org%2f3%2fdiscover%2ftv%3fapi_key%3d34142515d9d23817496eeb4ff1d223d0%26sort_by%3dpopularity.desc%26with_genres%3d16%26language%3dhe%26page%3d1",35,'http://ngarba.xyz/adds/yos/13.jpg')
        addDir3('[COLOR aqua]חיפוש סדרה[/COLOR]',"plugin://plugin.video.telemedia/?mode=14&name=חפש סידרה&image_master=&heb_name= &last_id=&dates= &data= &original_title= &id= &season= &episode= &tmdbid= &eng_name= &show_original_year= &isr=0&fanart=http%3A%2F%2Ff.frogi.co.il%2Fnews%2F640x300%2F010170efc8f.jpg&url=http%3A%2F%2Fapi.themoviedb.org%2F3%2Fsearch%2Ftv%3Fapi_key%3D34142515d9d23817496eeb4ff1d223d0%26query%3D%25s%26language%3Dhe%26page%3D1&iconimage=special%3A%2F%2Fhome%2Faddons%2Fplugin.video.telemedia%2Ftele%2FTv_Show%2Fsearch.png&description=TMDB&fav_status=false&groups_id=0",35,'http://ngarba.xyz/adds/yos/13.jpg')
        addDir3('[COLOR aqua]חיפוש סרט[/COLOR]',"plugin://plugin.video.telemedia/?mode=14&name=חפש סרט&image_master=&heb_name= &last_id=&dates= &data= &original_title= &id= &season= &episode= &tmdbid= &eng_name= &show_original_year= &isr=0&fanart=http%3A%2F%2Fwww.videomotion.co.il%2Fwp-content%2Fuploads%2Fwhatwedo-Pic-small.jpg&url=http%3A%2F%2Fapi.themoviedb.org%2F3%2Fsearch%2Fmovie%3Fapi_key%3D34142515d9d23817496eeb4ff1d223d0%26query%3D%25s%26language%3Dhe%26append_to_response%3Dorigin_country%26page%3D1&iconimage=special%3A%2F%2Fhome%2Faddons%2Fplugin.video.telemedia%2Ftele%2FMovies%2Fmovie_search.png&description=Tmdb&fav_status=false&groups_id=0",35,'http://ngarba.xyz/adds/yos/13.jpg')



def DCHICCO6():
        addDir3('[COLOR aqua]סרטים מדובבים[/COLOR]',"plugin://plugin.video.CHICCO/?cat_level=%20&count=0&description=%20&fanart=http%3a%2f%2fmoridim.me%2fimages%2flarge%2f9424.jpg&iconimage=http%3a%2f%2fmoridim.me%2fimages%2flarge%2f9424.jpg&index_depth=0&lang=eng&mode=5&name=%d7%a1%d7%a8%d7%98%d7%99%d7%9d%20%d7%9e%d7%93%d7%95%d7%91%d7%91%d7%99%d7%9d&page&selected_list=%20&url=%d7%a1%d7%a8%d7%98%d7%99%d7%9d%d7%a1%d7%a8%d7%98%d7%99%d7%9d%20%d7%9e%d7%93%d7%95%d7%91%d7%91%d7%99%d7%9d",35,'http://ngarba.xyz/adds/yos/13.jpg')
        addDir3('[COLOR aqua]חיפוש[/COLOR]',"plugin://plugin.video.CHICCO/?cat_level=%20&count=0&description&fanart=http%3a%2f%2fb2acpa.com%2f%7ebairdcpa%2fimages%2fTerminator.jpg&iconimage=http%3a%2f%2fngarba.xyz%2fadds%2fyos%2f8.jpg&index_depth=0&lang=%20&mode=6&name=%5bB%5d%5bCOLOR%20burlywood%5d%d7%a4%d7%95%d7%a9%5b%2fCOLOR%5d%5b%2fB%5d%5bB%5d%5bCOLOR%20aqua%5d%d7%97%d7%99%5b%2fCOLOR%5d%5b%2fB%5d&page&selected_list=%20&url=movie",35,'http://ngarba.xyz/adds/yos/13.jpg')

def DFlash7():
        addDir3('[COLOR aqua]סרטים מדובבים[/COLOR]',"plugin://plugin.video.FlashTV/?cat_level=%20&count=0&description=%20&fanart&iconimage=https%3a%2f%2fwww.xtrafondos.com%2fwallpapers%2ftoy-story-4-personajes-poster-3326.jpg&index_depth=0&lang=eng&mode=5&name=%d7%a1%d7%a8%d7%98%d7%99%d7%9d%20%d7%9e%d7%93%d7%95%d7%91%d7%91%d7%99%d7%9d&page&selected_list=%20&url=%d7%a1%d7%a8%d7%98%d7%99%d7%9d%d7%a1%d7%a8%d7%98%d7%99%d7%9d%20%d7%9e%d7%93%d7%95%d7%91%d7%91%d7%99%d7%9d",35,'http://ngarba.xyz/adds/yos/13.jpg')
        addDir3('[COLOR aqua]חיפוש[/COLOR]',"plugin://plugin.video.FlashTV/?cat_level=%20&count=0&description&fanart=http%3a%2f%2fb2acpa.com%2f%7ebairdcpa%2fimages%2fTerminator.jpg&iconimage=http%3a%2f%2fngarba.xyz%2fadds%2fyos%2f8.jpg&index_depth=0&lang=%20&mode=6&name=%5bB%5d%5bCOLOR%20burlywood%5d%d7%a4%d7%95%d7%a9%5b%2fCOLOR%5d%5b%2fB%5d%5bB%5d%5bCOLOR%20aqua%5d%d7%97%d7%99%5b%2fCOLOR%5d%5b%2fB%5d&page&selected_list=%20&url=movie",35,'http://ngarba.xyz/adds/yos/13.jpg')


def Eidanplus1():
        addDir3('[COLOR aqua]ערוצי ישראל[/COLOR]',"plugin://plugin.video.idanplus/?iconimage=C%253A%255CUsers%255CUser%255CAppData%255CRoaming%255CKodi%255Caddons%255Cplugin.video.idanplus%255Cicon.png&mode=1&module&moredata&name=%5bB%5d%d7%98%d7%9c%d7%95%d7%99%d7%96%d7%99%d7%94%5b%2fB%5d&url",35,'http://ngarba.xyz/adds/yos/3.jpg')
        addDir3('[COLOR aqua]רדיו ישראל[/COLOR]',"plugin://plugin.video.idanplus/?iconimage=C%253A%255CUsers%255CUser%255CAppData%255CRoaming%255CKodi%255Caddons%255Cplugin.video.idanplus%255Cicon.png&mode=3&module&moredata&name=%5bB%5d%d7%a8%d7%93%d7%99%d7%95%5b%2fB%5d&url",35,'http://ngarba.xyz/adds/yos/3.jpg')
def EServiceil2():
        addDir3('[COLOR aqua]'+translate(70000004)+'[/COLOR]',"plugin://plugin.video.live.streamspro/?url=https%3a%2f%2fpastebin.com%2fraw%2fQYKCtZqs&mode=1",35,'https://cdn.imgbin.com/5/7/10/imgbin-adam-sandler-click-film-poster-michael-newman-adam-sandler-6D9Ka94946DkP4diMLBF2CkPH.jpg')
def Ethecrew3():
        addDir3('[COLOR aqua]IPTV[/COLOR]',"plugin://plugin.video.thecrew/?action=whitehat",35,'http://ngarba.xyz/adds/yos/3.jpg')




def FYoutubeMusic1():
        addDir3('[COLOR aqua]חיפוש[/COLOR]',"plugin://plugin.video.spotitube/?mode=SearchDeezer",35,'http://ngarba.xyz/adds/yos/12.jpg')
        addDir3('[COLOR aqua]כניסה להרחבה[/COLOR]',"plugin://plugin.video.spotitube/?content_type=video",35,'http://ngarba.xyz/adds/yos/12.jpg')
def FServiceil2():
        addDir('[COLOR aqua]מוזיקה(יוטיוב)[/COLOR]','url',9876513,'http://ngarba.xyz/adds/yos/12.jpg')
        addDir3('[COLOR aqua]רדיו(עולם)[/COLOR]',"plugin://plugin.video.live.streamspro/?fanart=https%3a%2f%2fwww.wallpapertip.com%2fwmimgs%2f172-1728115_world-radio-day-latest-new-pc-background-desktop.jpg&mode=1&name=%5bCOLOR%20blue%5d%5bCOLOR%20deepskyblue%5d%d7%a8%d7%93%d7%99%d7%95-%d7%a2%d7%95%d7%9c%d7%9d%5b%2fCOLOR%5d&url=https%3a%2f%2fgithub.com%2fyonni55555%2fRP%2fraw%2fmaster%2fRADIO.txt",35,'http://ngarba.xyz/adds/yos/12.jpg')
        addDir3('[COLOR aqua]קבצי(שמע)[/COLOR]',"plugin://plugin.video.live.streamspro/?fanart=https%3a%2f%2fi.pinimg.com%2foriginals%2f84%2ffb%2fda%2f84fbdac0f75c9293a5b1cf58361d88f6.jpg&mode=1&name=%5bCOLOR%20burlywood%5d%5bCOLOR%20deepskyblue%5d%d7%a7%d7%91%d7%a6%d7%99%20%d7%a9%d7%9e%d7%a2%20%d7%98%d7%95%d7%a4-500(%d7%90%d7%a0%d7%92%d7%9c%d7%99%d7%aa)%20%5b%2fCOLOR%5d&url=https%3a%2f%2fgithub.com%2fyonni55555%2fRD%2fraw%2fmaster%2f-500-Greatest-Songs-.txt",35,'http://ngarba.xyz/adds/yos/12.jpg')
        addDir3('[COLOR aqua]הופעות(חיות)[/COLOR]',"plugin://plugin.video.live.streamspro/?fanart=https%3a%2f%2fi.pinimg.com%2foriginals%2f84%2ffb%2fda%2f84fbdac0f75c9293a5b1cf58361d88f6.jpg&mode=1&name=%5bCOLOR%20burlywood%5d%5bCOLOR%20deepskyblue%5d%d7%94%d7%95%d7%a4%d7%a2%d7%95%d7%aa%20%d7%97%d7%99%d7%95%d7%aa%20%d7%9e%d7%9c%d7%90%d7%95%d7%aa-%d7%97%d7%95%d7%9c-A-B-C%20%5b%2fCOLOR%5d&url=https%3a%2f%2fpastebin.com%2fraw%2fKAisZ2hT",35,'http://ngarba.xyz/adds/yos/12.jpg')

def Fidanplus3():
        addDir3('[COLOR aqua]רדיו ישראל[/COLOR]',"plugin://plugin.video.idanplus/?iconimage=C%253A%255CUsers%255CUser%255CAppData%255CRoaming%255CKodi%255Caddons%255Cplugin.video.idanplus%255Cicon.png&mode=3&module&moredata&name=%5bB%5d%d7%a8%d7%93%d7%99%d7%95%5b%2fB%5d&url",35,'http://ngarba.xyz/adds/yos/12.jpg')
        addDir3('[COLOR aqua]מוזיקה - גלגל"צ[/COLOR]',"plugin://plugin.video.idanplus/?iconimage=C%253A%255CUsers%255CUser%255CAppData%255CRoaming%255CKodi%255Caddons%255Cplugin.video.idanplus%255Cresources%255Cimages%255Cglglz.jpg&mode=1&module=glz&moredata&name=%5bB%5d%d7%9e%d7%95%d7%96%d7%99%d7%a7%d7%94%20-%20%d7%92%d7%9c%d7%92%d7%9c%22%d7%a6%5b%2fB%5d&url=glglz",35,'http://ngarba.xyz/adds/yos/12.jpg')
        addDir3('[COLOR aqua]מוזיקה - eco99fm[/COLOR]',"plugin://plugin.video.idanplus/?iconimage=C%253A%255CUsers%255CUser%255CAppData%255CRoaming%255CKodi%255Caddons%255Cplugin.video.idanplus%255Cresources%255Cimages%255C99fm.png&mode=0&module=99fm&moredata&name=%5bB%5d%d7%9e%d7%95%d7%96%d7%99%d7%a7%d7%94%20-%20eco99fm%5b%2fB%5d&url",35,'http://ngarba.xyz/adds/yos/12.jpg')
        addDir3('[COLOR aqua]מוזיקה - 100fm[/COLOR]',"plugin://plugin.video.idanplus/?iconimage=C%253A%255CUsers%255CUser%255CAppData%255CRoaming%255CKodi%255Caddons%255Cplugin.video.idanplus%255Cresources%255Cimages%255C100fm.jpg&mode=0&module=100fm&moredata&name=%5bB%5d%d7%9e%d7%95%d7%96%d7%99%d7%a7%d7%94%20-%20100fm%5b%2fB%5d&url",35,'http://ngarba.xyz/adds/yos/12.jpg')
        addDir3('[COLOR aqua]VOD-ערוץ 24 החדש[/COLOR]',"plugin://plugin.video.idanplus/?iconimage=C%253A%255CUsers%255CUser%255CAppData%255CRoaming%255CKodi%255Caddons%255Cplugin.video.idanplus%255Cresources%255Cimages%255C24telad.png&mode=1&module=keshet&moredata&name=%5bB%5d%d7%a2%d7%a8%d7%95%d7%a5%2024%20%d7%94%d7%97%d7%93%d7%a9%5b%2fB%5d&url=http%253A%252F%252Fwww.mako.co.il%252Fmako-vod-music24",35,'http://ngarba.xyz/adds/yos/12.jpg')
        addDir3('[COLOR aqua]הופעות[/COLOR]',"plugin://plugin.video.idanplus/?iconimage=C%253A%255CUsers%255CUser%255CAppData%255CRoaming%255CKodi%255Caddons%255Cplugin.video.idanplus%255Cresources%255Cimages%255Clive-music.jpg&mode=1&module=keshet&moredata&name=%5bB%5d%d7%94%d7%95%d7%a4%d7%a2%d7%95%d7%aa%5b%2fB%5d&url=https%253A%252F%252Fwww.mako.co.il%252Fmako-vod-more%252Fconcerts",35,'http://ngarba.xyz/adds/yos/12.jpg')
 




def GSportHD1():
        addDir3('[COLOR aqua]ספורט(כללי)[/COLOR]',"plugin://plugin.video.sporthdme/",35,'http://ngarba.xyz/adds/yos/17.jpg')

def Gthecrew2():
        addDir3('[COLOR aqua]ספורט(כללי)[/COLOR]',"plugin://plugin.video.thecrew/?action=bluehat",35,'http://ngarba.xyz/adds/yos/17.jpg')

def GServiceil3():
        addDir('[COLOR aqua]ספורט(יוטיוב)[/COLOR]','url',9876515,'http://ngarba.xyz/adds/yos/17.jpg')

def Gidanplus4():
        addDir3('[COLOR aqua]VOD-ספורט-5[/COLOR]',"plugin://plugin.video.idanplus/?iconimage=C%253A%255CUsers%255CUser%255CAppData%255CRoaming%255CKodi%255Caddons%255Cplugin.video.idanplus%255Cresources%255Cimages%255CSport5.png&mode=0&module=sport5&moredata&name=%5bB%5d%d7%9b%d7%9c%20%d7%94%d7%aa%d7%9b%d7%a0%d7%99%d7%95%d7%aa%5b%2fB%5d&url",35,'http://ngarba.xyz/adds/yos/17.jpg')
        addDir3('[COLOR aqua]VOD-ספורט-1[/COLOR]',"plugin://plugin.video.idanplus/?iconimage=C%253A%255CUsers%255CUser%255CAppData%255CRoaming%255CKodi%255Caddons%255Cplugin.video.idanplus%255Cresources%255Cimages%255Csport1.jpg&mode=0&module=sport1&moredata&name=%5bB%5d%d7%9b%d7%9c%20%d7%94%d7%aa%d7%9b%d7%a0%d7%99%d7%95%d7%aa%5b%2fB%5d&url",35,'http://ngarba.xyz/adds/yos/17.jpg')





def Dglllll():

        addDir3('[COLOR aqua]shadow[/COLOR]',"plugin://plugin.video.shadow/?all_w=%7b%7d&data=%20&dates=%20&description=Search&eng_name=%20&episode=%20&fanart=https%3a%2f%2fsearchengineland.com%2ffigz%2fwp-content%2fseloads%2f2017%2f12%2fcompare-seo-ss-1920-800x450.jpg&fav_status=false&heb_name=%20&iconimage=C%3a%5cUsers%5cUser%5cAppData%5cRoaming%5cKodi%5caddons%5cplugin.video.shadow%5cresources%5cartwork%2fsearch.png&id=%20&image_master&isr=0&last_id&mode=5&name=%d7%97%d7%99%d7%a4%d7%95%d7%a9&original_title=%20&season=%20&show_original_year=%20&tmdbid=%20&url=www&video_data=%7b%22rating%22%3a%20%220%22%2c%20%22episode%22%3a%200%2c%20%22title%22%3a%20%22%5cu05d7%5cu05d9%5cu05e4%5cu05d5%5cu05e9%22%2c%20%22season%22%3a%200%2c%20%22TVshowtitle%22%3a%20%22%22%2c%20%22mediatype%22%3a%20%22movie%22%2c%20%22plot%22%3a%20%22Search%22%2c%20%22OriginalTitle%22%3a%20%22%20%22%2c%20%22Tag%22%3a%20%22None%22%2c%20%22id%22%3a%20%22%20%22%7d",35,art + 'shadow.png')

        addDir3('[COLOR aqua]THE CREW [/COLOR]',"plugin://plugin.video.thecrew/?action=searchNavigator",35,'https://www.wirelesshack.org/wp-content/uploads/2020/03/How-To-Install-The-Crew-Kodi-Addon.jpg')

        addDir3('[COLOR aqua]Elementum [/COLOR]',"plugin://plugin.video.elementum/movies/search?keyboard=1",35,art + 'Elementum.png')

        addDir3('[COLOR aqua]Thorrent [/COLOR]',"plugin://plugin.video.torrent/?data= &dates= &description=חיפוש&eng_name= &episode= &fanart=&fav_status=false&heb_name= &iconimage=&id= &isr=0&mode=15&name=&original_title= &season= &show_original_year= &tmdbid= &url=www",35,'https://res-4.cloudinary.com/crunchbase-production/image/upload/c_lpad,h_256,w_256,f_auto,q_auto:eco/v1500302210/ihbu4znuw8heie4j7ad3.png')
        addDir3('[COLOR aqua]עידן+ [/COLOR]',"plugin://plugin.video.idanplus/?moredata=&name=]&url=&iconimage=i\addons\plugin.video.idanplus\icon.png&module=&mode=4",35,art + 'i+.png')

        addDir3('[COLOR aqua]עידן(קשת-12)+ [/COLOR]',"plugin://plugin.video.idanplus/?iconimage=C%253A%255CUsers%255CUser%255CAppData%255CRoaming%255CKodi%255Caddons%255Cplugin.video.idanplus%255Cresources%255Cimages%255Csearch.jpg&mode=6&module=keshet&moredata&name=%d7%97%d7%99%d7%a4%d7%95%d7%a9&url=https%253A%252F%252Fwww.mako.co.il%252Fautocomplete%252FvodAutocompletion.ashx%253Fquery%253D%257B0%257D%2526max%253D60%2526id%253Dquery",35,art + 'i+.png')

        addDir3('[COLOR aqua]טלמדיה [/COLOR]',"plugin://plugin.video.telemedia/?data=all&dates=%20&description=Search%20All&eng_name=%20&episode=%20&fanart=https%3a%2f%2fwww.komando.com%2fwp-content%2fuploads%2f2017%2f12%2fcomputer-search.jpg&fav_status=false&heb_name=%20&iconimage=https%3a%2f%2fsitechecker.pro%2fwp-content%2fuploads%2f2017%2f12%2fsearch-engines.png&id=%20&image_master&isr=0&last_id=0%24%24%240&mode=6&name=%5bCOLOR%20yellow%5d%d7%97%d7%99%d7%a4%d7%95%d7%a9%20%d7%9b%d7%9c%d7%9c%d7%99%5b%2fCOLOR%5d&original_title=%20&season=%20&show_original_year=%20&tmdbid=%20&url=%20",35,art + 'tel.png')
        addDir3('[COLOR aqua]סדרות טיוי [/COLOR]',"plugin://plugin.video.sdarot.tv/search/0",35,art + 'sdar.png')

        addDir3('[COLOR aqua]Movix live [/COLOR]',"plugin://plugin.video.movixws/?description=%d7%97%d7%99%d7%a4%d7%95%d7%a9&fanart=C%3a%5cUsers%5cUser%5cAppData%5cRoaming%5cKodi%5caddons%5cplugin.video.movixws%5cresources%5clogo%2fsearch.png&iconimage=C%3a%5cUsers%5cUser%5cAppData%5cRoaming%5cKodi%5caddons%5cplugin.video.movixws%5cresources%5clogo%2fsearch.png&mode=5&name=%5bCOLOR%20aqua%5d%5bI%5d%d7%97%d7%99%d7%a4%d7%95%d7%a9%5b%2fI%5d%5b%2fCOLOR%5d&url=www",35,art + 'movixws.png')
        addDir3('[COLOR aqua]יוטיוב [/COLOR]',"plugin://plugin.video.youtube/kodion/search/input/",35,art + 'ysearch.png')
        addDir3('[COLOR aqua]מי יוטיוב [/COLOR]',"plugin://plugin.video.MyYoutube/kodion/search/input/?description=חיפוש&fanart= &iconimage= &mode=4&name=חיפוש&url=www",35,art + 'myy.png')



def ezmaintenanceplus():

        addDir3('[COLOR aqua]ניקוי קאש+[/COLOR]',"plugin://script.ezmaintenanceplus/?action=maintenance&description&name=[COLOR white][B]MAINTENANCE[/B][/COLOR]&url=ur",35,art + 'ezmaintenanceplus.png')

        addDir3('[COLOR aqua]בדיקת מהירות[/COLOR]',"plugin://script.ezmaintenanceplus/?url=ur&action=speedtest&name=[COLOR white][B]SPEEDTEST[/B][/COLOR]&description=",35,art + 'ezmaintenanceplus.png')

        addDir3('[COLOR aqua]הגדרות ההרחבה[/COLOR]',"plugin://script.ezmaintenanceplus/?url=ur&action=settings&name=[COLOR white][B]SETTINGS[/B][/COLOR]&description",35,art + 'ezmaintenanceplus.png')


def LILI1():



        addDir3('[COLOR aqua]ההרחבות שלי[/COLOR]',"addons://user/",35,'https://is4-ssl.mzstatic.com/image/thumb/Purple122/v4/a0/1d/74/a01d74df-ef1e-e77f-b665-8a7910200829/source/512x512bb.jpg')

        addDir3('[COLOR aqua]התעדכן לאחרונה[/COLOR]',"addons://recently_updated/",35,'https://is4-ssl.mzstatic.com/image/thumb/Purple122/v4/a0/1d/74/a01d74df-ef1e-e77f-b665-8a7910200829/source/512x512bb.jpg')
        addDir3('[COLOR aqua]עדכונים זמינים[/COLOR]',"addons://outdated/",35,'https://cdn.iconscout.com/icon/premium/png-512-thumb/kodi-4-975805.png')
        addDir3('[COLOR aqua]חיפוש[/COLOR]',"addons://search/",35,'https://raw.githubusercontent.com/OpenELEQ/Style/master/MetalliQ/default/search.png')

        addDir3('[COLOR aqua]התקנה ממאגר הרחבות[/COLOR]',"addons://repos/",35,'https://tekcompare.com/wp-content/uploads/2018/12/iconfinder_623_Cloud_game_online_streaming_video_4017696-1-1200x1200.png')

        addDir3('[COLOR aqua]הרחבות וידאו[/COLOR]',"addons://user/xbmc.addon.video/",35,'DefaultAddonVideo.png')
        addDir3('[COLOR aqua]הרחבות מוזיקה[/COLOR]',"addons://user/xbmc.addon.audio/",35,'DefaultAddonMusic.png')

        addDir3('[COLOR aqua]הרחבות תוכנות[/COLOR]',"addons://user/xbmc.addon.executable/",35,'DefaultAddonProgram.png')

        addDir3('[COLOR aqua]לקוח טלוויזיה חיה[/COLOR]',"addons://user/xbmc.pvrclient/",35,'DefaultAddonPVRClient.png')

        addDir3('[COLOR aqua]מאגר הרחבות[/COLOR]',"addons://user/xbmc.addon.repository/",35,'DefaultAddonRepository.png')

        addDir3('[COLOR aqua]שינוי מעטפת[/COLOR]',"addons://user/xbmc.gui.skin/",35,'DefaultAddonSkin.png')

def shadow():

        addDir3('[COLOR aqua]כניסה להרחבה[/COLOR]',"plugin://plugin.video.shadow",35,art + 'shadow.png')
        addDir3('[COLOR aqua]shadow(סרטים)[/COLOR]',"plugin://plugin.video.shadow/?data=%20&dates=%20&description=Movies&eng_name=%20&episode=%20&fanart=https%3a%2f%2ftownsquare.media%2fsite%2f295%2ffiles%2f2019%2f12%2f2020-movies-collage.jpg%3fw%3d980%26q%3d75&fav_status=false&heb_name=%20&iconimage=https%3a%2f%2fcdn1.vectorstock.com%2fi%2f1000x1000%2f22%2f75%2flogo-slate-board-for-shooting-movies-vector-4692275.jpg&id=%20&image_master&isr=0&last_id&mode=2&name=%d7%a1%d7%a8%d7%98%d7%99%d7%9d&original_title=%20&season=%20&show_original_year=%20&tmdbid=%20&url=www",35,art + 'shadow.png')
        addDir3('[COLOR aqua]shadow(סדרות)[/COLOR]',"plugin://plugin.video.shadow/?data=%20&dates=%20&description=TV&eng_name=%20&episode=%20&fanart=https%3a%2f%2fcdn.mos.cms.futurecdn.net%2fqCD39X4DjbpgxD7ZFW63eG.jpg&fav_status=false&heb_name=%20&iconimage=https%3a%2f%2fimage.shutterstock.com%2fimage-vector%2ftv-television-electronic-media-logo-260nw-1138807478.jpg&id=%20&image_master&isr=0&last_id&mode=3&name=%d7%a1%d7%93%d7%a8%d7%95%d7%aa&original_title=%20&season=%20&show_original_year=%20&tmdbid=%20&url=www",35,art + 'shadow.png')
        addDir3('[COLOR aqua]חיפוש-סרט[/COLOR]',"plugin://plugin.video.shadow/?data=%20&dates=%20&description=Tmdb&eng_name=%20&episode=%20&fanart=http%3a%2f%2fwww.videomotion.co.il%2fwp-content%2fuploads%2fwhatwedo-Pic-small.jpg&fav_status=false&heb_name=%20&iconimage=https%3a%2f%2fcellcomtv.cellcom.co.il%2fglobalassets%2fcellcomtv%2fcontent%2fsratim%2fpets-secret-life%2f480x543-template.jpg&id=%20&image_master&isr=0&last_id&mode=14&name=%d7%97%d7%99%d7%a4%d7%95%d7%a9%20%d7%a1%d7%a8%d7%98&original_title=%20&season=%20&show_original_year=%20&tmdbid=%20&url=http%3a%2f%2fapi.themoviedb.org%2f3%2fsearch%2fmovie%3fapi_key%3d34142515d9d23817496eeb4ff1d223d0%26query%3d%25s%26language%3dhe%26append_to_response%3dorigin_country%26page%3d1",35,'https://raw.githubusercontent.com/OpenELEQ/Style/master/MetalliQ/default/search.png')
        addDir3('[COLOR aqua]חיפוש-סדרה[/COLOR]',"plugin://plugin.video.shadow/?data=%20&dates=%20&description=TMDB&eng_name=%20&episode=%20&fanart=http%3a%2f%2ff.frogi.co.il%2fnews%2f640x300%2f010170efc8f.jpg&fav_status=false&heb_name=%20&iconimage=http%3a%2f%2fimg.wcdn.co.il%2ff_auto%2cw_700%2ct_18%2f1%2f0%2f7%2f2%2f1072572-46.jpg&id=%20&image_master&isr=0&last_id&mode=14&name=%d7%97%d7%99%d7%a4%d7%95%d7%a9&original_title=%20&season=%20&show_original_year=%20&tmdbid=%20&url=http%3a%2f%2fapi.themoviedb.org%2f3%2fsearch%2ftv%3fapi_key%3d34142515d9d23817496eeb4ff1d223d0%26query%3d%25s%26language%3dhe%26page%3d1",35,'https://raw.githubusercontent.com/OpenELEQ/Style/master/MetalliQ/default/search.png')



def Dgllll():
        addDir3('[COLOR aqua]VOD-11 [/COLOR]',"plugin://plugin.video.idanplus/?iconimage=C%253A%255CUsers%255CUser%255CAppData%255CRoaming%255CKodi%255Caddons%255Cplugin.video.idanplus%255Cresources%255Cimages%255Ckan.jpg&mode=1&module=kan&moredata=%25D7%259B%25D7%2590%25D7%259F%2b11&name=%5bB%5d%d7%9b%d7%9c%20%d7%94%d7%aa%d7%95%d7%9b%d7%a0%d7%99%d7%95%d7%aa%5b%2fB%5d&url=https%253A%252F%252Fwww.kan.org.il%252Fpage.aspx%253FlandingpageId%253D1039",35,art + 'kan.jpg')
        addDir3('[COLOR aqua]VOD-12 [/COLOR]',"plugin://plugin.video.idanplus/?iconimage=C%253A%255CUsers%255CUser%255CAppData%255CRoaming%255CKodi%255Caddons%255Cplugin.video.idanplus%255Cresources%255Cimages%255Cvod.jpg&mode=1&module=keshet&moredata&name=%5bB%5d%d7%aa%d7%9b%d7%a0%d7%99%d7%95%d7%aa%20MakoTV%5b%2fB%5d&url=http%253A%252F%252Fwww.mako.co.il%252Fmako-vod-index",35,art + 'keshet.jpg')
        addDir3('[COLOR aqua]VOD-13 [/COLOR]',"plugin://plugin.video.idanplus/?iconimage=C%253A%255CUsers%255CUser%255CAppData%255CRoaming%255CKodi%255Caddons%255Cplugin.video.idanplus%255Cresources%255Cimages%255C13.png&mode=0&module=reshet&moredata&name=%5bB%5d%d7%9b%d7%9c%20%d7%94%d7%aa%d7%9b%d7%a0%d7%99%d7%95%d7%aa%5b%2fB%5d&url",35,art + '13.png')
        addDir3('[COLOR aqua]VOD-23 [/COLOR]',"plugin://plugin.video.idanplus/?iconimage=C%253A%255CUsers%255CUser%255CAppData%255CRoaming%255CKodi%255Caddons%255Cplugin.video.idanplus%255Cresources%255Cimages%255C23tv.jpg&mode=1&module=kan&moredata&name=%5bB%5d%d7%9b%d7%90%d7%9f%20%d7%97%d7%99%d7%a0%d7%95%d7%9b%d7%99%d7%aa%2023%5b%2fB%5d&url=https%253A%252F%252Fwww.kan.org.il%252Fpage.aspx%253FlandingPageId%253D1083",35,art + '23.jpg')

def Dglll():
        addDir3('[COLOR aqua]חיפוש במי יוטיוב [/COLOR]',"plugin://plugin.video.MyYoutube/kodion/search/input/?description=חיפוש&fanart= &iconimage= &mode=4&name=חיפוש&url=www",35,art + 'ysearch.png')
        addDir3('[COLOR aqua]חיפוש ביוטיוב [/COLOR]',"plugin://plugin.video.youtube/kodion/search/input/",35,art + 'ysearch.png')
        addDir3('[COLOR aqua]חם ברשת(מי יוטיוב) [/COLOR]',"plugin://plugin.video.MyYoutube/?description=הסרטונים החמים&fanart&iconimage&mode=2&name=הסרטונים החמים&url=https://www.youtube.com//feed/trending",35,art + 'flame-512.png')
        addDir3('[COLOR aqua]כניסה להרחבת יוטיוב [/COLOR]',"plugin://plugin.video.youtube",35,art + 'youtube.png')

def Dgll():


        addDir('[COLOR aqua]בילד [/COLOR]','url',192919291009,'https://retropie.org.uk/forum/assets/uploads/files/1512013693768-kodi.png')
        addDir('[COLOR aqua]חיפוש בהרחבות [/COLOR]','url',1929,'http://intellectual-property.co.il/wp-content/uploads/2015/05/Perspective-Button-Search-icon.png')
        addDir('[COLOR aqua]shadowכניסה ל [/COLOR]','url',20015,art + 'shadow.png')
        addDir3('[COLOR aqua]THE CREWכניסה ל  [/COLOR]',"plugin://plugin.video.thecrew",35,'https://www.wirelesshack.org/wp-content/uploads/2020/03/How-To-Install-The-Crew-Kodi-Addon.jpg')

        addDir3('[COLOR aqua]Elementumכניסה ל  [/COLOR]',"plugin://plugin.video.elementum/",35,art + 'Elementum.png')
        addDir3('[COLOR aqua]Thorrentכניסה ל  [/COLOR]',"plugin://plugin.video.torrent",35,'https://res-4.cloudinary.com/crunchbase-production/image/upload/c_lpad,h_256,w_256,f_auto,q_auto:eco/v1500302210/ihbu4znuw8heie4j7ad3.png')
        addDir3('[COLOR aqua]ערוצי עידן [/COLOR]',"plugin://plugin.video.idanplus/?iconimage=C%253A%255CUsers%255CUser%255CAppData%255CRoaming%255CKodi%255Caddons%255Cplugin.video.idanplus%255Cicon.png&mode=1&module&moredata&name=%5bB%5d%d7%98%d7%9c%d7%95%d7%99%d7%96%d7%99%d7%94%5b%2fB%5d&url",35,art + 'i+.png')
        addDir3('[COLOR aqua]רדיו עידן [/COLOR]',"plugin://plugin.video.idanplus/?iconimage=C%253A%255CUsers%255CUser%255CAppData%255CRoaming%255CKodi%255Caddons%255Cplugin.video.idanplus%255Cicon.png&mode=3&module&moredata&name=%5bB%5d%d7%a8%d7%93%d7%99%d7%95%5b%2fB%5d&urll",35,art + 'i+.png')
        addDir('[COLOR aqua]עידן VOD [/COLOR]','url',1930,art + 'i+.png')

        addDir('[COLOR aqua]סדרות טיוי [/COLOR]','url',1941948080,art + 'sdar.png')
        addDir3('[COLOR aqua]כניסה לטלמדיה [/COLOR]',"plugin://plugin.video.telemedia",35,art + 'tel.png')



        addDir3('[COLOR aqua]כניסה לMovix live [/COLOR]',"plugin://plugin.video.movixws",35,art + 'movixws.png')
        addDir('[COLOR aqua]יוטיוב [/COLOR]','url',1931,art + 'youtube.png')


        addDir3('[COLOR aqua]המעודפים שלי [/COLOR]',"plugin://script.skin.helper.widgets/?action=favourites&mediatype",35,'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTGifA4RM62yA5Gd5puJd5hYEKNToughMg75mNFuFpm-CfaR_cL')
        addDir3('[COLOR green]ניקוי קודי [/COLOR]',"plugin://script.program.Chamelon_cleaner",35,'https://reviewvpn.com/wp-content/uploads/2019/08/How-to-Clear-Cache-on-Kodi-750x500.png')
        addDir('[B][COLOR green]תחזוקה [/COLOR][/B]','url',20016,art + 'ezmaintenanceplus.png')

        addDir('[B][COLOR green]תחזוקה-כללי [/COLOR][/B]','url',20008,'https://p7.hiclipart.com/preview/175/230/518/plug-in-computer-icons-add-on-wordpress-kodi-wordpress.jpg')

        addDir3('[B][COLOR red]כבוי לקודי [/COLOR][/B]',"plugin://plugin.close.kodi/?description&fanart=i\addons\plugin.close.kodi\fanart.jpg&iconimage=\addons\plugin.close.kodi\resources\art\force.png&mode=4&name=Insta Kill (Warning Kills The MediaCenter Instantly)&url=fclose",35,'https://www.ivid.it/blog/wp-content/uploads/2018/03/cropped-ivid-promo-512x512.jpg')


def sdarottv():
        addDir3('[COLOR aqua]כניסה לסדרות טיוי [/COLOR]',"plugin://plugin.video.sdarot.tv",35,art + 'sdar.png')
        addDir3('[COLOR aqua]ילדים [/COLOR]',"plugin://plugin.video.sdarot.tv/genre/38/0",35,art + 'sdar.png')
        addDir3('[COLOR aqua]חפש סדרה [/COLOR]',"plugin://plugin.video.sdarot.tv/search/0",35,art + 'sdar.png')














def PlayLkids238787y():
        addDir3('[COLOR aqua]חם ברשת [/COLOR]',"plugin://plugin.video.youtube/special/popular_right_now/",35,art + 'flame-512.png')
        addDir3('[COLOR aqua]חפש ביוטיוב [/COLOR]',"plugin://plugin.video.youtube/kodion/search/input/",35,art + 'ysearch.png')
        addDir3('[COLOR aqua]חי ביוטיוב [/COLOR]',"plugin://plugin.video.youtube/special/live/",35,'https://d1csarkz8obe9u.cloudfront.net/posterpreviews/live-stream-logo-design-template-734b190682052e1a5f76a413c7f751ba_screen.jpg')
        addDir3('[COLOR aqua]הגדרות ליוטיוב [/COLOR]',"plugin://plugin.video.youtube/config/youtube/",35,'https://www.norebbo.com/wp-content/uploads/2011/05/youtube_settings.jpg')










def PlayLkids233y():
        addDir('[B][COLOR aqua]  •[/COLOR][/B][B][COLOR white]ת [/COLOR][/B][B][COLOR aqua]ו [/COLOR][/B][B][COLOR white]ר [/COLOR][/B][B][COLOR aqua]י [/COLOR][/B][B][COLOR white]ש [/COLOR][/B][B][COLOR aqua] •[/COLOR][/B]','url',194,art + 'Serviceil.png')

        addDir('[COLOR aqua]ערוצים בקליק [/COLOR]','url',7777776,'https://cdn.imgbin.com/5/7/10/imgbin-adam-sandler-click-film-poster-michael-newman-adam-sandler-6D9Ka94946DkP4diMLBF2CkPH.jpg')
        addDir('[COLOR aqua]סרטים בקליק [/COLOR]','url',7777777,'https://cdn.imgbin.com/5/7/10/imgbin-adam-sandler-click-film-poster-michael-newman-adam-sandler-6D9Ka94946DkP4diMLBF2CkPH.jpg')

        addDir('[COLOR aqua]קטגוריות ליוטיוב [/COLOR]','url',987652002122456,'https://st2.depositphotos.com/3554337/6639/i/950/depositphotos_66393627-stock-photo-golden-play-icon.jpg')
        addDir('[COLOR aqua]סרטים [/COLOR]','url',9876538,art + 'movies.png')
        addDir('[COLOR aqua]ילדים [/COLOR]','url',9876512,art + 'kids.png')
        addDir('[COLOR aqua]מוזיקה [/COLOR]','url',9876513,art + 'Music.png')
        addDir('[COLOR aqua]ספורט [/COLOR]','url',9876515,art + 'Sports.png')
        addDir('[COLOR aqua]עולם הקודי [/COLOR]','url',20038,art + 'images.jfif')
        addDir('[COLOR aqua]סטנדאפ [/COLOR]','url',9876598,art + 'su.jpg')
        addDir('[COLOR aqua]דוקומנטרי [/COLOR]','url',9876511,art + 'documentary.jpg')
        addDir('[COLOR aqua]דת ומדינה [/COLOR]','url',9876510000,'https://upload.wikimedia.org/wikipedia/commons/8/8c/Judaismo.jpg')
        addDir('[COLOR aqua]בריאות + [/COLOR]','url',987659009,art + 'bn.png')
        addDir('[COLOR aqua]טיולים [/COLOR]','url',9876514,art + 'travel.png')
        addDir('[COLOR aqua]יוטיוב פופלרי-IL [/COLOR]','url',20036,'https://yt3.ggpht.com/a/AATXAJwHom-ZsNmJGLXTS_LobC-xZ649Y0pkQS8Djg=s100-c-k-c0xffffffff-no-rj-mo')



def YouKODI2():





        addDir3('[B][COLOR aqua]סרטונים כלליים [/COLOR][/B]',"plugin://plugin.video.youtube/kodion/search/query/?q=KODI &search_type=playlist/?page=1",35,art + 'images.jfif')

        addDir3('[COLOR aqua]VPNRanks [/COLOR]',"plugin://plugin.video.youtube/channel/UC9Ll3FoujcdMb46GEkJ4lYg/?page=1",35,art + 'images.jfif')
        addDir3('[COLOR aqua]Electric MD [/COLOR]',"plugin://plugin.video.youtube/channel/UC-k3qiN7j63HpKjEYoa6zMQ/?page=1",35,art + 'images.jfif')
        addDir3('[COLOR aqua]KODI CANAL [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=KODI CANAL&search_type=playlist",35,art+ 'images.jfif')
   
        addDir3('[COLOR aqua]Chris Caserta [/COLOR]',"plugin://plugin.video.youtube/channel/UCAgTLyhnm3P38W8nWHJc0Xg/?page=1",35,art + 'images.jfif')
     
        addDir3('[COLOR aqua]GoJoe Productions [/COLOR]',"plugin://plugin.video.youtube/channel/UCr6_FEDtv7vwsm1C1GImTYA/?page=1",35,art + 'images.jfif')

        addDir3('[COLOR aqua]NO ISSUE [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=KODI NO ISSUE&search_type=playlist",35,art+ 'images.jfif')

        addDir3('[COLOR aqua]ocanalonline [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=ocanalonline",35,art + 'images.jfif')

        addDir3('[COLOR aqua]KODI ADDONS [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=KODI%20ADDONS&search_type=playlist",35,art+ 'images.jfif')



        addDir3('[COLOR aqua]MeacePeace [/COLOR]',"plugin://plugin.video.youtube/channel/UCx55aM88WDVMS-AR_q_VKUg/?page=1",35,art + 'images.jfif')
 












def Muyuy():

        addDir('[COLOR aqua]דרך (יוטיוב) [/COLOR]','url',98765199,'https://lh3.googleusercontent.com/W9bNP8huNRfwpHMxR-jHIXao_5FaOEdKLk3N0z7mr2W5ybdSEadEzDMD0qo-tNoe6A')

def Muly():


        addDir('[COLOR aqua]מוזיקה ישראלית רישמית [/COLOR]','url',98765197,art + '97.jpg')
        addDir('[COLOR aqua]עכשיו מוזיקה(חול) [/COLOR]','url',98765196,art + 'NOWMUSIC.png')
        addDir('[COLOR aqua]YOU MUSIK(חול) [/COLOR]','url',9876520018,'https://lh3.googleusercontent.com/proxy/h_b2-j76eI_USxOLmBZV-A3BtIeXIPnyZOvkuMksAdIsO3z4vevrGr5y80-VoUtjZlJlv2FT7L2uI-p8jqr_98_kH-D87xpu3QNEYcbjebMdys0IDD3Mm4I')
        addDir('[COLOR aqua]DJ WHO(חול) [/COLOR]','url',98765195,'https://yt3.ggpht.com/a/AGF-l7-zALRItOQnOaN5zwZxpE1XZyiZcdCllnN3wg=s100-c-k-c0xffffffff-no-rj-mo')
        addDir('[COLOR aqua]VEVO TUBE(חול) [/COLOR]','url',98765193,'https://yt3.ggpht.com/-AN6VHCEqvbo/AAAAAAAAAAI/AAAAAAAAAAA/4VTnH0Gva5Y/nd/photo.jpg')
        addDir('[COLOR aqua]The Best Ultimate Music Collection [/COLOR]','url',987651925,art + 'tbum.jpg')


def Slly():
        addDir3('[COLOR aqua]עדן בן זקן [/COLOR]',"plugin://plugin.video.youtube/channel/UCt927ZDEsYMJL_8PXqMiVhg/?page=1",35,art + '97.jpg')
        addDir3('[COLOR aqua]נועה קירל [/COLOR]',"plugin://plugin.video.youtube/channel/UC7sHZrh1-mdwyBLq52m1MSw/?page=1",35,art + '97.jpg')
        addDir3('[COLOR aqua]גילי ארגוב [/COLOR]',"plugin://plugin.video.youtube/channel/UCequxLNw7IOP9rwJZhOtK6w/?page=1",35,art + '97.jpg')
        addDir3('[COLOR aqua]עמיר בניון [/COLOR]',"plugin://plugin.video.youtube/channel/UCerYyxoFp9Ln-zgxvM7X_0w/?page=1",35,art + '97.jpg')
        addDir3('[COLOR aqua]אושר ביטון [/COLOR]',"plugin://plugin.video.youtube/channel/UCVKwHi_KdIyd09oO8ap3vIA/?page=1",35,art + '97.jpg')
        addDir3('[COLOR aqua]אייל גולן [/COLOR]',"plugin://plugin.video.youtube/channel/UCrI0Slej0fiiwYPhR1EmFBw/?page=1",35,art + '97.jpg')
        addDir3('[COLOR aqua]מורן מזור [/COLOR]',"plugin://plugin.video.youtube/channel/UCNAeAJ7F1tvrLX-B7N2ohfA/?page=1",35,art + '97.jpg')
        addDir3('[COLOR aqua]אדיר גץ [/COLOR]',"plugin://plugin.video.youtube/channel/UC3KqEm2Q5XjzJJfhyj3MxSw/?page=1",35,art + '97.jpg')
        addDir3('[COLOR aqua]מאור אדרי [/COLOR]',"plugin://plugin.video.youtube/channel/UCDYRaqbP0BA4E73Ywn6-eVQ/?page=1",35,art + '97.jpg')
        addDir3('[COLOR aqua]אגם בוחבוט [/COLOR]',"plugin://plugin.video.youtube/channel/UC9TW96-3a8_scwVJjo9_PbA/?page=1",35,art + '97.jpg')
        addDir3('[COLOR aqua]רגב הוד [/COLOR]',"plugin://plugin.video.youtube/channel/UCs-MmgLIZ5YSFJuBz75HdSg/?page=1",35,art + '97.jpg')
        addDir3('[COLOR aqua]ישי ריבו [/COLOR]',"plugin://plugin.video.youtube/channel/UCHwxQ7twj_VWIPMcJ3Zdyqg/?page=1",35,art + '97.jpg')
        addDir3('[COLOR aqua]עומר אדם [/COLOR]',"plugin://plugin.video.youtube/user/OmerAdamOfficial/?page=1",35,art + '97.jpg')
        addDir3('[COLOR aqua]מאיר בנאי [/COLOR]',"plugin://plugin.video.youtube/user/MeirBanai/?page=1",35,art + '97.jpg')
        addDir3('[COLOR aqua]נתן גושן [/COLOR]',"plugin://plugin.video.youtube/user/NathanGoshenOfficial/?page=1",35,art + '97.jpg')
        addDir3('[COLOR aqua]מושיק עפיה [/COLOR]',"plugin://plugin.video.youtube/user/MoshikAfiaOfficial/?page=1",35,art + '97.jpg')
        addDir3('[COLOR aqua]ליאור נרקיס [/COLOR]',"plugin://plugin.video.youtube/user/LiorNarkisOfficial/?page=1",35,art + '97.jpg')
        addDir3('[COLOR aqua]בועז שרעבי [/COLOR]',"plugin://plugin.video.youtube/user/BoazSharabiMusic/?page=1",35,art + '97.jpg')
        addDir3('[COLOR aqua]ישי לוי [/COLOR]',"plugin://plugin.video.youtube/user/IshayLeviOfficial/?page=1",35,art + '97.jpg')
        addDir3('[COLOR aqua]נסרין קדרי [/COLOR]',"plugin://plugin.video.youtube/user/NasreenQadri/?page=1",35,art + '97.jpg')
        addDir3('[COLOR aqua]ריטה [/COLOR]',"plugin://plugin.video.youtube/user/ritaofficial/?page=1",35,art + '97.jpg')
        addDir3('[COLOR aqua]שרית חדד [/COLOR]',"plugin://plugin.video.youtube/user/SaritHadadOfficial/?page=1",35,art + '97.jpg')
        addDir3('[COLOR aqua]דודו אהרון [/COLOR]',"plugin://plugin.video.youtube/user/DuduAharonOfficiaI/?page=1",35,art + '97.jpg')
        addDir3('[COLOR aqua]שלומי שבת [/COLOR]',"plugin://plugin.video.youtube/user/shlomishabatofficiaI/?page=1",35,art + '97.jpg')
        addDir3('[COLOR aqua]חיים משה [/COLOR]',"plugin://plugin.video.youtube/user/haimmosheoffical/?page=1",35,art + '97.jpg')
        addDir3('[COLOR aqua]איציק קלה [/COLOR]',"plugin://plugin.video.youtube/user/itzikalaofficial/?page=1",35,art + '97.jpg')
        addDir3('[COLOR aqua]פאר טסי [/COLOR]',"plugin://plugin.video.youtube/user/peertasimizrahi/?page=1",35,art + '97.jpg')
        addDir3('[COLOR aqua]הראל מויאל [/COLOR]',"plugin://plugin.video.youtube/user/HarelMoyalMusic/?page=1",35,art + '97.jpg')


def Sxly():
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה מוסיקה 1 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLSDFo3uefkViQiBE1boD4E1lkT-L0tval/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה מוסיקה 2 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLqf3vdDTch5eIprOE5UW22JYVeF2H3DZQ/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה מוזיקה! 3 [/COLOR]',"plugin://plugin.video.youtube/playlist/PL2BiE_4h8Tpx5gH-aLL2fPHEDIQuNdOO7/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו ככה אני מכנה מוסיקה 4 [/COLOR]',"plugin://plugin.video.youtube/playlist/playlist? list = PLC134EF07843F8E12/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני קורא מוסיקה Vol.5 [/COLOR]',"plugin://plugin.video.youtube/playlist/PL0F21A53AF61D1FB7/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני קורא מוסיקה Vol.6 [/COLOR]',"plugin://plugin.video.youtube/playlist/PL469DC54E90251585/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה מוסיקה 7 [/COLOR]',"plugin://plugin.video.youtube/playlist/PL6Z-l9iL9V02f4s7eTwOOHLICG_pMp-bi/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה מוזיקה! 8 [/COLOR]',"plugin://plugin.video.youtube/playlist/PL2BiE_4h8TpzglEey9QQK56Pk_kc0D_Ll/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני קורא מוסיקה Vol.9 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLAAB55DE564DDB852/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה מוזיקה! 10 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLGQ0UcnwJRN0vlWtPCvCddvpVv-_RJXik/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו זה מה שאני מכנה מוסיקה 11 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLe_aExlm6LzI-bHdvaznqY9HaN0uccsWY/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני קורא מוסיקה Vol.12 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLDouWbMQEftHsFyHSBua-RZLFsx--Cu4U/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה מוסיקה 13 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLP1Y3xiNAKkuhumMQUsCZocF-SaS7uIAC/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה מוזיקה! 14 [/COLOR]',"plugin://plugin.video.youtube/playlist/PL2BiE_4h8TpwA_Vs7CmADdM8TWsnmH9L8/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו זה מה שאני מכנה מוסיקה 15 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLsqB7ljSBkucly4zjjGca9PUDCvrdd4F1/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני קורא מוסיקה 16 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLP1Y3xiNAKkug6YZSWuszc3nrXMxImP0T/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה מוזיקה! 17 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLGQ0UcnwJRN2YFTPvcFdlEqPk2X50EtsC/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה מוזיקה! 18 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLsqB7ljSBkudm8Kc21ML3S8Ywwm8POK_n/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה מוזיקה! 19 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLGQ0UcnwJRN3nlqZfg3GzdnJRu7tXbDvP/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה מוזיקה! 20 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLP1Y3xiNAKkvYyHd7bmpd0B8gHTxvcYdL/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה מוסיקה 21 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLP1Y3xiNAKktUOg36k5y3pOnHh9gmoXsn/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה מוזיקה! 22 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLU2xNh0BeCUhEVLj3S78WNag9O-Hpm8ad/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה מוזיקה! 23 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLsqB7ljSBkufEHqSjQJmedoixNkWNtQBO/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני קורא מוסיקה Vol.24 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLDouWbMQEftFLmCbJNnxBqo925x89tJci/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה מוזיקה! 25 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLsqB7ljSBkuexkNUk-eaT0nS9KAZPGMD7/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה מוזיקה! 26 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLsqB7ljSBkuesJ07Bxz6eiLcIaIz7xYXv/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה מוזיקה! 27 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLsqB7ljSBkuecopwcuVGcYAJO4qvz3XA3/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה מוזיקה! 28 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLsqB7ljSBkufIxPcOdmwnxGfSRZgDGOe3/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה מוזיקה! 29 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLsqB7ljSBkucC3zgKZF3S4EiZ45PUmx-/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה מוזיקה! כרך 30 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLDouWbMQEftEEeKB6GcLaDQbypvob4e10/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה מוזיקה! 31 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLsqB7ljSBkuevnNzpL3R_p6BEV_u1r3aZ/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה מוזיקה! 32 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLsqB7ljSBkudmCDLFhy2slnXN3gVUuGrm/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה מוזיקה! 33 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLsqB7ljSBkud2zZR9oVu2XGjZ8aDNlIVX/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה מוזיקה! 34 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLsqB7ljSBkufvOUAC7Wbr5_Ik_XsnjD_X/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה מוזיקה! 35 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLsqB7ljSBkucOpSfwBvSGo-oNiGJ3ALJi/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה מוזיקה! 36 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLsqB7ljSBkufqYFkLc4cBF6CkHzDBxnYx/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה מוזיקה! 37 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLDouWbMQEftEcdNjhvM5YeVvXSl9nxOaU/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה מוזיקה! 38 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLsqB7ljSBkuex2YFNUhqHTEPU4PXMz6Gz/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה מוזיקה! 39 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLsqB7ljSBkueDzyERVqcAdh2C-aiTmBXY/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו זה מה שאני מתקשר למוזיקה 40 [/COLOR]',"plugin://plugin.video.youtube/playlist/PL1h8do6DyqVMWIR4s3ppNF64_M0y42wW2/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה מוזיקה! 41 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLsqB7ljSBkuc7rHY6_l1khV-rG_Tie81e/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה מוזיקה! 42 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLsqB7ljSBkufUxVPOQxyTkistak74Si_S/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה מוזיקה! כרך 43 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLDouWbMQEftHJSvaRvBzvFZ4S34kucnwl/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה מוזיקה! 44 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLsqB7ljSBkuehTugfSUFkeXFGbwKBcYnu/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה מוזיקה! 45 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLsqB7ljSBkueLsTNOL9vMM9QX3Vnrz-yn/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה מוזיקה! 46 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLDUAmuW0s8Whc9NXMvEtO5jFynx43OBLo/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה מוזיקה! 47 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLDouWbMQEftFtfaMjEM-9IjipNjw7qJ5W/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו זה מה שאני מתקשר למוזיקה 48 [/COLOR]',"plugin://plugin.video.youtube/playlist/PL1h8do6DyqVOBo4p_hK90IMfCIPcFQ3dx/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני קורא מוסיקה Vol.49 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLxniG6aRxGSsg3ZuNKTs7dE5VWNBche0D/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו זה מה שאני קורא מוסיקה! 51 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLhUnYSiS17hw156nLAPgoULF3Mq7_z6K-/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה מוזיקה! 52 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLGQ0UcnwJRN1i1peiUpidY8gOl6u7dGbY/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה מוזיקה! 53 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLGQ0UcnwJRN0AgPw0IWosO6eyHCmlgOjx/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה מוזיקה! 54 [/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLGQ0UcnwJRN3GZ-1DvWtyVXI_wP-XitwI/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו זה מה שאני קורא מוסיקה! 56 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLhUnYSiS17hzI0c55YCNUREsg_QLem0D2/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו זה מה שאני אאהב מוזיקה 57 [/COLOR]',"plugin://plugin.video.youtube/playlist/PL1h8do6DyqVNHVVtloq2-cOWnuWtAX87w/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה מוזיקה! 58 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLGQ0UcnwJRN2AnC0Fe49aa7Lq-QILORYh/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה מוזיקה! 59 [/COLOR]',"plugin://plugin.video.youtube/playlist/PL1F0D80E99F7850E5/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו זה מה שאני קורא מוסיקה! 60 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLhUnYSiS17hxqroAmcTp0rPZlvjlSOKQ-/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה מוזיקה! כרך 61 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLDouWbMQEftGZPWsKV2-J1Nb-bnnP1kDt/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו זה מה שאני מתקשר למוזיקה 62[/COLOR]',"plugin://plugin.video.youtube/playlist/PLDouWbMQEftEFihO_LZMovLip0mVz0Fg3/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה מוזיקה! כרך 63 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLDouWbMQEftGksuKJ-MJ8i2WwtwH-DyVe/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה מוזיקה! 64 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLDB9B7A7906FAFAB8/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו זה מה שאני מתקשר למוזיקה 65 [/COLOR]',"plugin://plugin.video.youtube/playlist/PL_34_m4eTlaOh7AX4GJRnnxKgJ5n9_V-M/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה מוזיקה! כרך א  66 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLDouWbMQEftFvmLqnvKo-Svl6QNXaD4ac/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני קורא מוסיקה 67 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLgXn-x6PNSy0QqokVgysvrcN_99cnlK1W/?page=1",35,art + 'NOWMUSIC.png')	
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה מוסיקה 68 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLgXn-x6PNSy3zxCaW4I9zxJpoNGm97dUK/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו זה אני קורא מוזיקה 69 [/COLOR]',"plugin://plugin.video.youtube/playlist/PL_34_m4eTlaP6n2tYDBKamuvoQDo89a97/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו זה מה שאני קורא מוסיקה! 70 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLfajXyIbTpnHOAqRdvINIq2ak-lFiEJvw/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו זה מה שאני קורא מוסיקה! 71 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLfajXyIbTpnHWjIRCcKyLcBorqLBnjPxc/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו זה מה שאני קורא מוזיקה 72 [/COLOR]',"plugin://plugin.video.youtube/playlist/PL_34_m4eTlaMoYI8LghIOjui2Tr8rukHp/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו זה מה שאני קורא מוסיקה! 73 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLjvJyxqOmFBJFZ8kMlpTIG63jCFwi_-cu/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני קורא מוסיקה 74 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLDouWbMQEftHqrKjdu7cFSACIudT2n5Il/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני קורא מוסיקה 75 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLjvJyxqOmFBIRjjgW0IQgRfh3cfAgANsS/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני קורא מוסיקה 76 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLDouWbMQEftHiTge92lMQFgbNVUCBlP8E/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו זה מה שאני קורא מוזיקה 77 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLziBTZqySBRFOFOwbSuPn4GtockoGot7k/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה מוזיקה! 78 [/COLOR]',"plugin://plugin.video.youtube/playlist/PL6CDBDD2A3C0D55A5/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו זה מה שאני קורא מוסיקה! 79 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLjvJyxqOmFBLVpyCD38x8RkEaYtETiBcR/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה מוסיקה 80 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLBB7D0AF873F8FAEA/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה מוזיקה! 81 [/COLOR]',"plugin://plugin.video.youtube/playlist/PL8FA9A7569EBB5E4A/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה מוזיקה! 82 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLoDgQlTbBQzYPrbsgmAJcDoD9Y33XhNJo/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו זה מה שאני מתקשר למוזיקה 83 [/COLOR]',"plugin://plugin.video.youtube/playlist/PL_34_m4eTlaOeNd6fP9MspKqh9ksDiNtm/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה מוזיקה! 84 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLwyQmbD4WPl9s1rHOfSSKUj8a86HRLUCA/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה מוזיקה! 85 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLlhDgn0Cytc26XrU4x3JDhXb9dxyt2DEa/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה מוסיקה 86 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLDg9kwdnXsO-sGrCANOR5gb44MLhLD1Er/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה מוסיקה 87 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLRmc7JLx8IJKOccrdanLLQG1s0FTaHGKH/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו זה מה שאני מתקשר למוזיקה 88 [/COLOR]',"plugin://plugin.video.youtube/playlist/PL_34_m4eTlaPzdgA9RG_BlIImsUwCVkzy/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו זה מה שאני קורא מוסיקה! 89 [/COLOR]',"plugin://plugin.video.youtube/playlist/PL_34_m4eTlaOtJMirQzXvOoAwdechWbhF/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו זה מה שאני קורא מוסיקה! 90 [/COLOR]',"plugin://plugin.video.youtube/playlist/PL_34_m4eTlaNHt6GM5dOnraJ2zdE4R2Z_/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו זה מה שאני קורא מוסיקה! 91 [/COLOR]',"plugin://plugin.video.youtube/playlist/PL_34_m4eTlaMf-42RHro2x2UVMHNEkLvD/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו זה מה שאני קורא למוזיקה 92 [/COLOR]',"plugin://plugin.video.youtube/playlist/PL_34_m4eTlaOFcXryY7OFbYGtK5Y1JoIa/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו זה מה שאני קורא מוסיקה! 93 [/COLOR]',"plugin://plugin.video.youtube/playlist/PL_34_m4eTlaN5Dj1kIzrJMX95HRBLqeQr/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו זה מה שאני קורא מוסיקה! 94 [/COLOR]',"plugin://plugin.video.youtube/playlist/PL_34_m4eTlaO0auWQxAH__sUTfRidOQZW/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו זה מה שאני קורא מוסיקה! 95 [/COLOR]',"plugin://plugin.video.youtube/playlist/NOW לזה אני קורא המנונים של המפלגה/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו זה מה שאני קורא מוסיקה! 96 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLJyQ4LyHbaraIkU1z9RzBLS2kWqAoQXH0/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו זה מה שאני קורא מוסיקה! עכשיו 97 [/COLOR]',"plugin://plugin.video.youtube/playlist/PL_34_m4eTlaPorC89EUOQxwhXeZxd-Hc7/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו זה מה שאני קורא מוסיקה! 98 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLJyQ4LyHbarYfhbtEaTk4xj9CGRlylq6I/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו זה מה שאני קורא מוסיקה! 99 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLAd5X7u2hj3dRVSJz4mrcRxfrbCZ-E4iN/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו ככה אני מכנה מוסיקה 100 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLLZStkUkKPlVCF5pqz7Ztx8lXsTpGbIf6/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו זה מה שאני קורא מוסיקה! 101 [/COLOR]',"plugin://plugin.video.youtube/playlist/PL_34_m4eTlaP8vMmdKKQpo4pm0efcwkxc/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה מוסיקה 102 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLfWOuLCdH-1dCXUN2WvV6mUiTXRpr5VmI/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו זה מה שאני קורא מוסיקה! 103 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLcn2SuWDLcXDkhAclaScxjgWqW6KHiv_m/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו זה מה שאני קורא מוסיקה! 104 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLhV4RKTkP5JQRIjQUPM5Ndr_xuF7gCF6h/?page=1",35,art + 'NOWMUSIC.png')	
        addDir3('[COLOR aqua]עכשיו זה מה שאני מכנה פופ [/COLOR]',"plugin://plugin.video.youtube/playlist/PL_34_m4eTlaNQBMQYxfxQLN7eUkIKP66y/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני קוראת 60s [/COLOR]',"plugin://plugin.video.youtube/playlist/PL2BiE_4h8TpwWwKe3i_c4pnPshJktXC92/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו זה מה שאני מכנה שנות ה -70 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLhXCO9UQq4zoIJY4qa1UA_WQWuwS-y2bc/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו זה מה שאני מכנה שנות השמונים [/COLOR]',"plugin://plugin.video.youtube/playlist/PL_34_m4eTlaMgClOUihGU5EKM0md93FCN/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו זה מה שאני מכנה שנות ה -90 [/COLOR]',"plugin://plugin.video.youtube/playlist/PL_34_m4eTlaOrcFRHD9mG4zUilcXQS8uB/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני קוראת ה- 00 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLsdPA0A_fKLmuHNuafb76kecjHqeGoBLs/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]VA - עכשיו זה מה שאני מכנה מסיבת קיץ 2019 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLCo9rIUIbahty3bDn2cUeK_fU6sYrmWnF/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה רגאיי [/COLOR]',"plugin://plugin.video.youtube/playlist/PL2BiE_4h8TpwJLR--E3-Fco9BRmEH0oq1/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו זה מה שאני מכנה המאה ה -21 [/COLOR]',"plugin://plugin.video.youtube/playlist/PL_34_m4eTlaPLkaa4gLSJsWm86Z0H8i_U/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה מדינה (2017) [/COLOR]',"plugin://plugin.video.youtube/playlist/PL2BiE_4h8TpwCSkzXEntUnMb2K8Sfl8q3/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]VA - עכשיו זה מה שאני מכנה מסיבת קיץ 2019 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLCo9rIUIbahty3bDn2cUeK_fU6sYrmWnF/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה רוק קלאסי (2015) [/COLOR]',"plugin://plugin.video.youtube/playlist/PL2BiE_4h8Tpw-9ppd1cagjhcsa6nuOByP/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה מוזיקה! 1985 (כעת סדרת יום השנה העשירית) [/COLOR]',"plugin://plugin.video.youtube/playlist/PLsqB7ljSBkufwGaYG3NFmCK9Z9dp86vb9/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו זה מה שאני קורא המנונים של המפלגה [/COLOR]',"plugin://plugin.video.youtube/playlist/PL_34_m4eTlaN0b1Wntb0io2m_j0Bbe1Id/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו: 100 צפיות: Sing-a-Long [/COLOR]',"plugin://plugin.video.youtube/playlist/PL2BiE_4h8Tpx3Ez_UdMt-n6WeamFX3bqs/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו 100 צפיות לסרטים [/COLOR]',"plugin://plugin.video.youtube/playlist/PLmMGqezX7LHW2HGwL8h3UpLtPxciLf9hO/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו: 100 צפיות: שירי מכוניות [/COLOR]',"plugin://plugin.video.youtube/playlist/PL2BiE_4h8Tpx-eImS3x2BYsxSIwqWfl7x/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]VA - NU 100 צפיות שנשכחו שנות ה -80 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLh2ZThx4HC6WSLzfH8weBzCpzCLUNDGl4/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]VA - NU 100 צפיות שנשכחו שנות ה -90 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLCo9rIUIbahs3c8qsdSzflX7xstAoJg3N/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו: 100 צפיות: משטרי כוח [/COLOR]',"plugin://plugin.video.youtube/playlist/PL2BiE_4h8Tpy37yKc8FP4HpIV6ZyR2eaZ/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו: 100 צפיות: חג המולד [/COLOR]',"plugin://plugin.video.youtube/playlist/PL2BiE_4h8Tpz00pWE68zD_Ag9PO9o903s/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה רוקנרול [/COLOR]',"plugin://plugin.video.youtube/playlist/PL2BiE_4h8TpzdcbEeANYQDnvsfXo0HHL5/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני קורא שירי אהבה (2018) [/COLOR]',"plugin://plugin.video.youtube/playlist/PL2BiE_4h8Tpz3VMIcAnTzaX5rpsvtIczX/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני קורא קל [/COLOR]',"plugin://plugin.video.youtube/playlist/PL2BiE_4h8Tpwr3V1CEDhNeKxEm6PLQwSe/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו זה מה שאני קורא דיסני 2017 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLhXCO9UQq4zosccGMdyCinFpdHvSE9Kvu/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו מה שאני קורא לאבא רוק [/COLOR]',"plugin://plugin.video.youtube/playlist/PLW_NpxKH1uD_qdX2gbvTsHVzYKvEQXGh7/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]VA - עכשיו זה מה שאני מכנה מסיבת קיץ 2019 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLCo9rIUIbahty3bDn2cUeK_fU6sYrmWnF/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו זה מה שאני קורא לו רמיקס [/COLOR]',"plugin://plugin.video.youtube/playlist/PLhXCO9UQq4zocy64nFXan7WiscyJymBDH/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה אולד סקול [/COLOR]',"plugin://plugin.video.youtube/playlist/PL2BiE_4h8TpyHnumViPWg0_enDQRotJv4/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה נשמה קלאסית [/COLOR]',"plugin://plugin.video.youtube/playlist/PL2BiE_4h8TpzvN8xfhOGPUw-SAcDa2-Ex/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו זה מה שאני מכנה זמר [/COLOR]',"plugin://plugin.video.youtube/playlist/PL_34_m4eTlaNh63gxFpUwwAROXj5V3AX8/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני קוראת ליל כל הקדושים [/COLOR]',"plugin://plugin.video.youtube/playlist/PLGQ0UcnwJRN3rMvLhns856JQoxtQtYIgf/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני קוראת אני רוצה רוק [/COLOR]',"plugin://plugin.video.youtube/playlist/PLGQ0UcnwJRN3rRVKwiNLTc1rAVrWSGEUp/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני קוראת מספר 1 (2015) [/COLOR]',"plugin://plugin.video.youtube/playlist/PLGQ0UcnwJRN2ZlwzY369IQP__M_bGRp1E/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה מוטאון [/COLOR]',"plugin://plugin.video.youtube/playlist/PLGQ0UcnwJRN0sYMpb9cKV9ct_h1Ct1YP0/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני מכנה גל חדש 80s [/COLOR]',"plugin://plugin.video.youtube/playlist/PLGQ0UcnwJRN03-63KDFnCiKaYLJsszOi_/?page=1",35,art + 'NOWMUSIC.png')
        addDir3('[COLOR aqua]עכשיו לזה אני קוראת Country Vol. 3 [/COLOR]',"plugin://plugin.video.youtube/playlist/PLGQ0UcnwJRN0sCK_zH_BoG1nd4Y_3pmJb/?page=1",35,art + 'NOWMUSIC.png')


 

def Dgly():
        addDir3('[B][COLOR coral]country music [/COLOR][/B]',"plugin://plugin.video.youtube/playlist/PLV3wO-tIt_3ECUWNSkyFH633Gnk3gluV8/?page=1",35,'https://yt3.ggpht.com/a/AGF-l7-zALRItOQnOaN5zwZxpE1XZyiZcdCllnN3wg=s100-c-k-c0xffffffff-no-rj-mo')

        addDir3('[B][COLOR coral]uncategorized [/COLOR][/B]',"plugin://plugin.video.youtube/playlist/PLV3wO-tIt_3F52OlmieJsNUd_ABn2iXZN/?page=1",35,'https://yt3.ggpht.com/a/AGF-l7-zALRItOQnOaN5zwZxpE1XZyiZcdCllnN3wg=s100-c-k-c0xffffffff-no-rj-mo')

        addDir3('[B][COLOR coral]events [/COLOR][/B]',"plugin://plugin.video.youtube/playlist/PLV3wO-tIt_3HGIQ3C_Czmc0x-JaDpFkAA/?page=1",35,'https://yt3.ggpht.com/a/AGF-l7-zALRItOQnOaN5zwZxpE1XZyiZcdCllnN3wg=s100-c-k-c0xffffffff-no-rj-mo')

        addDir3('[B][COLOR coral]Christmas [/COLOR][/B]',"plugin://plugin.video.youtube/playlist/PLV3wO-tIt_3FKhHChoGD5H6LP4jmkBPyD/?page=1",35,'https://yt3.ggpht.com/a/AGF-l7-zALRItOQnOaN5zwZxpE1XZyiZcdCllnN3wg=s100-c-k-c0xffffffff-no-rj-mo')

        addDir3('[B][COLOR coral]80/90s [/COLOR][/B]',"plugin://plugin.video.youtube/playlist/PLV3wO-tIt_3FH1ah7Rp671n63z2huFYZ2/?page=1",35,'https://yt3.ggpht.com/a/AGF-l7-zALRItOQnOaN5zwZxpE1XZyiZcdCllnN3wg=s100-c-k-c0xffffffff-no-rj-mo')

        addDir3('[B][COLOR coral]concerts [/COLOR][/B]',"plugin://plugin.video.youtube/playlist/PLV3wO-tIt_3Efj8N08eopR5NFh1dCmEt0/?page=1",35,'https://yt3.ggpht.com/a/AGF-l7-zALRItOQnOaN5zwZxpE1XZyiZcdCllnN3wg=s100-c-k-c0xffffffff-no-rj-mo')

        addDir3('[B][COLOR coral]R&B [/COLOR][/B]',"plugin://plugin.video.youtube/playlist/PLV3wO-tIt_3E3fK2NKmylEEqkRVaW9hLz/?page=1",35,'https://yt3.ggpht.com/a/AGF-l7-zALRItOQnOaN5zwZxpE1XZyiZcdCllnN3wg=s100-c-k-c0xffffffff-no-rj-mo')

        addDir3('[B][COLOR coral]karaoke [/COLOR][/B]',"plugin://plugin.video.youtube/playlist/PLV3wO-tIt_3GVT106wzYNdRoL7YbRZlT-/?page=1",35,'https://yt3.ggpht.com/a/AGF-l7-zALRItOQnOaN5zwZxpE1XZyiZcdCllnN3wg=s100-c-k-c0xffffffff-no-rj-mo')

        addDir3('[B][COLOR coral]tragically hip [/COLOR][/B]',"plugin://plugin.video.youtube/playlist/PLV3wO-tIt_3FN5M5ct_4PscMv_SL4hcGp/?page=1",35,'https://yt3.ggpht.com/a/AGF-l7-zALRItOQnOaN5zwZxpE1XZyiZcdCllnN3wg=s100-c-k-c0xffffffff-no-rj-mo')

        addDir3('[B][COLOR coral]screensavers [/COLOR][/B]',"plugin://plugin.video.youtube/playlist/PLV3wO-tIt_3EbjH5y5XlV29jowSjlNMO3/?page=1",35,'https://yt3.ggpht.com/a/AGF-l7-zALRItOQnOaN5zwZxpE1XZyiZcdCllnN3wg=s100-c-k-c0xffffffff-no-rj-mo')

        addDir3('[B][COLOR coral]cape breton kitchen party [/COLOR][/B]',"plugin://plugin.video.youtube/playlist/PLV3wO-tIt_3F4DNbag62rnJ4EOS5r2mnA/?page=1",35,'https://yt3.ggpht.com/a/AGF-l7-zALRItOQnOaN5zwZxpE1XZyiZcdCllnN3wg=s100-c-k-c0xffffffff-no-rj-mo')

        addDir3('[B][COLOR coral]motown [/COLOR][/B]',"plugin://plugin.video.youtube/playlist/PLV3wO-tIt_3HzAo-BPj2W-l9VwzxqgHCU/?page=1",35,'https://yt3.ggpht.com/a/AGF-l7-zALRItOQnOaN5zwZxpE1XZyiZcdCllnN3wg=s100-c-k-c0xffffffff-no-rj-mo')

def Suy():


        addDir3('[COLOR aqua]פלייליסט סטנדאפ(ישראלי) [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=סטנדאפ פלייליסט&search_type=playlist",35,art + 'su.jpg')
        addDir3('[COLOR aqua]פלייליסט סטנדאפ(עולמי) [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=stand%20up%20comedy&search_type=playlist/?page=1",35,art + 'su.jpg')
        addDir3('[COLOR aqua]יוחאי ספונדר [/COLOR]',"plugin://plugin.video.youtube/channel/UC-9wDB8k1WRfMKnHk3XW4Qw/?page=1",35,'https://www.castilia.co.il/CastiliaWebLink/1864/get.resource/images/1037/1000037.png')
        addDir3('[COLOR aqua]אסף מור יוסף [/COLOR]',"plugin://plugin.video.youtube/channel/UCgeTKxv1HBBXkIiarKx9IpA/?page=1",35,'https://yt3.ggpht.com/a/AGF-l79bQVL0lppUBVYPeGPn0kfdxoZ1LuSmEWs-qA=s800-mo-c-c0xffffffff-rj-k-no')
        addDir3('[COLOR aqua]צמד שיניים [/COLOR]',"plugin://plugin.video.youtube/channel/UCcCQ4nMLzDXmVPLO6O-CAsA/?page=1",35,'http://www.comedybar.co.il/pictures/show_big_0344740001450951166.jpg')
        addDir3('[COLOR aqua]קומדי בר [/COLOR]',"plugin://plugin.video.youtube/channel/UCVbCUgpl_9DA0iUsS_rkIbQ/?page=1",35,'https://yt3.ggpht.com/a/AGF-l7_W6sfJ7YNDcq-haZ2e8nCn140ga4yyZDAI7g=s176-c-k-c0x00ffffff-no-rj-mo')
        addDir3('[COLOR aqua]טדי קטעים פה [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=ערוץ טדי&search_type=playlist",35,'https://blog.partner.co.il/wp-content/uploads/2017/10/kolaj-1000x500.jpg')
        addDir3('[COLOR aqua]נאור ציון [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=נאור ציון&search_type=playlist",35,art + 'su.jpg')	 
        addDir3('[COLOR aqua]הצגות מרוקאיות [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=הצגות מרוקאיות&search_type=playlist",35,art + 'su.jpg')
        addDir3('[COLOR aqua]מני עוזרי [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=מני עוזרי&search_type=playlist",35,art + 'su.jpg')
        addDir3('[COLOR aqua]בן בן ברוך [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=בן בן ברוך&search_type=playlist",35,art + 'su.jpg')
        addDir3('[COLOR aqua]ישראל קטורזה [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=ישראל קטורזה&search_type=playlist",35,art + 'su.jpg')
        addDir3('[COLOR aqua]שלום אסייג [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=שלום אסייג&search_type=playlist",35,art + 'su.jpg')
        addDir3('[COLOR aqua]יוסי פנסו [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=יוסי פנסו&search_type=playlist",35,art + 'su.jpg')
        addDir3('[COLOR aqua]יוסי גבני [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=יוסי גבני&search_type=playlist",35,art + 'su.jpg')
        addDir3('[COLOR aqua]אלי ומריאנו [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=אלי ומריאנו&search_type=playlist",35,art + 'su.jpg')
        addDir3('[COLOR aqua]הרצועה [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=הרצועה&search_type=playlist",35,art + 'su.jpg')
        addDir3('[COLOR aqua]נדב אבוקסיס [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=נדב אבוקסיס&search_type=playlist",35,art + 'su.jpg')
        addDir3('[COLOR aqua]שחר חסון [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=שחר חסון&search_type=playlist",35,art + 'su.jpg')
        addDir3('[COLOR aqua]אודי כגן [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=אודי כגן&search_type=playlist",35,art + 'su.jpg')
        addDir3('[COLOR aqua]שלשיית מה קשור [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=שלשיית מה קשור&search_type=playlist",35,art + 'su.jpg')
        addDir3('[COLOR aqua]ירון ברלד סטנדאפ [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=ירון ברלד סטנדאפ&search_type=playlist",35,art + 'su.jpg')
        addDir3('[COLOR aqua]שלישיית פרוזק [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=שלישיית פרוזק&search_type=playlist",35,art + 'su.jpg')




        

def vevy():
        addDir3('[COLORred]VEVO[/COLOR] [COLORwhite]US Kanal[/COLOR]',"plugin://plugin.video.youtube/user/VEVO/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoUS.png')
        addDir3('[COLORred]VEVO[/COLOR] [COLORwhite]DE Kanal[/COLOR]',"plugin://plugin.video.youtube/user/deutschlandVEVO/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoDE.png')
        addDir3('[COLORred]VEVO[/COLOR] [COLORwhite]UK Kanal[/COLOR]',"plugin://plugin.video.youtube/user/VEVOUK/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoUK.png')
        addDir3('[COLORred]VEVO[/COLOR] [COLORwhite]FR Kanal[/COLOR]',"plugin://plugin.video.youtube/user/VevoFranceOfficiel/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoFR.png')
        addDir3('[COLORred]VEVO[/COLOR] [COLORwhite]NL Kanal[/COLOR]',"plugin://plugin.video.youtube/user/VEVONederland/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoNL.png')
        addDir3('[COLORred]VEVO[/COLOR] [COLORwhite]ES Kanal[/COLOR]',"plugin://plugin.video.youtube/user/VEVOEspana/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoES.png')
        addDir3('[COLORred]VEVO[/COLOR] [COLORwhite]IT Kanal[/COLOR]',"plugin://plugin.video.youtube/user/VEVOIT/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoIT.png')
        addDir3('[COLORred]VEVO[/COLOR] [COLORwhite]PL Kanal[/COLOR]',"plugin://plugin.video.youtube/user/VEVOPolska/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoPL.png')
        addDir3('[COLORred][B]What´s Hot[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFu8MzzbNVtUvHs0cQ_gZ03m/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoCharts.png')
        addDir3('[COLORred][B]Hot this Week[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFtx71frwf8cxXXhW0YEG3xF/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoCharts.png')
        addDir3('[COLORred][B]Top 20[/B][/COLOR] [COLORwhite]Videos in the US[/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFuTq2RLA0DhevkZYp954-k4/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoCharts.png')
        addDir3('[COLORred][B]Top 20[/B][/COLOR] [COLORwhite]New Artist Videos in the US[/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFuHBYGM1iEL6OUyiA4BsvrZ/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoCharts.png')
        addDir3('[COLORred][B]Top 10[/B][/COLOR] [COLORwhite]Pop Videos[/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFv8JKRhQtU4elLD73E3kvvo/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoCharts.png')
        addDir3('[COLORred][B]Top 10[/B][/COLOR] [COLORwhite]Alternative Videos[/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFvHFiFhJhaqyRAHkX7ewSRk/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoCharts.png')
        addDir3('[COLORred][B]Top 10[/B][/COLOR] [COLORwhite]Alternative Videos of 2018[/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFtZeu9JzS4O7m6HvGFYqhCu/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoCharts.png')
        addDir3('[COLORred][B]Top 10[/B][/COLOR] [COLORwhite]Country Videos[/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFu712crop5LYYzvxm_aY4Yi/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoCharts.png')
        addDir3('[COLORred][B]Top 10[/B][/COLOR] [COLORwhite]Country Videos of 2018[/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFvuDwJjlGWLjtLgIdlKW4YG/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoCharts.png')
        addDir3('[COLORred][B]Top 10[/B][/COLOR] [COLORwhite]EDM Videos[/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFuVbKK_q7An7AGK_sBovNbm/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoCharts.png')
        addDir3('[COLORred][B]Top 10[/B][/COLOR] [COLORwhite]EDM Videos of 2018[/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFsO6z9aLV540RcbIQSDsbMP/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoCharts.png')
        addDir3('[COLORred][B]Top 10[/B][/COLOR] [COLORwhite]Hip-Hop Videos[/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFs8J2ySTyV8aW9ZDwT-f2KE/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoCharts.png')
        addDir3('[COLORred][B]Top 10[/B][/COLOR] [COLORwhite]Hip-Hop Videos of 2018[/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFtxXjd3Klm7cDmqXCxyY9b0/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoCharts.png')
        addDir3('[COLORred][B]Top 10[/B][/COLOR] [COLORwhite]Indie Videos[/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFtJHsp-bsHZH3jxLa08rDya/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoCharts.png')
        addDir3('[COLORred][B]Top 10[/B][/COLOR] [COLORwhite]Indie Videos of 2018[/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFuEOGsquQgnbxQQ6d9W2aKu/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoCharts.png')
        addDir3('[COLORred][B]Top 10[/B][/COLOR] [COLORwhite]Latin Videos[/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFuz1RSdd0ua9EHdQSJecALm/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoCharts.png')
        addDir3('[COLORred][B]Top 10[/B][/COLOR] [COLORwhite]Latin Videos of 2018[/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFuVuLIQoV8aOHArPfZbxLV2/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoCharts.png')
        addDir3('[COLORred][B]Top 10[/B][/COLOR] [COLORwhite]Metal Videos[/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFunVZhgJ9IREhr73C2amsLz/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoCharts.png')
        addDir3('[COLORred][B]Top 10[/B][/COLOR] [COLORwhite]Metal Videos of 2018[/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFvuqteD3p7vAgUIyPbGBjGK/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoCharts.png')
        addDir3('[COLORred][B]Top 10[/B][/COLOR] [COLORwhite]R&B Videos[/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFuJMY7OjmKmhtOEcegCY6C6/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoCharts.png')
        addDir3('[COLORred][B]Top 10[/B][/COLOR] [COLORwhite]R&B Videos of 2018[/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFvvFxqFhboitegq_lVPgb18/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoCharts.png')
        addDir3('[COLORred][B]Top 10[/B][/COLOR] [COLORwhite]Rock Videos[/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFuvha_x5OEnmpYpfK-AtuTp/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoCharts.png')
        addDir3('[COLORred][B]Top 10[/B][/COLOR] [COLORwhite]Rock Videos of 2018[/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFudLBYO_ZSU-8Rjv29JIYh_/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoCharts.png')
        addDir3('[COLORwhite]All New[/COLOR] [COLORred][B]ALTERNATIVE[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFsez6cjXAxHTruW0jteUHQk/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoNewGenre.png')
        addDir3('[COLORwhite]Kickin´ New[/COLOR] [COLORred][B]COUNTRY[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFtUu1HrxtZ4hv8nNLKiRseN/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoNewGenre.png')
        addDir3('[COLORwhite]New[/COLOR] [COLORred][B]EDM[/B][/COLOR] [COLORwhite]Beats[/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFvBK4oJZylITMXRxAPJvbr8/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoNewGenre.png')
        addDir3('[COLORwhite]Hot New[/COLOR] [COLORred][B]HIP-HOP[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFv-V7FvZP-PWuE-1x2Deqqe/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoNewGenre.png')
        addDir3('[COLORwhite]All New[/COLOR] [COLORred][B]INDIE[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFvXYAx7RjMQd6h7_URtCwoK/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoNewGenre.png')
        addDir3('[COLORwhite]Nuevo Pop[/COLOR] [COLORred][B]LATINO[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFtps6SqgQYfMoMk557f2VAk/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoNewGenre.png')
        addDir3('[COLORwhite]Malicious New[/COLOR] [COLORred][B]METAL[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFuErwY_it1HO20Da-13FfNz/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoNewGenre.png')
        addDir3('[COLORwhite]Nuevo Regional[/COLOR] [COLORred][B]MEXICANO[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFun6Q71-e4lgwHigs0EbSfd/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoNewGenre.png')
        addDir3('[COLORwhite]New[/COLOR] [COLORred][B]R&B[/B][/COLOR] [COLORwhite]Vibes[/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFupYyrDriLYu3ba9oYMUJ65/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoNewGenre.png')
        addDir3('[COLORwhite]Rugged New[/COLOR] [COLORred][B]ROCK[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFvrS_oXmav-as9fy3lt1i34/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoNewGenre.png')
        addDir3('[COLORwhite]Brand New[/COLOR] [COLORred][B]POP[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFt2TyOofWG0XwA8IDC8SGIN/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoNewGenre.png')
        addDir3('[COLORwhite]Los Rompe Tarima[/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFvRr9wRh1o8oeIpkPUdAjV6/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoNewGenre.png')
        addDir3('[COLORred][B]Fresh Music[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFuiE7QFMzvaTuhXleCaAc52/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoGenre.png')
        addDir3('[COLORred][B]Afro Beat[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFufJOabZGuV93QVdZzouWyc/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoGenre.png')
        addDir3('[COLORred][B]Dancehall Delights[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFu9k1UqFdWffUtMyeNbwAYw/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoGenre.png')
        addDir3('[COLORred][B]Dance Pop Hits[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFtynbPGh-GPxTsCGAW35GgW/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoGenre.png')
        addDir3('[COLORred][B]Dad Rock[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFvsOFNUeME8BSbiH_PwQGOK/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoGenre.png')
        addDir3('[COLORred][B]Electro Alt/Indie[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFtWjRRwOK_D_RO2kv0yU3mx/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoGenre.png')
        addDir3('[COLORred][B]Extrem Metal[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFv-fsLsz-1RaVdKeBPp5o28/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoGenre.png')
        addDir3('[COLORred][B]Grown Folk R&B[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFtgtiMbBi64rRudSIMFg-d8/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoGenre.png')
        addDir3('[COLORred][B]Heavy Spitters[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFs14BsetzaXkYUo-Nx6WRG7/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoGenre.png')
        addDir3('[COLORred][B]Hear it Now: Country![/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFtU-Y58frRg2nENqyZLYuzj/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoGenre.png')
        addDir3('[COLORred][B]Indie Pop[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFtG6Vx47mZFpr56Wfty30FJ/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoGenre.png')
        addDir3('[COLORred][B]Island Vibes[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFtU-Y58frRg2nENqyZLYuzj/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoGenre.png')
        addDir3('[COLORred][B]Latin Trendsetters[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFsfDtWiBJ4j7YyDINWIiHpq/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoGenre.png')
        addDir3('[COLORred][B]Nuevo Sabor Tropical[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFtVmU7eZa84X1s7EmaUaeI5/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoGenre.png')
        addDir3('[COLORred][B]Old 2 the New[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFuF8lJd_OZwQsWMrKMCEgIB/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoGenre.png')
        addDir3('[COLORred][B]Organic Alt/Indie[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFsrB_M5iGi2ww3vCTVVyjZW/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoGenre.png')
        addDir3('[COLORred][B]Pure Pop[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFvKRiSw23TNP68fIrUblrWH/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoGenre.png')
        addDir3('[COLORred][B]Pop Teen[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFvxjdtw3Iy4LsyhXeCt_P44/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoGenre.png')
        addDir3('[COLORred][B]Riddim Nation[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFvF0nBYvE8vKSlWsGssAydq/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoGenre.png')
        addDir3('[COLORred][B]Roots Reggae[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFtd2_FhMAWoiMW0r5X-Sveo/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoGenre.png')
        addDir3('[COLORred][B]Soca Hits[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFsmprDH-i2yeq1z8OwiFzDu/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoGenre.png')
        addDir3('[COLORred][B]Teen Hip-Hop and R&B[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFvHLl17Tm2-fyhwDBnecahx/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoGenre.png')
        addDir3('[COLORred][B]Trap Stars[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFuSozSTGO7dibrhaDg6qRq2/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoGenre.png')
        addDir3('[COLORred][B]This One s For The Girls[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFspwjv96-6Vanlik6v2vRz0/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoGenre.png')
        addDir3('[COLORred][B]UK Represent[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFsi4M0yYHy4KL-UBVfCmq3G/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoGenre.png')
        addDir3('[COLORwhite]Love it Live:[/COLOR] [COLORred][B]COUNTRY[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFuLQIXnp6BrHTYaGF0w4dY-/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoLive.png')
        addDir3('[COLORwhite]Love it Live:[/COLOR] [COLORred][B]INDIE[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFtVyHzilNNbDeI5UkWa1hZ8/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoLive.png')
        addDir3('[COLORwhite]Love it Live:[/COLOR] [COLORred][B]HIP-HOP[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFvz5YcFommSYF-iCrZj6nhE/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoLive.png')
        addDir3('[COLORwhite]Love it Live:[/COLOR] [COLORred][B]METAL[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFvSPe7p4oCziGKb8yMm2D8a/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoLive.png')
        addDir3('[COLORwhite]Love it Live:[/COLOR] [COLORred][B]R&B[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFtKOKmHyEgagZOOsed6bLGp/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoLive.png')
        addDir3('[COLORwhite]Love it Live:[/COLOR] [COLORred][B]ROCK[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFseh1MIXV1gsrU_h_1Pc_mo/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoLive.png')
        addDir3('[COLORwhite]Love it Live:[/COLOR] [COLORred][B]POP[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFseUoJd-4NUu042RuQ0PUfi/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoLive.png')
        addDir3('[COLORwhite]Live Performances[/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFvtAbH4_z7IEaSYAHrNW8Wo/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoLive.png')
        addDir3('[COLORwhite]DSCVR - All Live Performances[/COLOR]',"plugin://plugin.video.youtube/playlist/PLfpWqf0Dq32_xD4HttGXuLkM-QfSoWBvW/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoLive.png')
        addDir3('[COLORwhite]LiveSets @ The Great Escape Festival 2018[/COLOR]',"plugin://plugin.video.youtube/playlist/PL7KLwyJCC7QyKJoYKgfo8l7VkrkKkyjRq/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoLive.png')
        addDir3('[COLORred][B]COUNTRY[/B][/COLOR] [COLORwhite]Party Playlist[/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFv8hIun4ujGj0RF66Ogb-vf/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoMoods.png')
        addDir3('[COLORred][B]EDM[/B][/COLOR] [COLORwhite]Party Playlist[/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFvxJlU0eH71A4nkP1O1HsUo/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoMoods.png')
        addDir3('[COLORred][B]HIP-HOP[/B][/COLOR] [COLORwhite]In the Gym[/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFtZk0J0MsWkajC3139aQ2wy/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoMoods.png')
        addDir3('[COLORred][B]HIT[/B][/COLOR] [COLORwhite]the Gym[/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFuXtvZQsoJYw3PTZjCN8CCZ/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoMoods.png')
        addDir3('[COLORred][B]R&B[/B][/COLOR] [COLORwhite]Party Playlist[/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFv4jC7qf3u38KNpvv2SOkJR/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoMoods.png')
        addDir3('[COLORred][B]ROMANCE[/B][/COLOR] [COLORwhite]Rockero[/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFs5owDVo-lHb6QgCA0ZL3Jk/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoMoods.png')
        addDir3('[COLORred][B]POP[/B][/COLOR] [COLORwhite]Party Playlist[/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFvz9SFKucMbmBt-SnZtokVY/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoMoods.png')
        addDir3('[COLORred][B]Pop Outta Bed[/B][/COLOR] [COLORwhite]- Music With Your Coffee[/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFukDT2wdYkXwSZqg8HsH73q/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoMoods.png')
        addDir3('[COLORred][B]The Breakfast Club[/B][/COLOR] [COLORwhite]- Morning Music[/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFtfwzVHdLt_nJwt9Iv7qoD7/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoMoods.png')
        addDir3('[COLORred][B]CHILLOUT[/B][/COLOR] [COLORwhite]- Lazy Morning[/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFtROKI2bqQdOGNWgmRWsKNv/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoMoods.png')
        addDir3('[COLORred][B]Mellow Out[/B][/COLOR] [COLORwhite]- Low Key Afternoon[/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFul67nuDgHNojFAt1IPjiIC/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoMoods.png')
        addDir3('[COLORred][B]Midnight Chill[/B][/COLOR] [COLORwhite]- Sleepy Head[/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFugJqfmiNpXMRop_swcsXHZ/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoMoods.png')
        addDir3('[COLORred][B]Crushin On You[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFuo2kolkJmA_Th0sUC_mLtW/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoMoods.png')
        addDir3('[COLORred][B]Hoy Se Bebe[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFs2is-Fji_wHWtfO_-Rko2x/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoMoods.png')
        addDir3('[COLORred][B]Late Registration[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFtvZUAUKlYLfS74PyTgJqo4/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoMoods.png')
        addDir3('[COLORwhite]Incoming[/COLOR] [COLORred][B]ALTERNATIVE[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFt_H0qxBMqqQonj83vaKDbF/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoPlaylist.png')
        addDir3('[COLORwhite]Incoming[/COLOR] [COLORred][B]COUNTRY[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFtftz_53w-VnY9kYz8bC66w/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoPlaylist.png')
        addDir3('[COLORwhite]Incoming[/COLOR] [COLORred][B]EDM[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFubH8RSGxdBDwhf7g4C60Vy/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoPlaylist.png')
        addDir3('[COLORwhite]Incoming[/COLOR] [COLORred][B]HIP-HOP[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFvN_9mCk7b8h33NrlxiPTx1/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoPlaylist.png')
        addDir3('[COLORwhite]Incoming[/COLOR] [COLORred][B]INDIE[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFsFhx7JRa8pbMVIExlLYNah/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoPlaylist.png')
        addDir3('[COLORwhite]Incoming[/COLOR] [COLORred][B]METAL[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFuFHvOwsadSCn3NKeuNIh0B/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoPlaylist.png')
        addDir3('[COLORwhite]Incoming[/COLOR] [COLORred][B]R&B[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFvSkAtT0DUEffzC5mi7hUOl/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoPlaylist.png')
        addDir3('[COLORwhite]Incoming[/COLOR] [COLORred][B]ROCK[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFtva3fYalscaRiMVc9C6EES/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoPlaylist.png')
        addDir3('[COLORwhite]Incoming[/COLOR] [COLORred][B]POP[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFuIC3udROGYMT_M4f39x4BW/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoPlaylist.png')
        addDir3('[COLORwhite]DSCVR[/COLOR] [COLORred][B]ALTERNATIVE[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFuZjjpuZMhh7KC-Sw6aehjA/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoDSCVR.png')
        addDir3('[COLORwhite]DSCVR[/COLOR] [COLORred][B]COUNTRY[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFs8XbSARCWThNqt5YXhCOHu/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoDSCVR.png')
        addDir3('[COLORwhite]DSCVR[/COLOR] [COLORred][B]EDM[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFsGFJ6dh8R6AExOhIYljnjp/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoDSCVR.png')
        addDir3('[COLORwhite]DSCVR[/COLOR] [COLORred][B]HIP-HOP[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFt5tsGbHhlAVX7KDM4WpMYC/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoDSCVR.png')
        addDir3('[COLORwhite]DSCVR[/COLOR] [COLORred][B]INDIE[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFuwFi1wSueeFR-7MdKn5xM-/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoDSCVR.png')
        addDir3('[COLORwhite]DSCVR[/COLOR] [COLORred][B]LATINO[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFtd5iXVx_m6tSyyJZskY3xf/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoDSCVR.png')
        addDir3('[COLORwhite]DSCVR[/COLOR] [COLORred][B]METAL[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFsl7Hqzq6VeI7rWskr4lb37/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoDSCVR.png')
        addDir3('[COLORwhite]DSCVR[/COLOR] [COLORred][B]R&B[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFvlIjnD63Q8WJdzN_Sa94kp/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoDSCVR.png')
        addDir3('[COLORwhite]DSCVR[/COLOR] [COLORred][B]ROCK[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFsQ42vFCS-PhDg--aPyh9R7/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoDSCVR.png')
        addDir3('[COLORwhite]DSCVR[/COLOR] [COLORred][B]POP[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFtbNWZwYMO7HLlH58DcVJoi/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoDSCVR.png')
        addDir3('[COLORred][B]ALTERNATIVE[/B][/COLOR] [COLORwhite]Replay[/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFu2G9yrUTQaq34OGlENR7Dw/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoReplay.png')
        addDir3('[COLORred][B]COUNTRY[/B][/COLOR] [COLORwhite]Replay[/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFsO4BWeXMvfFJuwXONeMRAJ/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoReplay.png')
        addDir3('[COLORred][B]EDM[/B][/COLOR] [COLORwhite]Replay[/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFspK-zf2PoWqP6NJYflkM-B/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoReplay.png')
        addDir3('[COLORred][B]INDIE[/B][/COLOR] [COLORwhite]Replay[/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFs5S8Hy6amKBeKuGq2CMxCv/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoReplay.png')
        addDir3('[COLORred][B]METAL[/B][/COLOR] [COLORwhite]Replay[/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFvruwh6bTrU_X1Yn7aCvwtZ/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoReplay.png')
        addDir3('[COLORred][B]RAP[/B][/COLOR] [COLORwhite]Replay[/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFtb-K_G-Uv-FgKNFuT2KSBW/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoReplay.png')
        addDir3('[COLORred][B]R&B[/B][/COLOR] [COLORwhite]Replay[/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFvP58E91WStRnOPTxSTTgC7/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoReplay.png')
        addDir3('[COLORred][B]ROCK[/B][/COLOR] [COLORwhite]Replay[/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFt8kH1xUjp9mmrUMTG3qt1I/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoReplay.png')
        addDir3('[COLORred][B]POP[/B][/COLOR] [COLORwhite]Replay[/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFsuscmwmqh96nRKLrVM8BOy/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoReplay.png')
        addDir3('[COLORred][B]POP[/B][/COLOR] [COLORwhite]Mix 2018>2015[/COLOR]',"plugin://plugin.video.youtube/playlist/PL7KLwyJCC7QzpNciVGe-7K6ShC3MzL3vd/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoMix.png')
        addDir3('[COLORred][B]DANCE/ELECTRO[/B][/COLOR] [COLORwhite]Mix 2018>2015[/COLOR]',"plugin://plugin.video.youtube/playlist/PL7KLwyJCC7QyXUZLdnHDbBIjBZZSOFRKk/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoMix.png')
        addDir3('[COLORred][B]INDIE/ROCK/ALTERNATIVE[/B][/COLOR] [COLORwhite]Mix 2018>2015[/COLOR]',"plugin://plugin.video.youtube/playlist/PL7KLwyJCC7Qx3UC8uj-qLIsOdd5OmkNHY/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoMix.png')
        addDir3('[COLORred][B]Interviews[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFtf0OfrhrX05vWJlddRR_AW/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoMeets.png')
        addDir3('[COLORred][B]VEVO Meets[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFvxtE1BaLe2s4EHqRxqNEdx/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoMeets.png')
        addDir3('[COLORred][B]60Seconds with...[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9tY0BWXOZFuUNkhmRYHLQjc5wOjKNU_Z/?page=1",35,'http://sgkodi.de/VEVO/Daten/VevoMeets.png')

def kidsy():
        addDir('[COLOR aqua]ילדודס[/COLOR]','PL3432ABAC840E3DF3',9876520020,art + 'kids.png')
        addDir('[COLOR aqua]נוסטלגיה חינוכית[/COLOR]','url',9876520000,art + '23.jpg')   
     
        addDir3('[COLOR aqua]הצגות לילדים [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=הצגות לילדים&search_type=playlist",35,art + 'kids.png')
        addDir3('[COLOR aqua]סרטים לילדים מדובב + מתורגם [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=סרטים לילדים מדובב + מתורגם&search_type=playlist",35,art + 'kids.png')
        addDir3('[COLOR aqua]קלטות לילדים [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=קלטות לילדים&search_type=playlist",35,art + 'kids.png')
        addDir3('[COLOR aqua]יובל המבולבל[/COLOR]','plugin://plugin.video.youtube/kodion/search/query/?q=%d7%99%d7%95%d7%91%d7%9c%20%d7%94%d7%9e%d7%91%d7%95%d7%91%d7%9c',35,art + '30022.png')
        addDir3('[COLOR aqua]ערוץ כוכבי הילדים[/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=ערוץ כוכבי הילדים&search_type=playlist",35,'https://yt3.ggpht.com/a/AATXAJwqCO6o62V5YrWzEpXl4PCDL0uJCkbFBwrX0g=s288-c-k-c0xffffffff-no-rj-mo')
        addDir3('[COLOR aqua]דוד חיים [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=דוד חיים&search_type=playlist",35,art + '30024.jpg')
        addDir3('[COLOR aqua]מיכל הקטנה[/COLOR]','plugin://plugin.video.youtube/kodion/search/query/?q=%d7%9e%d7%99%d7%9b%d7%9c%20%d7%94%d7%a7%d7%98%d7%a0%d7%94',35,art + '30027.jpg')
        addDir3('[COLOR aqua]רינת [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=רינת&search_type=playlist",35,art + '30028.jpg')
        addDir3('[COLOR aqua]פסטיגל [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=פסטיגל&search_type=playlist",35,art + '30029.jpg')
        addDir3('[COLOR aqua]מופעי קרקס[/COLOR]','plugin://plugin.video.youtube/kodion/search/query/?q=full%20circus%20show',35,art + 'kids.png')
		
        addDir('[COLOR aqua]ערוץ גוניור[/COLOR]','PL3432ABAC840E3DF3',20022,art + '30030.jpg')
        addDir('[COLOR aqua]ניק גוניור[/COLOR]','PL3432ABAC840E3DF3',20023,art + '30031.jpg')
        addDir('[COLOR aqua]ניקלודאון[/COLOR]','PL3432ABAC840E3DF3',20024,art + '30032.jpg')
        addDir('[COLOR aqua]לוגי[/COLOR]','PL3432ABAC840E3DF3',20025,art + '30033.jpg')
        addDir('[COLOR aqua]הופ[/COLOR]','PL3432ABAC840E3DF3',20026,art + 'hop.png')
        addDir('[COLOR aqua]הופ ילדות ישראלית[/COLOR]','PL3432ABAC840E3DF3',20027,art + 'hopy.jpg')
        addDir('[COLOR aqua]לולי[/COLOR]','PL3432ABAC840E3DF3',20028,art + 'luly.jpg')
        addDir('[COLOR aqua]בייבי[/COLOR]','PL3432ABAC840E3DF3',20029,art + 'baby.jpg')
        addDir('[COLOR aqua]הוט ילדים[/COLOR]','PL3432ABAC840E3DF3',20030,art + 'HOTVOD.png')
        addDir('[COLOR aqua]ערוץ הילדים[/COLOR]','PL3432ABAC840E3DF3',20031,art + 'kidstv.png')
        addDir('[COLOR aqua]ערוץ זום[/COLOR]','PL3432ABAC840E3DF3',20032,art + 'zoom.jpg')
        addDir('[COLOR aqua]דיסני גוניור[/COLOR]','PL3432ABAC840E3DF3',20033,art + 'dsjr.jpg')	
        addDir('[COLOR aqua]סדרות נוסטלגיות[/COLOR]','PL3432ABAC840E3DF3',20034,art + 'kids.png')	
        addDir3('[COLOR aqua]לימוד קסמים לילדים [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=לימוד קסמים לילדים&search_type=playlist",35,art + 'kids.png')	
        addDir3('[COLOR aqua]יצירה לילדים [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=יצירה לילדים&search_type=playlist",35,art + 'kids.png')
        addDir3('[COLOR aqua]אוריגמי לילדים [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=אוריגמי לילדים&search_type=playlist",35,art + 'kids.png')

def moviesy():
        addDir('[COLOR aqua] סרטים וסדרות (חול)[/COLOR]','url',987657899,art + 'movies.png')
        addDir('[COLOR aqua] סרטים וסדרות-2 (חול)[/COLOR]','url',9876520014,art + 'movies.png')
        addDir('[COLOR aqua]טריילרים [/COLOR]','url',9876510005,'https://yt3.ggpht.com/-l0S3cJpdAXI/AAAAAAAAAAI/AAAAAAAAAAA/OmClcgO7WyI/nd/photo.jpg')
        addDir3('[COLOR aqua]סרטים דוקומנטרים [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=סרטים דוקומנטרים&search_type=playlist",35,art + 'documentary.jpg')
        addDir3('[COLOR aqua]סרטים ישראליים [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=סרטים ישראליים&search_type=playlist",35,art + 'movies.png')
        addDir3('[COLOR aqua]סרטים מתורגמים[/COLOR]','plugin://plugin.video.youtube/kodion/search/query/?q=%d7%a1%d7%a8%d7%98%20%d7%9e%d7%aa%d7%95%d7%a8%d7%92%d7%9d%20%d7%9e%d7%9c%d7%90',35,art + 'movies.png')
        addDir3('[COLOR aqua]סרטים לילדים [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=סרטים לילדים&search_type=playlist",35,art + 'movies.png')



def nostalgiay():
        addDir('[COLOR aqua]חינוכית-תוכניות עבר[/COLOR]','url',9876520001,art + '23.jpg')
        addDir('[COLOR aqua]חינוכית-ילדים נוסטלגיה[/COLOR]','url',9876520002,art + '23.jpg')
        addDir('[COLOR aqua]חינוכית-ילדים[/COLOR]','url',9876520003,art + '23.jpg')
        addDir('[COLOR aqua]חינוכית-תוכניות משודרות[/COLOR]','url',9876520004,art + '23.jpg')
        addDir('[COLOR aqua]חינוכית-לומדים מהבית[/COLOR]','url',9876520005,art + '23.jpg')
        addDir('[COLOR aqua]חינוכית-מוזיקה[/COLOR]','url',9876520006,art + '23.jpg')
        addDir('[COLOR aqua]חינוכית-ספיישלים[/COLOR]','url',9876520007,art + '23.jpg')
        
        
def nostalgia1y():	
 
        addDir3('[COLOR aqua]לאן יהודים לאן[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL45D145EEFF323EF1/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]עברית בסימנטוב[/COLOR]'+translate(830057)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj7z_fK_Sklm-S0MADQVS-Zh/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]פגישה עם סופר[/COLOR]'+translate(830021)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj6c9WpeMqBRHuMMLdARsOIl/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]מה פתאום[/COLOR]'+translate(830021)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj6Y8TPlvSP29SBEK2YzX6UC/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]דנידינה[/COLOR]'+translate(830021)+'',"plugin://plugin.video.youtube/playlist/PL2ZWSou1jCkgRRhmqqRmz_jIiSCoxnOhI/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]שרתי לך ארצי[/COLOR]'+translate(830021)+'',"plugin://plugin.video.youtube/playlist/PLLttfoK87AdUxzLIyhq070W9fe8uSQT9h/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]גם אנו שופטים[/COLOR]'+translate(830022)+'',"plugin://plugin.video.youtube/playlist/PL2ZWSou1jCkgO2tjJ_b6f54jNfh5yxA1w/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]אנחנו[/COLOR]'+translate(830023)+'',"plugin://plugin.video.youtube/playlist/PL2ZWSou1jCkg65bHddf6_uUgMRVQuQqom/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]אין בעיה עם דודו טופז[/COLOR]'+translate(830023)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj4tQNSa0P2f18xxVyA-G11x/?page=1",35,art + '23.jpg')    

        addDir3('[COLOR aqua]דבי בבית חולים[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj7XhtXmAGGejgA8d8xk2m11&index=3/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]ניקוי ראש[/COLOR]'+translate(830021)+'',"plugin://plugin.video.youtube/playlist/PLLttfoK87AdWkaAQTs1ddlhdhooBk26Bh/?page=1",35,art + '23.jpg')

        addDir3('[COLOR aqua] זהו זה - מערכונים קצרים [/COLOR]',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj6YNFu1RaXRrKl4wYAB1YZ1/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]ציפיטפוט[/COLOR]'+translate(830025)+'',"plugin://plugin.video.youtube/playlist/PL2ZWSou1jCki_l6pMqE3vm2yR4cqWbJql/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]הדוברמן החברמן[/COLOR]'+translate(830026)+'',"plugin://plugin.video.youtube/playlist/PL2ZWSou1jCkhoiIsQ5ulJpCrERP5YhaCh/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]שעת כושר[/COLOR]'+translate(830027)+'',"plugin://plugin.video.youtube/playlist/PL2ZWSou1jCkj0xW8htgeJfvoaVSSFQjaR/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]האיים אבודים[/COLOR]'+translate(830021)+'',"plugin://plugin.video.youtube/playlist/PLRpSOtNcr-nFtxYRjAbXMYbZuTUetlhQA/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]עוד סיפור[/COLOR]'+translate(830028)+'',"plugin://plugin.video.youtube/playlist/PL2ZWSou1jCkiQuXZHFU3PWXgC4J6eYiKM/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]ציפי בלי הפסקה[/COLOR]'+translate(830029)+'',"plugin://plugin.video.youtube/playlist/PLozcTjklgUYyG9WCyBJ5tM7wXjSNZZ-4Z/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]בתיה עוזיאל[/COLOR]'+translate(830030)+'',"plugin://plugin.video.youtube/playlist/PL2ZWSou1jCkjpRRbW0Zg6dNiZns-o4H2J/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]מה זאת אומרת[/COLOR]'+translate(830031)+'',"plugin://plugin.video.youtube/playlist/PL2ZWSou1jCkgOkSv-pa40tjYGssr80YFu/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]השעה שלנו[/COLOR]'+translate(830032)+'',"plugin://plugin.video.youtube/playlist/PL2ZWSou1jCkj-zlc79D6PAbtJ1c83_8Tz/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]שניים אוחזין[/COLOR]'+translate(830034)+'',"plugin://plugin.video.youtube/playlist/PL2ZWSou1jCkjCG6X8Aojp_aQYLisBccE6/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]שובו של השריף[/COLOR]'+translate(830035)+'',"plugin://plugin.video.youtube/playlist/PL2ZWSou1jCkhp6_5CNAQLg1QT6YCdPA64/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]משדרי הביולוגיה הראשונים[/COLOR]'+translate(830036)+'',"plugin://plugin.video.youtube/playlist/PL2ZWSou1jCkhp6_5CNAQLg1QT6YCdPA64/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]מושגי יסוד ביהדות[/COLOR]'+translate(830037)+'',"plugin://plugin.video.youtube/playlist/PL2ZWSou1jCkjalPrmfZC9WbAisTau4uez/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]יוצא מן הכלל[/COLOR]'+translate(830038)+'',"plugin://plugin.video.youtube/playlist/PL2ZWSou1jCkg-ni4Rf2VElyCYlNXbkCAJ/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]דלת הקסמים[/COLOR]'+translate(830039)+'',"plugin://plugin.video.youtube/playlist/PL2ZWSou1jCkjj231haFQyE787KZce7I-T/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]דן ועדנה[/COLOR]'+translate(830040)+'',"plugin://plugin.video.youtube/playlist/PL2ZWSou1jCkgBMfVqgq_yX98dEd39BGIs/?page=1",35,art + '23.jpg')

        addDir3('[COLOR aqua]בולבול הקבולבול[/COLOR]'+translate(830041)+'',"plugin://plugin.video.youtube/playlist/PL2ZWSou1jCkj2medujsVWr6DiBQrEvQHz/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]רואים 6/6[/COLOR]'+translate(830042)+'',"plugin://plugin.video.youtube/playlist/PL2ZWSou1jCkii5mQfIWt8BaEl8PwF41z9/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]קרובים קרובים[/COLOR]'+translate(830043)+'',"plugin://plugin.video.youtube/playlist/PL2ZWSou1jCkgAney3rJgsJa0V4yhYbUDG/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]פיצוחים[/COLOR]'+translate(830044)+'',"plugin://plugin.video.youtube/playlist/PL2ZWSou1jCkjPV9ILga3udm6D27M0VXtI/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]סולו[/COLOR]'+translate(830045)+'',"plugin://plugin.video.youtube/playlist/PL2ZWSou1jCkjMzXLDwfW2fB6Dm35N_fGz/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]מסך לספרות[/COLOR]'+translate(830046)+'',"plugin://plugin.video.youtube/playlist/PL2ZWSou1jCkiC1s6pEIlWjK0B72WrMUNn/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]חשבון פשוט[/COLOR]'+translate(830047)+'',"plugin://plugin.video.youtube/playlist/PL2ZWSou1jCkj0GMbiBn0u_dCJRIhttNTT/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]השריף מגבעות הוליווד[/COLOR]'+translate(830048)+'',"plugin://plugin.video.youtube/playlist/PL2ZWSou1jCkjXLj9ZTCsUY3ET0sJXr0YN/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]Police file[/COLOR]'+translate(830050)+'',"plugin://plugin.video.youtube/playlist/PL2ZWSou1jCkhjLsA5QY3VstqDI6RakBkP/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]Mission: Possible[/COLOR]'+translate(830051)+'',"plugin://plugin.video.youtube/playlist/PL2ZWSou1jCkh6APhNV4AUmzzd_kY53ctS/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]ארץ מולדת[/COLOR]'+translate(830052)+'',"plugin://plugin.video.youtube/playlist/PL2ZWSou1jCkjYnhH2VTX6nE6LzYFxHnKs/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]Signal CQ Calling[/COLOR]'+translate(830054)+'',"plugin://plugin.video.youtube/playlist/PL2ZWSou1jCkgi_a2X8IAdmLfrG5_cOAq5/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]Neighbours[/COLOR]'+translate(830055)+'',"plugin://plugin.video.youtube/playlist/PL2ZWSou1jCkioehq3dj0z9qmZed9Qe7G-/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]Here we are[/COLOR]'+translate(830057)+'',"plugin://plugin.video.youtube/playlist/PL2ZWSou1jCkiUbjMohokWFVTB2TJZjg7v/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]Radio Fever[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL6A9E9B129E1AB41C/?page=1",35,art + '23.jpg')

        addDir3('[COLOR aqua]השריף מגבעות הוליווד[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL2ZWSou1jCkjXLj9ZTCsUY3ET0sJXr0YN/?page=1",35,art + '23.jpg')

 
        addDir3('[COLOR aqua]בבית של פיסטוק[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PLXBg2muL3FT4ZFhIwUSIK4Je6A36NhRJU/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]קריאת כיוון[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PL9771858B87C51F9F/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]קשת וענן[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj6qcpdP7e44dNj7xHuwd3oo/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]בלי סודות[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PL8651FB75A99093FE/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]עניין של זמן - העונה הראשונה[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PLiRWC7Q54GipZ7KO8jtKlLzIQM3klZ49t/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]עניין של זמן - כל העונות[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj6ALaQJ0c7eF_Pb9WXUoQ-I/?page=1",35,art + '23.jpg')
 
        addDir3('[COLOR aqua]עשרים פלוס - כל העונות[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj7hNn37mL60Dkhck-md70nR/?page=1",35,art + '23.jpg')

        addDir3('[COLOR aqua]חצי המנשה[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PLrrGhNe9FN6vie1pyq13mudHgDo9lgQuc/?page=1",35,art + '23.jpg')




        addDir3('[COLOR aqua]אסכולה[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj4NUt_gtD2AA6tD5zWXmO3g/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]שבעים פנים[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj4_euQ9QLSONWvFbmGjoSJc&index=9/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]קשר משפחתי[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj4qMe3mNyJ8W38Y157LLPjh/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]מי בחלילית[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj58DIAef8lhaUVAirMrZFdz/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]אופרה אחרת[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj6m5hbuhGYPLxFBsN-qD-Mj&index=4/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]זהירות ציפי בדרכים[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj4ZsfObFMOLKpQP22c9Qizt/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]אכפת לי[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj40wYDFVEnd7-PxuLDmfGd6/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]ארצנו הקטנטונת[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj5pd5gBisAd4eV9h266ari2/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]סופי לעת עתה[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PLB7C7C77FF944FF70&index=2/?page=1",35,art + '23.jpg')


        addDir3('[COLOR aqua]מוצ"ש - ספי ריבליו[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PLiRWC7Q54Giq86kHcJGInrW7WgEKWjt29/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]לא כולל שירות[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PLLttfoK87AdXQM9BaWjichoLYzHSMftJ4/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]חיים זה לא הכל [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=חיים זה לא הכל/?page=1",35,'https://upload.wikimedia.org/wikipedia/he/thumb/b/b1/LoAkol.jpg/220px-LoAkol.jpg')



 

        
def kids99y():
        addDir3('[COLOR aqua]ארתור - עונה ראשונה[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL-NIkmWdkQcJJe1RKjovNkMeEu648jbnI/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]ארתור - עונה שנייה[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PLJ9grwuaPAHpABj-ikIM6-FAEaYWY-TJL&index=42/?page=1",35,art + '23.jpg')

        addDir3('[COLOR aqua]רחוב סומסום[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL6NZo0IGsGDez_WBnUBb-cQmoYeQZTDqt/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]פרפר נחמד[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj7XTzORdSrWpgCfF1x7ZUeK/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]פרפר נחמד - פרקים חדשים[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj48eZZD9HC7x-y8qFYP9cc3/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]פרפר נחמד - מיטב השירים[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj45OPEXI-ibfJy8ON0k1ARh/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]רגע עם דודלי[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PLxvTjxfH2MJUXei9-6yCqx_r432-ZDiDh/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]מועדון החתול שמיל[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PLiRWC7Q54GipEz1Em790vHMgb0nRsz1bi/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]בסוד העניינים[/COLOR]'+translate(830062)+'',"plugin://plugin.video.youtube/playlist/PL99855780F1F601D0/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]גברת פלפלת[/COLOR]'+translate(830062)+'',"plugin://plugin.video.youtube/playlist/PLAg97dIi1Ajgf6f35OblbwVhb6w4duxwY/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]נילס הולגרסון[/COLOR]'+translate(830062)+'',"plugin://plugin.video.youtube/playlist/PLkIu9Av21tnFCbwKjYCa5_mb5iGKfy1QL/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]הלב-מרקו[/COLOR]'+translate(830062)+'',"plugin://plugin.video.youtube/playlist/PLwXEsK85wc0OGtVFt-5kEiQN6s3Qlu62a/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]עליסה בארץ הפלאות[/COLOR]'+translate(830062)+'',"plugin://plugin.video.youtube/playlist/PLwXEsK85wc0MhPZOPkLqi4dsACdBg3hE8/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]היה היה (האדם)[/COLOR]'+translate(830062)+'',"plugin://plugin.video.youtube/playlist/PL7s3QxO6wm48st6XALJqSP1iQHbd4ghGW/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]היה היה (החיים)[/COLOR]'+translate(830062)+'',"plugin://plugin.video.youtube/playlist/PL2mji1CY01QQrP_3JrC8U1uO7nS1-WlzD/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]חוש חש הבלש-אנגלית[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PLcnOogeoQ4TrfP9mO57AQY543KTLaTl8N/?page=1",35,art + '23.jpg')
 
        addDir3('[COLOR aqua]אגדות אחים גרים - עונה ראשונה[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PLYlrzbISBfkuyDzUwktkKJ8ecy-RZ3AHI/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]אגדות אחים גרים - עונה שנייה[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PLYlrzbISBfktPBUHxCckXbRxD6KkCapzu/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]טוב טוב הגמד[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL3mToa_H_f8JYsozlj7y9VdRzRaAfJZ4i/?page=1",35,art + '23.jpg')


        addDir3('[COLOR aqua]הקוסם מארץ עוץ[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PLIcHuikEGUEYNvMoOpK2L44skNC8QYGSJ/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]סנדוקאן [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=סנדוקאן/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]שאלתיאל קוואק [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=שאלתיאל קוואק&search_type=playlist",35,art + '23.jpg')
        addDir3('[COLOR aqua]שאלתיאל קוואק - עונה שנייה[/COLOR]'+translate(830062)+'',"plugin://plugin.video.youtube/playlist/PLZIgNCxEpVtGDv8g4o6E9BSGlT4ekMi12/?page=1",35,art + '23.jpg')


        addDir3('[COLOR aqua]המומינים [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q= המומינים&search_type=playlist",35,art + '23.jpg')

        addDir3('[COLOR aqua]פינוקיו[/COLOR]'+translate(830062)+'',"plugin://plugin.video.youtube/playlist/PLwXEsK85wc0OQV1DgaY4zC0_CiB8ZD5j9/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]טאו-טאו[/COLOR]'+translate(830062)+'',"plugin://plugin.video.youtube/playlist/PLwXEsK85wc0OMTKgRKShDXO73wEv4B-c9/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]הדרדסים[/COLOR]'+translate(830062)+'',"plugin://plugin.video.youtube/playlist/PLig2mjpwQBZkgIgp6HwDRJjRkRNdnFV-l/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]קופיקו - עונה ראשונה[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PLR7DTcU2p0QhDzYbbniDNwSbXUM_p6N3f/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]קופיקו - עונה שנייה[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PLR7DTcU2p0QgEdLPHhrhKtxElvYVrseAQ/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]קופיקו - עונה שלישית[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PLMq11W2eqQKQ2bcTcccLG_simyR0SXZP-/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]קופיקו - עונה רביעית[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PLchPUqk2BZjE4b0MbRBYhctCWZn-YtI8B/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]בארץ הקטקטים[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL_tnw-Uo_Oo6gcJ0M1jx0gPtc_weGF1Ke/?page=1",35,art + '23.jpg')
 
        addDir3('[COLOR aqua]בולי איש השלג[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PLiRWC7Q54Gip5kGOgoyCfQefdluYQHNXU/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]המחסן של כאילו[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PLrrGhNe9FN6tYFur9XejlsKCib684_w2E/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]פיטר פן[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PLsGURLmGZrQvXIxhnyxqMDeQHw80TAdt8/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]שוטרים וגנבים[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PLp2vc3iwGlwRfC_bnuAHA1FuaxCKyDtHP/?page=1",35,art + '23.jpg')

        addDir3('[COLOR aqua]קוסמים קטנים[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PLiRWC7Q54GipQWO9JCV8jw5Oh537ppA4L/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]היי בינבה[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PLKhumFgo_zE6hiSHG1IniVbGcJ1rlBLvG/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]אוטובוס הקסמים [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=אוטובוס הקסמים &search_type=playlist",35,art + '23.jpg')
        addDir3('[COLOR aqua]הופה היי[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PLiRWC7Q54Giqp7xe6q_a6bXf6I6ANfrKI/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]פופאי הסרט ומדודבבים [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=פופאי הסרט המלא מדובב&search_type=playlist",35,art + '23.jpg')
        addDir3('[COLOR aqua]הופה היי[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PLiRWC7Q54Giqp7xe6q_a6bXf6I6ANfrKI/?page=1",35,art + '23.jpg')


def Broadcast99y(): 
        addDir3('[COLOR aqua]שבט צוצלת [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=שבט צוצלת&search_type=playlist",35,art + '23.jpg')

        addDir3('[COLOR aqua]אחשלירוח [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=אחשלירוח&search_type=playlist",35,art + '23.jpg')


        addDir3('[COLOR aqua]23 דקות[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj7QDpAtcFy1_-Zf-OUgBFQ1/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]אחלה יום[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PL8AE904EF143BA340/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]אוכל למחשבה[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PLiRWC7Q54Gio3eCzoFAsGLz83HT40QUCZ/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]אומרים שהיה פה[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj7BNSE3BoiW-hALYC_dATQn/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]אם לא עכשיו[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj4TtM4X_skUjtbZPNn8Xttj/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]ארוחות שעשו היסטוריה[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj5eW1B7rkqAoU1GmfFHFwWv/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]הידעת?[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj6L43UJSC2LfBcxxZYx4Wj4/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]הבימה מערכה שניה[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj5R3jFtctL01mBjcjO17hvJ/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]העפרון הכי מחודד[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj7tzWxrWGNdyK-gbs1d8qf8/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]ואקום - עונה ראשונה[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj6ij1PPVnvJG9mliQNrDT_h/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]ואקום - עונה שנייה[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj4EcYSIWN-zM8vmmFktDXF5/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]חדר 101 [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=חדר 101/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]חוצה ישראל - עם קובי מידן[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PL127E7734AE7476DD/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]חותם אישי[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj5klM0RPo1k7J5iDS6otYG8/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]חיות במה[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj7iPkOqCZpCQNtf7W6kqQ6x/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]חלם בהלם[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj63PcR3r2VmhG95qmPzXouc/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]כאן ואומן[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj4WTj-7ffYUJpt2FDvS5ivo/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]כנסת נכבדה[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj4wTsnXOgf0OBcoaiO7kQfg/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]להיות מדען עם פרופסור דן[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj4oR5aIC0Ru5JZA1a1TT-RN/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]מה זה מוזה - עונה ראשונה[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj4F8EkY07BfV1KhdjmtjX0P/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]מה זה מוזה - עונה שנייה[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj5KKuKBn54FgrmNvXKZ6BYJ/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]עולם הבובות של גלי[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj5y9-iDpGCcw1Rf1YhMl85m/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]פסקול ישראלי שירים בודדים[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj4BhoUBgEoRl0LP94e1ivAo/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]שטרודל[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj5Hw7X0PY-mLgVYFFm0TK5b/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]אדריכלות ישראלית[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj6Ajq6brj2sbLQ0AEmD10L_&index=9/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]שיחת נפש[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj4hWCdqRdSppJk2akOip3Q4/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]תיק תקשורת[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PL0AFb_m5tVQI7SBCpLA9VzVX9EXYAr2WQ/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]חדש בעיניים[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj5qPsqwLPkxs_-lkIJZfg0H/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]המושכים בחוטים[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj6s0QtcgOpIwKewkEeSN77e/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]הכל פתוח[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj4LovalcoZLy7TPJ8oAL0k6/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]הכל אנשים[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj7TAvhkV8c9UnnMHUpQy-Bx/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]חדשות מהעבר - עונה ראשונה[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj76Eh3jZ6V5lRvuAp6lHU1e/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]חדשות מהעבר - עונה שנייה[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj4IjHf-ISoprm2r9FO0szaD/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]חדשות מהעבר - עונה שלישית[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj6Y7AkPBqhGRsHNaG77e2f9/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]היו סרטים[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj474gCGLEUa7_Zo5Bxgy9fG&index=43/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]טעמים[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj6FX0sryFAHDSQPB5fb0Ye9/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]זה מזה[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj6JtH-ZS7brPS6CS2R02nmw/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]בין השורות[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj6fMz_DxFpb-wgQDgR6YAOf/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]גאון של אבא[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj65xupugNnupcCT0tzS_HH3/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]פלאשבק[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj6gEP4qa6lTQy3P8jcRMS3z/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]מה הסיפור? - עונה ראשונה[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj4pXBYq0rXfkLDWdNriJ_3-/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]מה הסיפור? - עונה שנייה[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj5cz5fWddeMmXQ_97bNjBh-&index=3/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]שערוריה[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj4S_9xEMNDAw9N6HLPD8tfi/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]מוסף המוספים[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj6RCZ4v_lgajIiOU3PM6nNo/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]הקשר הישראלי - עונה שנייה[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj6H-qyug15LKMTvLY9TgwVN/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]זמן הורים[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj4njfaDOYLtyRfowZaDbPZE/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]אינטרמצו עם אריק - עונה ראשונה[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj5K-DyuhP5FghHHN8x0BEgA/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]אינטרמצו עם אריק - עונה שנייה[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj7pQXCOUwNohLCvkbusvqD6/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]פרופיל 2013[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj5zbilu3Z8azxJpv24X1dwn/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]לינק+[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj4D7japJmmP4L0urxx3j33R/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]הכל תרבות[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj4wnHAqF1cabFNSv3p9RCfr&index=2/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]חי בסרט[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj4ph_DTmh2pYW-ENXxsNXVb/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]גדולים מהחיים-הדור הבא[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj7BJiKn76rVDpDvMP4bGd55/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]שם נולדתי[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj5ghNY2qA41CzTan9WPf01m/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]עניין של טעם - בישול מהספרים[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj56FLWmFEiqFjNIHjKJlO3j/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]עניין של טעם[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj4nexv1mWGSmQB2fmwuAwUw/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]2,3 הקשב[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj74EndXG78h2Oqw60Mk8yWx/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]ההפסקה הגדולה[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PLFF36DACC75CDB042/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]זרקור עם גל גבאי[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj6bjzN59BD70vmYuXlURzEo/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]סברס[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj72fEPM2Mu76jTrHOg8SEok/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]לשון המראות[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL3D2F6C62B695FE89/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]שיחות ברוח[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PLABDA0375B943DAEC/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]ברית עם מילה[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PLBA7E16EB421A5F60/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]המושבעים[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PLAB74682339E0173C/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]אני לא כזה[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL8AF214FE9865E579/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]כן לציפור[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL41D53039B90917B0/?page=1",35,art + '23.jpg')

 
def lomdim99y(): 
        addDir3('[COLOR aqua]דן ועדנה - לימוד אנגלית[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj781aLgQXZNeCcbn9qXbX5E/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]הלו פנינה - לימוד עברית[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PL8Ydu6CcDpZQoXCvRq_O7l0AcgaV1aiV6/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]תעלם ותכלם - לימוד ערבית[/COLOR]'+translate(830033)+'',"plugin://plugin.video.youtube/playlist/PL2ZWSou1jCkichu7tlmSIk6FmmFEJ3i64/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]Candy Can Do It - לימוד אנגלית[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PL8Ydu6CcDpZSJQmln2O90W_3EMBsuqXOE/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]IN ITALIANO - לימוד איטלקית[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PL8Ydu6CcDpZSuA5DcAszNLFpQ-QdnZXHF/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]גבי ודבי - לימוד אנגלית[/COLOR]'+translate(830056)+'',"plugin://plugin.video.youtube/playlist/PL2ZWSou1jCkhfZ4rEHTR0OIXh1GyIqDPw/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]Dites Moi Tout - לימוד צרפתית[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PL8Ydu6CcDpZRzt1ZB6WZFWdbIg-MDUv3l/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]בוא נתערב - לימוד עברית[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PL8Ydu6CcDpZRqp5xJ5YpXUZWspJa6YE_8/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]English English English - לימוד אנגלית[/COLOR]'+translate(830058)+'',"plugin://plugin.video.youtube/playlist/PL2ZWSou1jCkgZ0AhwJe5D3j2-QmNovBRq/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]More About English - לימוד אנגלית[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PL8Ydu6CcDpZReqe4i8tPvyzYv3_z5jw_N/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]גלילאו - עונה רביעית[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj5ERxljvk0cLQAjnLMj3son/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]גלילאו - עונה חמישית[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj6Ypxb-_Dh0eoCztCXiBYsN/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]גלילאו - עונה שישית[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj5RB1GQe2OoPwFWTcwFMFDs/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]גלילאו - עונה שביעית[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj5UDRn7jbyChrKst-WUX_qF/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]גיאומטריה[/COLOR]'+translate(830049)+'',"plugin://plugin.video.youtube/playlist/PL2ZWSou1jCkimo8aEXsW0qGT8FDIto0rL/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]נאס"א : העולם שלנו[/COLOR]'+translate(830049)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj4fkOhV8lrwQsz8e-JDoynm&index=43/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]אוצרות ומכמנים[/COLOR]'+translate(830049)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj6Nb8bGTwxIrCQQG9yzcKuq/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]חידון התנ"ך[/COLOR]'+translate(830049)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj51ODBIMhtOF_lYxjS1cuQh/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]ערב חדש לילדים[/COLOR]'+translate(830049)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj5_wjkZreM5E7NScaGBFYLe/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]מי בא לקישקשתא?[/COLOR]'+translate(830049)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj7McnJ8UQse9KH58JaxZWF4/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]קישקשתא בדרכים - המקום הנכון לחצות[/COLOR]'+translate(830049)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj5szmjjHjRrx2OQ4mX4aUev/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]בית ספר לקוסמים[/COLOR]'+translate(830049)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj6KxVL84Li-dp6BnOB0gChG/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]תנ"ך בחרוזים[/COLOR]'+translate(830049)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj5NmIEX774qPsqFVeWLKptt/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]קרב מוחות[/COLOR]'+translate(830049)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj54RN3mRLW566n82cttFOer/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]מנת משכל[/COLOR]'+translate(830049)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj4-rWObWycjkZM1M54s3j4D/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]Signal CQ Calling[/COLOR]'+translate(830054)+'',"plugin://plugin.video.youtube/playlist/PL2ZWSou1jCkgi_a2X8IAdmLfrG5_cOAq5/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]Neighbours[/COLOR]'+translate(830055)+'',"plugin://plugin.video.youtube/playlist/PL2ZWSou1jCkioehq3dj0z9qmZed9Qe7G-/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]Here we are[/COLOR]'+translate(830057)+'',"plugin://plugin.video.youtube/playlist/PL2ZWSou1jCkiUbjMohokWFVTB2TJZjg7v/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]לשם שינוי - בגרות באזרחות[/COLOR]'+translate(830057)+'',"plugin://plugin.video.youtube/playlist/PLBAF8C2237E80A6DC/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]זה לא עסק[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PLBE9EAFE6BA307506/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]סובב ישראל[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PLE196ECE55F4B8629/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]לאן יהודים לאן[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL45D145EEFF323EF1/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]כמה כמה[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PLD04AADEEA392DE2F/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]יוצרים עם חנוך פיבן[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PLCE8D051221B747EC/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]חשבון פשוט-חשבון לכיתה ד[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL8EFCDA3F0C14856E/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]ספיישל לומדים - כל התוכניות[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL5966B40FAD38F7D5/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]מורה פרטי - מתמטיקה לבגרות 3 יחידות[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PLD2A326BB34DD9059/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]מורה פרטי - מתמטיקה לבגרות 4 יחידות[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL4499F9E4F2B0715D/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]מורה פרטי - מתמטיקה לבגרות 5 יחידות[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL1C7690D248842BE3/?page=1",35,art + '23.jpg')

 
def special99y(): 
        addDir3('[COLOR aqua]אוצרות נוסטלגיה בשחור לבן[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj6mH4KRWm7IE_J1geTcVmX9/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]ארכיון רשות השידור[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PLLttfoK87AdVEUsFtRJCoCXl4Yx0jp-3-&index=4/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]שידורים לרצח רבין[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj4QjlggCSzpoZ5VxOFK_CrP/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]חנה מרון 1923-2014[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj48SyN77XSbSf53_-h7mWp7&index=2/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]ספי ריבלין 1947-2013[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj7I5Vwy8ZqoY0WpkxnUkabM/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]אסי דיין 1945-2014[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj6nOCrX0rG6VXav8pUREFlF/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]אריק איינשטין 1939-2013 [/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj4LFBKNwCk7Xi1vpkqIkvff/?page=1",35,art + '23.jpg')
 
        addDir3('[COLOR aqua]ספיישל חג חנוכה[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj6iSrDhUtCLTLeLhq9Bnn3O/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]ספיישל חג פורים[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj4KOG8oJrs70F_u8bAVH3lW/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]ספיישל חג טו בשבט[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj6Ob3E922l8DoM8U-ay6rwt/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]ספיישל חג פסח[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj6wyHVgtg0ebuwqYqhh2D_j/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]חגי תשרי[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj4LOZbA2VzFPUTkheKOlmaE/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]תוכניות מיוחדות ליום הזיכרון[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj4eWriUKWAPnNODq8QR_UlB/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]סיכומי ששת הימים[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj6h-wbbbnUI-TkwyirGxbcr/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]יום השואה בחינוכית[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj6zllZWhjkRCv95Q9LPhRZ2/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]שמיכת טלאים - פרוייקט ליום הזיכרון[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj40WOr1ylSGNITWbH7r6pAF&index=2/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]אולפן פתוח-מלחמת המפרץ[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj406VKwHca6NeZc8RLQe-2U/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]קולה של אמא[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj4QX3eKDcyn_GngNv14t6vs/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]היסטוריה בארץ ישראל[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL4654A73C7195CDE5/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]נוסטלגיה באנגלית[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PLD1AA6CFEB351552E/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]ספורט - משחקים מלאים[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PLAFF0CE2A6D305335/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]ספיישל תוכניות לילדים[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PLEEADE8D8F08C1CF8/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]קטעי קאלט נוסטלגיים - חלק א[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL865DC5C74264BF11/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]קטעי קאלט נוסטלגיים - חלק ב[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL78D26C6B20B90459/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]ספיישל אקטואליה ותרבות[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL41C878044EB8B4DF/?page=1",35,art + '23.jpg')


        addDir3('[COLOR aqua]אלי יצפאן - DVD CD.3 [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=KGam4dPAF0w/?page=1",35,art + '23.jpg')

        addDir3('[COLOR aqua]הגשש החיוור - [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=הגשש החיוור מערכונים מלאים&search_type=playlist",35,art + '23.jpg')


 
def music99y():
        addDir3('[COLOR aqua]מחווה לאמן בקאמרי[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj7m81J5ClB3hjdIZ6CN3uwH/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]מוזיקה היום[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj4HjSMomAQkLAxTezmoREXn/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]אני גיטרה - עונה ראשונה[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj4VO17d-PgLgwhuUMkelg4k/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]אני גיטרה - עונה שנייה[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj4SY2HwfowNP3nQ9hKpL2Ko/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]פסקול ישראלי[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj4BhoUBgEoRl0LP94e1ivAo/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]חלום לים התיכון[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj5h_EJBX7YvcKSuclmG2mA6/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]דואט ישראלי[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj7IzrXIoNEfXzq0BOG-vClM/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]ארכיון רשות השידור - מוזיקה[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PLLttfoK87AdXPHsgVJz0lYhzXrUU_9MxO/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]כדי שלא יאבד[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj4dK_dKGEwJY0wG5HYkLLs-/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]זו ילדותי[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj42DChiYRjfKMHWF5yBKpmJ/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]מוזיקה ישראלית - קליפים[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL0CA90DCC0F764E88/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]פסטיבל שירי ילדים[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PLiRWC7Q54Giryds243PO_ocr2I2cEJb44/?page=1",35,art + '23.jpg')
 
def kidsnew99y():
        addDir3('[COLOR aqua]בחצר של פופיק - כל העונות[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PLrXHa7yEIVEK4otul2GvgRduQrp_WHozQ/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]דן ומוזלי - עונה ראשונה[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PLunrwEAfSt0Q4EY9QvJLQ-qcmj26fFGps/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]דן ומוזלי - עונה שנייה[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PLth1a195qHsh2JB7l8Y-0B8RKTzKeLTzI/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]דן ומוזלי - עונה שלישית[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj6HjLShpTpzJfmYbrKtb2iq/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]כל השירים של דן ומוזלי[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj6eJ2M_tZhiFUKhh3-xTJ0_/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]החפרנים - עונה ראשונה[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj6PWe7kECdyz6ToCjcmSd6z/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]החפרנים - עונה שנייה[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj5kggjXDJupMLWlxOtalMCe/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]החפרנים - עונה שלישית[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj72a-r737sA5zGGmns56uLI/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]שרגא בישגדא - עונות: 1,2,3,4,5[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj5KPYOntZkqg2Nwyqj2M1Lf/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]שרגא בישגדא - עונה 6[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj7yAMOPpd9RZpRbsWlb30CH/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]שוסטר ושוסטר [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=שוסטר ושוסטר עונה/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]הורים וגורים[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj5sp5nUKFuwuUddCXYjiH8F/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]תראו אותי[/COLOR]'+translate(830064)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj7jf8HAcgMERYrNyHQd6bgD/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]אולפן הבית - מתכונים[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj6O2gLT7i0Usc5LVRFF-wRT/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]אולפן הבית - שיאים[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj5LYIrCbBwfFHKVt4C6j8JH/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]אולפן הבית - מילים להחלפה[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj638OcGN_S_ptSPC-LCcDAv/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]אולפן הבית - חמשירים[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj5GovUy3GXS1d2ELtDXyMWt&index=2/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]אולפן הבית - טריוויה[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj6mkx1NYiG9fy7fg_lhAM2g/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]אולפן הבית - גן חיות[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj4-tSuiYCRuXzbG7OVdXkTc/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]אולפן הבית - סופר בריין[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj5-7O6pcFU-LDqz38ES7XcX/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]אולפן הבית - התעוררות[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj4plw_67m2RCi-YB1yGsQMJ/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]אולפן הבית - פתגם[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj5fEWuvyYU1Bw5xoksQFCHi/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]אולפן הבית - עצות ומשחקים[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj4-PoYife4j11pGZzbiqYH3/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]אולפן הבית - ערב[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj7nXkSHUkn2WR0fDJ8bX8Yc/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]אולפן הבית - היפ הופ[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj5x1Mpals5RkvP1_SGCLeNO/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]אולפן הבית - דגלים[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj5wktrVq0M3RDGv4tBdMusP/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]אולפן הבית - מדען[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj7ramMR-kDnOSbVvkFoswZk/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]בית ספר לשפים מתחילים[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj7xLodgRH6lTHQysTUKG_Kr/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]המטבחון - בישול לילדים[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj7mdtecfMQvlvxv2KHI-7BD&index=4/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]הולה הופ - לילדים[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj4pgezv6SHwl2b9JeHdXnHD/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]יוגה לילדים - סרטוני הדרכה[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj7wHwsiqOd00V9SBa8XrdNR&index=2/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]רוצים לזוז - כושר ילדים[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj4-pONO5m1bGZbyuAaxVHK6&index=2/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]פעילויות יצירה לילדים[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj4gEgcQ7xUnkEMhLJKVqEvE/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]אלימות זה בידיים שלנו[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL44A6264C94477E4C/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]בשביל הסיפורים[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PLF1F15FC862BDEB2F/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]חטף פתח[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL97498F46F690C8BC/?page=1",35,art + '23.jpg')
        addDir3('[COLOR aqua]זאק וקוואק[/COLOR]'+translate(830059)+'',"plugin://plugin.video.youtube/playlist/PL1VPiBc5XLZwuAsIgYRGmreRxuzbC4TMu/?page=1",35,art + '23.jpg')


		
def juniory():
        addDir3('[COLOR aqua]קופיקו עונה 1[/COLOR]',"plugin://plugin.video.youtube/playlist/PLR7DTcU2p0QhDzYbbniDNwSbXUM_p6N3f/?page=1",35,art + '30030.jpg')
        addDir3('[COLOR aqua]קופיקו עונה 2[/COLOR]',"plugin://plugin.video.youtube/playlist/PLR7DTcU2p0QgEdLPHhrhKtxElvYVrseAQ/?page=1",35,art + '30030.jpg')
        addDir3('[COLOR aqua]קופיקו עונה 3[/COLOR]',"plugin://plugin.video.youtube/playlist/PLR7DTcU2p0QhNGUffSgu8_5dP3lnOGZTx/?page=1",35,art + '30030.jpg')
        addDir3('[COLOR aqua]רוי בוי[/COLOR]',"plugin://plugin.video.youtube/playlist/PLR7DTcU2p0Qg8pxiEld0Fg3K2Bd8gTKw5/?page=1",35,art + '30030.jpg')
        addDir3('[COLOR aqua]משטרת האגדות[/COLOR]',"plugin://plugin.video.youtube/playlist/PLR7DTcU2p0QiaEmc56lGHMpxW4ladE93X/?page=1",35,art + '30030.jpg')


def nostaly():
        addDir3('[COLOR aqua]הבית של פיסטוק[/COLOR]',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj7D-QAVZ94EK-BHm7XG9BOl/?page=1",35,art + 'kids.png')
        addDir3('[COLOR aqua]נילס הולגרסון [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=נילס הולגרסון&search_type=playlist",35,art + 'kids.png')
        addDir3('[COLOR aqua]דובוני אכפת לי [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=דובוני אכפת לי&search_type=playlist",35,art + 'kids.png')
        addDir3('[COLOR aqua]הקוסם מארץ עוץ[/COLOR]',"plugin://plugin.video.youtube/playlist/PLrm9dDLqwrHnZF86MMTIb-Q3LSKLGLTDQ/?page=1",35,art + 'kids.png')
        addDir3('[COLOR aqua]הדרדסים [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=הדרדסים&search_type=playlist",35,art + 'kids.png')
        addDir3('[COLOR aqua]צבי הנינגה [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=צבי הנינגה&search_type=playlist",35,art + 'kids.png')
        addDir3('[COLOR aqua]הלב [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=הלב מרקו&search_type=playlist",35,art + 'kids.png')
        addDir3('[COLOR aqua]הקטקטים [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=הקטקטים&search_type=playlist",35,art + 'kids.png')
        addDir3('[COLOR aqua]שוטרים וגנבים [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=שוטרים וגנבים&search_type=playlist",35,art + 'kids.png')
        addDir3('[COLOR aqua]גברת פלפלת [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=גברת פלפלת&search_type=playlist",35,art + 'kids.png')

        addDir3('[COLOR aqua]החיים - היה היה [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=החיים - היה היה&search_type=playlist",35,art + 'kids.png')
        addDir3('[COLOR aqua]בלי סודות [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=בלי סודות&search_type=playlist",35,art + 'kids.png')
        addDir3('[COLOR aqua]פרפר נחמד [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=פרפר נחמד&search_type=playlist",35,art + 'kids.png')
        addDir3('[COLOR aqua]דן הדוור [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=דן הדוור&search_type=playlist",35,art + 'kids.png')
        addDir3('[COLOR aqua]הדבורה מאיה [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=הדבורה מאיה&search_type=playlist",35,art + 'kids.png')
        addDir3('[COLOR aqua]קשת וענן [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=קשת וענן&search_type=playlist",35,art + 'kids.png')
		
def dsjuniory():
        addDir3('[COLOR aqua]דיסני גוניור כללי [/COLOR]',"plugin://plugin.video.youtube/channel/UC2FtQO6HiTYejqkbqrowGSw&search_type=playlist",35,art + 'dsjr.jpg')
        addDir3('[COLOR aqua]ארמון החיות [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=ארמון החיות&search_type=playlist",35,art + 'dsjr.jpg')
        addDir3('[COLOR aqua]הנסיכה סופיה הראשונה [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=הנסיכה סופיה הראשונה&search_type=playlist",35,art + 'dsjr.jpg')
        addDir3('[COLOR aqua]הסרטים המצויירים של מיני [/COLOR]',"plugin://plugin.video.youtube/playlist/PLCcisG7DtTgtpi5Hbb8ZJuOvbGLVJVjf5/?page=1",35,art + 'dsjr.jpg')
        addDir3('[COLOR aqua]ספיישל להיות פיראט[/COLOR]',"plugin://plugin.video.youtube/playlist/PLVwL64lSxWWzCmfvd65mBVKGX0VMFIEM7/?page=1",35,art + 'dsjr.jpg')
        addDir3('[COLOR aqua]התעמלות עם מיקי מאוס[/COLOR]',"plugin://plugin.video.youtube/playlist/PLVwL64lSxWWwLsl52oUSphP6zSbbvQu_h/?page=1",35,art + 'dsjr.jpg')
        addDir3('[COLOR aqua]דוק רופאת צעצועים[/COLOR]',"plugin://plugin.video.youtube/playlist/PLVwL64lSxWWyRD2CIOc5qkXUuSWSsyuRh/?page=1",35,art + 'dsjr.jpg')
        addDir3('[COLOR aqua]הרגעים הגדולים של סטאר [/COLOR]',"plugin://plugin.video.youtube/playlist/PLRKLm5GvuZVIv7NoJvoBrlAlOYaatpzqM/?page=1",35,art + 'dsjr.jpg')
        addDir3('[COLOR aqua]היורשים - בית ספר של סודות[/COLOR]',"plugin://plugin.video.youtube/playlist/PLRKLm5GvuZVJq1moobQvXZUHMM943qAWP/?page=1",35,art + 'dsjr.jpg')
        
def zoomy():
        addDir3('[COLOR aqua]ערוץ זום כללי [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=ערוץ זום&search_type=playlist",35,art + 'zoom.jpg')
        addDir3('[COLOR aqua]ציקה ומפירו[/COLOR]',"plugin://plugin.video.youtube/playlist/PLKMFPiSCwUk2GEiyvpK-VxGigTDnHD_3C/?page=1",35,art + 'zoom.jpg')
        addDir3('[COLOR aqua]סוסי פרא[/COLOR]',"plugin://plugin.video.youtube/playlist/PL9FUtLp-Tfr3vR1EJa04KIDYskHfpsaQp/?page=1",35,art + 'zoom.jpg')
        addDir3('[COLOR aqua]מועדון החנונים[/COLOR]',"plugin://plugin.video.youtube/playlist/PLKMFPiSCwUk0myYc1Z8oPLGO6hXJdf5uv/?page=1",35,art + 'zoom.jpg')
        addDir3('[COLOR aqua]סופר סטרייקה[/COLOR]',"plugin://plugin.video.youtube/playlist/PLKMFPiSCwUk3bjgDUSlTPskV9rA74nBiB/?page=1",35,art + 'zoom.jpg')
        addDir3('[COLOR aqua]מועדון החנונים[/COLOR]',"plugin://plugin.video.youtube/playlist/PLKMFPiSCwUk22xxgMwcNShgeBYNSfotbB/?page=1",35,art + 'zoom.jpg')
        addDir3('[COLOR aqua]אמאמביכה[/COLOR]',"plugin://plugin.video.youtube/playlist/PLKMFPiSCwUk3yEo1xowld-EV_U7w8YwfF/?page=1",35,art + 'zoom.jpg')
        addDir3('[COLOR aqua]איטי ועצבני[/COLOR]',"plugin://plugin.video.youtube/playlist/PLKMFPiSCwUk08zM6SlJ3RrCu2_zdReijH/?page=1",35,art + 'zoom.jpg')
        addDir3('[COLOR aqua]פאוור  ריינגרס[/COLOR]',"plugin://plugin.video.youtube/playlist/PLKMFPiSCwUk3KmFxp-8n4NtmdHGCQFxee/?page=1",35,art + 'zoom.jpg')
        addDir3('[COLOR aqua]צפוף[/COLOR]',"plugin://plugin.video.youtube/playlist/PLKMFPiSCwUk28xwNsCOGZr70pSaXxlnlk/?page=1",35,art + 'zoom.jpg')
        

		
		
def kidstvy():
        addDir3('[COLOR aqua]ערוץ הילדים כללי [/COLOR]',"plugin://plugin.video.youtube/channel/UCOFp2_GttW3ljCuOc7r4l7g/?page=1",35,art + 'kidstv.png')
        addDir3('[COLOR aqua]הכל טום[/COLOR]',"plugin://plugin.video.youtube/playlist/PLstSEvEmr9e8wuM076jsnSbM6HEdLjmfz/?page=1",35,art + 'kidstv.png')
        addDir3('[COLOR aqua]ברחובות שלנו[/COLOR]',"plugin://plugin.video.youtube/playlist/PLstSEvEmr9e-2ucQ38nu31Ms1qJPlVHcS/?page=1",35,art + 'kidstv.png')
        addDir3('[COLOR aqua]שוברי גלים[/COLOR]',"plugin://plugin.video.youtube/playlist/PLnzhIyrsnB5bRzOyHnZgx7yHzOBAXz79L/?page=1",35,art + 'kidstv.png')
        addDir3('[COLOR aqua]נדחפים[/COLOR]',"plugin://plugin.video.youtube/playlist/PLstSEvEmr9e-7DxpPTuIbRjIbFCMcY7YZ/?page=1",35,art + 'kidstv.png')
        addDir3('[COLOR aqua]השמיניה[/COLOR]',"plugin://plugin.video.youtube/playlist/PLdHb9F0cRmPwtckIQ4LtKH_ZZOtTYoxC7/?page=1",35,art + 'kidstv.png')
        addDir3('[COLOR aqua]בית ספר למוזיקה[/COLOR]',"plugin://plugin.video.youtube/playlist/PLF583DE56321F34CF/?page=1",35,art + 'kidstv.png')
        
def hoty():
        addDir3('[COLOR aqua]HOTVODyoung כללי [/COLOR]',"plugin://plugin.video.youtube/channel/UC0GgioZ1XWa9xNJJH66h7rg/?page=1",35,art + 'HOTVOD.png')
        addDir3('[COLOR aqua]סוסי פרא[/COLOR]',"plugin://plugin.video.youtube/playlist/PL419YR22ubLCkWDoe9rdRvkeF3UD259Wq/?page=1",35,art + 'HOTVOD.png')
        addDir3('[COLOR aqua]גאליס [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=גאליס כל העונות פרקים מלאים&search_type=playlist",35,art + 'HOTVOD.png')
        addDir3('[COLOR aqua]מועדון החנונים [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=מועדון החנונים&search_type=playlist",35,art + 'HOTVOD.png')
        addDir3('[COLOR aqua]הקלמרים [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=הקלמרים&search_type=playlist",35,art + 'HOTVOD.png')
        addDir3('[COLOR aqua]הפיגמות [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=הפיגמות&search_type=playlist",35,art + 'HOTVOD.png')
        addDir3('[COLOR aqua]שכונה[/COLOR]',"plugin://plugin.video.youtube/playlist/PL419YR22ubLAeiTiDZ3oHDtPmD54vi2vB/?page=1",35,art + 'HOTVOD.png')
        addDir3('[COLOR aqua]גיא ביער החיות[/COLOR]',"plugin://plugin.video.youtube/playlist/PL419YR22ubLD1JcHPAtU_KFQ-53xOZ9YP/?page=1",35,art + 'HOTVOD.png')
        addDir3('[COLOR aqua]החוף של רינת - 2[/COLOR]',"plugin://plugin.video.youtube/playlist/PL419YR22ubLB2k8pelTCjEcf9vtOdJPMX/?page=1",35,art + 'HOTVOD.png')
        addDir3('[COLOR aqua]עמרי והפיה יעלי[/COLOR]',"plugin://plugin.video.youtube/playlist/PL419YR22ubLBPUYYOTxv3y4J4jadrvBDM/?page=1",35,art + 'HOTVOD.png')
        addDir3('[COLOR aqua]חיפזון וזהירון [/COLOR]',"plugin://plugin.video.youtube/playlist/PL419YR22ubLCBKso-lZI46QeMOajbJo1K/?page=1",35,art + 'HOTVOD.png')
        addDir3('[COLOR aqua]החוף של רינת - עונה 1[/COLOR]',"plugin://plugin.video.youtube/playlist/PL419YR22ubLDmN4nWRYdtXsPEqfUcwXTu/?page=1",35,art + 'HOTVOD.png')
        addDir3('[COLOR aqua]רוני וקשיו[/COLOR]',"plugin://plugin.video.youtube/playlist/PLFC30D9236B6C1D89/?page=1",35,art + 'HOTVOD.png')
        addDir3('[COLOR aqua]הגרוטיאדה[/COLOR]',"plugin://plugin.video.youtube/playlist/PLD410CE40090B6F46/?page=1",35,art + 'HOTVOD.png')	
        addDir3('[COLOR aqua]מותק של יומולדת[/COLOR]',"plugin://plugin.video.youtube/playlist/PL19F7B03ACE78D040/?page=1",35,art + 'HOTVOD.png')
        addDir3('[COLOR aqua]מלכת קסמים[/COLOR]',"plugin://plugin.video.youtube/playlist/PL252279467C3A6572/?page=1",35,art + 'HOTVOD.png')

		
def hopy():
        addDir3('[COLOR aqua]הופ כללי [/COLOR]',"plugin://plugin.video.youtube/channel/UClZXqxeY540_Epab3WDHFGw/?page=1",35,art + 'hop.png')
        addDir3('[COLOR aqua]סמי הכבאי [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=סמי הכבאי&search_type=playlist",35,art + 'hop.png')
        addDir3('[COLOR aqua]פיטר הארנב [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=פיטר הארנב&search_type=playlist",35,art + 'hop.png')
        addDir3('[COLOR aqua]דני שובבני [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=דני שובבני&search_type=playlist",35,art + 'hop.png')
        addDir3('[COLOR aqua]סבא טוביה [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=סבא טוביה&search_type=playlist",35,art + 'hop.png')
        addDir3('[COLOR aqua]מר עגבניה [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=מר עגבניה פרקים מלאים &search_type=playlist",35,art + 'hop.png')
        addDir3('[COLOR aqua]בוב הבנאי [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=בוב הבנאי&search_type=playlist",35,art + 'hop.png')
	

def hopyy():
        addDir3('[COLOR aqua]הופ ילדות ישראלית כללי [/COLOR]',"plugin://plugin.video.youtube/channel/UCfNjGgy-3XfTzgWoGMt_QOw/?page=1",35,art + 'hopy.jpg')

        addDir3('[COLOR aqua]שירי נעמי שמר [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=שירי נעמי שמר&search_type=playlist",35,art + 'hopy.jpg')
        addDir3('[COLOR aqua]שירי אריק איינשטיין - שירים ילדים [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=שירי אריק איינשטיין - שירים ילדים&search_type=playlist",35,art + 'hopy.jpg')

       				
def nickjuniory():
        addDir3('[COLOR aqua]דורה [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=דורה פרקים מלאים בעברית  &search_type=playlist",35,art + '30031.jpg')
        addDir3('[COLOR aqua]מפרץ ההרפתקאות[/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=מפרץ ההרפתקאות פרקים מלאים בעברית&search_type=playlist",35,art + '30031.jpg')
        addDir3('[COLOR aqua]תמר הבלשית[/COLOR]',"plugin://plugin.video.youtube/playlist/PLPWc8VdaIIsAki2FqbtHQ7xW3zIMCTL3d/?page=1",35,art + '30031.jpg')
        addDir3('[COLOR aqua]ענבלי בא לי[/COLOR]',"plugin://plugin.video.youtube/playlist/PLPWc8VdaIIsB2vKN57J-hZAk8nqGpa4EF/?page=1",35,art + '30031.jpg')
        addDir3('[COLOR aqua]זמן לזוז[/COLOR]',"plugin://plugin.video.youtube/playlist/PLPWc8VdaIIsDYbIQJMDX4usMYw7pYmPxj/?page=1",35,art + '30031.jpg')
        addDir3('[COLOR aqua]הסוד של מיה[/COLOR]',"plugin://plugin.video.youtube/playlist/PLPWc8VdaIIsCGEVOC2iJxnWNEjI13xbnA/?page=1",35,art + '30031.jpg')
        addDir3('[COLOR aqua]עולמו הקסום של מקס[/COLOR]',"plugin://plugin.video.youtube/playlist/PLPWc8VdaIIsCeVQhASYBNmykK4gKh0DCe/?page=1",35,art + '30031.jpg')
        addDir3('[COLOR aqua]מר למה וגברת ככה[/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=מר למה וגברת ככה  &search_type=playlist",35,art + '30031.jpg')
        addDir3('[COLOR aqua]משפחת יומולדת[/COLOR]',"plugin://plugin.video.youtube/playlist/PLPWc8VdaIIsBOUPxtM2CD7yGs1D8NCM_Z/?page=1",35,art + '30031.jpg')
        addDir3('[COLOR aqua]שטויות בחדשות [/COLOR]',"plugin://plugin.video.youtube/playlist/PLPWc8VdaIIsBzxaUfj3smv1tJ8sKQXwrW/?page=1",35,art + '30031.jpg')
        addDir3('[COLOR aqua]בגינה של לין[/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=בגינה של לין  &search_type=playlist",35,art + '30031.jpg')
        addDir3('[COLOR aqua]סיפורי פיות[/COLOR]',"plugin://plugin.video.youtube/playlist/PLPWc8VdaIIsD8YvtRkkqjYC5SF7TKvAcM/?page=1",35,art + '30031.jpg')
        addDir3('[COLOR aqua]יצירה בקצרה[/COLOR]',"plugin://plugin.video.youtube/playlist/PLPWc8VdaIIsC0SPM0_dgOVIDn5vcCH8Ti/?page=1",35,art + '30031.jpg')
        addDir3('[COLOR aqua]שלוש ארבע לעבודה[/COLOR]',"plugin://plugin.video.youtube/playlist/PLPWc8VdaIIsASIzs8TcS3FFYEL68jBPWO/?page=1",35,art + '30031.jpg')
        addDir3('[COLOR aqua]רוני וקשיו[/COLOR]',"plugin://plugin.video.youtube/playlist/PLPWc8VdaIIsDPb04SHd5fzzqYt3FtmWs-/?page=1",35,art + 'Cartoons.png')
		
def lulyy():
        addDir3('[COLOR aqua]לולי כללי [/COLOR]',"plugin://plugin.video.youtube/channel/UCcYc90JDakyeXGeZgPL1ejA/?page=1",35,art + 'luly.jpg')
        addDir3('[COLOR aqua]טלטאביז[/COLOR]',"plugin://plugin.video.youtube/playlist/PLCVlyUabAQX0baRcL13edNd1zBeqLuoaV/?page=1",35,art + 'luly.jpg')


def babyy():   
        addDir3('[COLOR aqua]בייבי כללי [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=ערוץ בייבי  &search_type=playlist",35,art + 'baby.jpg')    
        addDir3('[COLOR aqua]ערוץ בייבי - תוכניות ברצף[/COLOR]',"plugin://plugin.video.youtube/playlist/PLErYJg2XgxyWqQlU1CqCdPs15WhnAzzwb/?page=1",35,art + 'baby.jpg')
        addDir3('[COLOR aqua]שירים ישראליים לילדים[/COLOR]',"plugin://plugin.video.youtube/playlist/PLErYJg2XgxyXTMAJvmFXoW6Qe66Ztw0Fk/?page=1",35,art + 'baby.jpg')
        addDir3('[COLOR aqua]קיץ עם ערוץ בייבי[/COLOR]',"plugin://plugin.video.youtube/playlist/PLErYJg2XgxyWdetl6GmsKjp4hIlaR6BDl/?page=1",35,art + 'baby.jpg')
        addDir3('[COLOR aqua]פרקים מיוחדים ליום ההולדת[/COLOR]',"plugin://plugin.video.youtube/playlist/PLErYJg2XgxyWWl7sL3Oh25LxgXe5Vgpwz/?page=1",35,art + 'baby.jpg')
        addDir3('[COLOR aqua]חגי ישראל עם רינת גבאי ומימי [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=חגי ישראל עם רינת גבאי ומימי&search_type=playlist",35,art + 'baby.jpg')
        addDir3('[COLOR aqua]חורף עם ערוץ בייבי[/COLOR]',"plugin://plugin.video.youtube/playlist/PLErYJg2XgxyV4DL2r3vpo74zeJuWa8K1x/?page=1",35,art + 'baby.jpg')
        addDir3('[COLOR aqua]אוצר מילים עם נוני[/COLOR]',"plugin://plugin.video.youtube/playlist/PLErYJg2XgxyXmgk6cyROtlJh2g-Fk_T6n/?page=1",35,art + 'baby.jpg')
        addDir3('[COLOR aqua]רינת גבאי ומימי בארץ המילים[/COLOR]',"plugin://plugin.video.youtube/playlist/PLErYJg2XgxyX7c9LjwlY22F3cjpI5h6V_/?page=1",35,art + 'baby.jpg')
        addDir3('[COLOR aqua]דרקו ותולי[/COLOR]',"plugin://plugin.video.youtube/playlist/PLErYJg2XgxyVJhg76kIibughL6QiHgN2-/?page=1",35,art + 'baby.jpg')
        addDir3('[COLOR aqua]אוליבר[/COLOR]',"plugin://plugin.video.youtube/playlist/PLErYJg2XgxyX1gmsKze-1WjpDoNefNYJD/?page=1",35,art + 'baby.jpg')
        addDir3('[COLOR aqua]מתכוננים לשינה עם ערוץ בייבי[/COLOR]',"plugin://plugin.video.youtube/playlist/PLErYJg2XgxyVYzsbPxH2dzhlWLs9sWGTa/?page=1",35,art + 'baby.jpg')		
        addDir3('[COLOR aqua]רינת גבאי בעולם האגדות[/COLOR]',"plugin://plugin.video.youtube/playlist/PLErYJg2XgxyWiffjko4BQmExqDdR6-C4v/?page=1",35,art + 'baby.jpg')
		
def logyy():
        addDir3('[COLOR aqua]היה היה[/COLOR]',"plugin://plugin.video.youtube/playlist/PL7FRY7ROxqHQQFHpxmJ6r-xiB1K0BwGdu/?page=1",35,art + '30033.jpg')
        addDir3('[COLOR aqua]אין חיה כזאת - ממושה [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=אין חיה כזאת - ממושה&search_type=playlist",35,art + '30033.jpg')
        addDir3('[COLOR aqua]אוטובוס הקסמים [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=אוטובוס הקסמים&search_type=playlist",35,art + 'kids.png')
        addDir3('[COLOR aqua]המובילים עונה 1[/COLOR]',"plugin://plugin.video.youtube/playlist/PL-SBsAk8heRmm43KBeVhC9h6R6wCUSW7j/?page=1",35,art + '30033.jpg')
        addDir3('[COLOR aqua]המובילים עונה 2[/COLOR]',"plugin://plugin.video.youtube/playlist/PLBaGngHK8wj1OxzO6P3ouBUulIG4fijkG/?page=1",35,art + '30033.jpg')
        addDir3('[COLOR aqua]המובילים עונה 1-2-3[/COLOR]',"plugin://plugin.video.youtube/playlist/PLEDfJ53YcNLw8oh725vvG4qYd04bDo3z3/?page=1",35,art + '30033.jpg')
		

def nicklodeony():
        addDir3('[COLOR aqua]הצחוקייה 1-4: פרקים מלאים[/COLOR]',"plugin://plugin.video.youtube/playlist/PLuQCYUv97StSnZGTUoMyIjbFdAACRCxKV/?page=1",35,art + '30032.jpg')
        addDir3('[COLOR aqua]צמפיונסיק[/COLOR]',"plugin://plugin.video.youtube/playlist/PLuQCYUv97StRAe0OQOvWUBejgQVAjrucA/?page=1",35,art + '30032.jpg')
        addDir3('[COLOR aqua]גן חיות 1 + 2[/COLOR]',"plugin://plugin.video.youtube/playlist/PLuQCYUv97StTP1kioc4cGBUkdPrktt8Pz/?page=1",35,art + '30032.jpg')
        addDir3('[COLOR aqua]גן חיות עונה 3[/COLOR]',"plugin://plugin.video.youtube/playlist/PLuQCYUv97StQfg1CrmkR5ChUnu6q1X5Hj/?page=1",35,art + '30032.jpg')
        addDir3('[COLOR aqua]משפחת כספי[/COLOR]',"plugin://plugin.video.youtube/playlist/PLuQCYUv97StRNroygQpznlYXzyvob8aDJ/?page=1",35,art + '30032.jpg')
        addDir3('[COLOR aqua]שכונה[/COLOR]',"plugin://plugin.video.youtube/playlist/PLuQCYUv97StQ1q3po2cwh48H6LOSZbjaM/?page=1",35,art + '30032.jpg')
        addDir3('[COLOR aqua]הצחוקייה סופרסטארז[/COLOR]',"plugin://plugin.video.youtube/playlist/PLuQCYUv97StQ5w1484WOSYjwFfhiQsnPy/?page=1",35,art + '30032.jpg')
        addDir3('[COLOR aqua]הצחוקייה - קצרצרים, עונות 3-1[/COLOR]',"plugin://plugin.video.youtube/playlist/PLuQCYUv97StTBH8qBwHzw12DHe7Zn78Qx/?page=1",35,art + '30032.jpg')
        addDir3('[COLOR aqua]שכונה[/COLOR]',"plugin://plugin.video.youtube/playlist/PLuQCYUv97StR0o1N7zfbpobVVwev0sx91/?page=1",35,art + '30032.jpg')
        addDir3('[COLOR aqua]יפניק[/COLOR]',"plugin://plugin.video.youtube/playlist/PLuQCYUv97StS-YtE8BYNUpLIxKrGOBAe6/?page=1",35,art + '30032.jpg')
        addDir3('[COLOR aqua]סופר שטותניק[/COLOR]',"plugin://plugin.video.youtube/playlist/PLuQCYUv97StRk-DsmuAL0ptZPJ9ATkguV/?page=1",35,art + '30032.jpg')
        addDir3('[COLOR aqua]חבורת הספסל האחורי[/COLOR]',"plugin://plugin.video.youtube/playlist/PLuQCYUv97StTLZK9Zicyj4qfyiVh0DbkN/?page=1",35,art + '30032.jpg')
        addDir3('[COLOR aqua]קיץ דיגיטלי[/COLOR]',"plugin://plugin.video.youtube/playlist/PLuQCYUv97StT2i_JrYVDy2cVTW1Gtmp9s/?page=1",35,art + '30032.jpg')

def Dglllllly():
        addDir3('[COLOR aqua]תשרי [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q= חודש תשרי&search_type=playlist",35,'https://d3m9l0v76dty0.cloudfront.net/system/photos/2425670/large/237190d8c6cf6079514a1093ad4c08c6.jpg')
        addDir3('[COLOR aqua]חשוון [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q= חודש חשוון&search_type=playlist",35,'https://d3m9l0v76dty0.cloudfront.net/system/photos/2425670/large/237190d8c6cf6079514a1093ad4c08c6.jpg')
        addDir3('[COLOR aqua]כסלו [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q= חודש כסלו&search_type=playlist",35,'https://d3m9l0v76dty0.cloudfront.net/system/photos/2425670/large/237190d8c6cf6079514a1093ad4c08c6.jpg')
        addDir3('[COLOR aqua]טבת [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q= חודש טבת&search_type=playlist",35,'https://d3m9l0v76dty0.cloudfront.net/system/photos/2425670/large/237190d8c6cf6079514a1093ad4c08c6.jpg')
        addDir3('[COLOR aqua]שבט [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q= חודש שבט&search_type=playlist",35,'https://d3m9l0v76dty0.cloudfront.net/system/photos/2425670/large/237190d8c6cf6079514a1093ad4c08c6.jpg')
        addDir3('[COLOR aqua]אדר [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q= חודש אדר&search_type=playlist",35,'https://d3m9l0v76dty0.cloudfront.net/system/photos/2425670/large/237190d8c6cf6079514a1093ad4c08c6.jpg')
        addDir3('[COLOR aqua]ניסן [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q= חודש ניסן&search_type=playlist",35,'https://d3m9l0v76dty0.cloudfront.net/system/photos/2425670/large/237190d8c6cf6079514a1093ad4c08c6.jpg')
        addDir3('[COLOR aqua]אייר [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q= חודש אייר&search_type=playlist",35,'https://d3m9l0v76dty0.cloudfront.net/system/photos/2425670/large/237190d8c6cf6079514a1093ad4c08c6.jpg')
        addDir3('[COLOR aqua]סיוון [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q= חודש סיוון&search_type=playlist",35,'https://d3m9l0v76dty0.cloudfront.net/system/photos/2425670/large/237190d8c6cf6079514a1093ad4c08c6.jpg')
        addDir3('[COLOR aqua]תמוז [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q= חודש תמוז&search_type=playlist",35,'https://d3m9l0v76dty0.cloudfront.net/system/photos/2425670/large/237190d8c6cf6079514a1093ad4c08c6.jpg')
        addDir3('[COLOR aqua]אב [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q= חודש אב&search_type=playlist",35,'https://d3m9l0v76dty0.cloudfront.net/system/photos/2425670/large/237190d8c6cf6079514a1093ad4c08c6.jpg')
        addDir3('[COLOR aqua]אלול [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q= חודש אלול&search_type=playlist",35,'https://d3m9l0v76dty0.cloudfront.net/system/photos/2425670/large/237190d8c6cf6079514a1093ad4c08c6.jpg')

		
def lifestyley():  
        addDir3('[COLOR aqua]ערוץ החיים הטובים [/COLOR]',"plugin://plugin.video.youtube/channel/UCMwS6gVUo01idry02RWPAUg/?page=1",35,art + 'lifestyle.png')     
        addDir3('[COLOR aqua]'+translate(10013)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLCXKcf_9F-9ILiz6gapk-g6eRVczIinXn/?page=1",35,art + 'lifestyle.png')
        addDir3('[COLOR aqua]'+translate(10015)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLBQgA3Kndk7eYrJwHej6Swx-nryBmN52V/?page=1",35,art + 'lifestyle.png')
        addDir3('[COLOR aqua]'+translate(10016)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLK_DOFD1-caZyw7DH1PeghrCeAa0RXKGl/?page=1",35,art + 'lifestyle.png')
        addDir3('[COLOR aqua]'+translate(10018)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLPJTnhnYa-pOndAB5TU2A8qEpUguaxj5U/?page=1",35,art + 'lifestyle.png')
        addDir3('[COLOR aqua]'+translate(10019)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PL40DAF9063E60BD47/?page=1",35,art + 'lifestyle.png')
        addDir3('[COLOR aqua]'+translate(10020)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLfih4ifv3adEVX8ISbaVBY75hgh6FS7zP/?page=1",35,art + 'lifestyle.png')
        addDir3('[COLOR aqua]'+translate(10021)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLCR91DssNhp74MGMMJAbb7l2s2nm_5yvG/?page=1",35,art + 'lifestyle.png')
        addDir3('[COLOR aqua]'+translate(10023)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLWSwSEhBdIBKsVqaZn9PwebkLguJX3vSM/?page=1",35,art + 'lifestyle.png')
        addDir3('[COLOR aqua]'+translate(10025)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLYMK_Nbs-rsupx1SLcgZFXnfy7HZ3KRoN/?page=1",35,art + 'lifestyle.png')
        addDir3('[COLOR aqua]'+translate(10026)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLKUX44R3MbuR3sX61i9QiwnOBr61tEMc_/?page=1",35,art + 'lifestyle.png')
        addDir3('[COLOR aqua]'+translate(10027)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLE0ZXwRBc5iNxdziR3nGtfZoi11p2y0hO/?page=1",35,art + 'lifestyle.png')
        addDir3('[COLOR aqua]'+translate(10028)+'[/COLOR]',"plugin://plugin.video.youtube/channel/UCAUgzUb_ZUlGRCPYoPAIlsw/playlists/",35,art + 'lifestyle.png')
        

def documentaryy():    
        addDir('[COLOR aqua]דוקו מהעולם המיטב [/COLOR]','url',9876510004,'https://i.imgur.com/OcIWNOl.jpg')    
        addDir('[COLOR aqua]דוקו היסטוריה המיטב [/COLOR]','url',9876520012,'https://images-na.ssl-images-amazon.com/images/I/61mUljJAXJL.png')        
        addDir('[COLOR aqua]דוקו פשע המיטב [/COLOR]','url',9876520013,'https://icons.iconarchive.com/icons/3xhumed/mega-games-pack-40/512/True-Crime-Streets-of-LA-2-icon.png') 
        addDir3('[COLOR aqua]דוקו בעברית[/COLOR]','plugin://plugin.video.youtube/kodion/search/query/?q=%d7%93%d7%95%d7%a7%d7%95%d7%9e%d7%a0%d7%98%d7%a8%d7%99%20%d7%99%d7%a9%d7%a8%d7%90%d7%9c%d7%99',35,art + 'documentary.jpg')
        #addDir('[COLOR aqua]סרטוני טבע בעברית[/COLOR]','PLnzhIyrsnB5Y8Ymf2ryG-LlX0DxK0JD5N',1,art + 'documentary.jpg')
        addDir3('[COLOR aqua]זמן אמת[/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=זמן אמת&search_type=playlist",35,art + 'documentary.jpg')		
        addDir3('[COLOR aqua]חוצה ישראל[/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=חוצה ישראל&search_type=playlist",35,art + 'documentary.jpg')
        #addDir('[COLOR aqua]דוקומנטרי עם רינו צרור[/COLOR]','PLnzhIyrsnB5ahqRF_z2KwVFffa65NbDyR',1,art + 'documentary.jpg')
        addDir3('[COLOR aqua]טבע לילדים בעברית [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=טבע לילדים בעברית&search_type=playlist",35,art + 'documentary.jpg')
        #addDir('[COLOR aqua]סרטונים נבחרים נשיונל גאוגרפיק[/COLOR]','PLivjPDlt6ApQ8vBgHkeEjeRJjzqUGv9dV',1,art + 'documentary.jpg')
        #addDir('[COLOR aqua]סרטונים פופולריים סרטי טבע תיעודיים[/COLOR]','PL5o3ll3G4acxgDMSO7JXvDsosQ-UDPL6n',1,art + 'documentary.jpg')
        addDir3('[COLOR aqua]נשיונל גיאוגרפיק[/COLOR]','plugin://plugin.video.youtube/kodion/search/query/?q=national%20geographic',35,art + 'documentary.jpg')
        addDir3('[COLOR aqua]Net Geo Wild[/COLOR]','plugin://plugin.video.youtube/kodion/search/query/?q=Net%20Geo%20Wild',35,art + 'documentary.jpg')
        addDir3('[COLOR aqua]דיסקברי[/COLOR]','plugin://plugin.video.youtube/kodion/search/query/?q=discovery',35,art + 'documentary.jpg')
        addDir3('[COLOR aqua]דוקומנטרי BBC[/COLOR]','plugin://plugin.video.youtube/kodion/search/query/?q=bbc%20documentary',35,art + 'documentary.jpg')
        addDir3('[COLOR aqua]סרטוני טבע HD [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=סרטוני טבע HD&search_type=playlist",35,art + 'documentary.jpg')
        addDir3('[COLOR aqua]טבע וחיות בר HD [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=טבע וחיות בר HD&search_type=playlist",35,art + 'documentary.jpg')
        addDir3('[COLOR aqua]אוקיינוס[/COLOR]','plugin://plugin.video.youtube/kodion/search/query/?q=ocean%20documentary',35,art + 'documentary.jpg')
        addDir3('[COLOR aqua]אפריקה[/COLOR]','plugin://plugin.video.youtube/kodion/search/query/?q=africa%20documentary',35,art + 'documentary.jpg')
        #addDir('[COLOR aqua]רוסיה הפראית[/COLOR]','PLql7ZywaMwm0qsDq7eziLHbtmHkD77aCj',1,art + 'documentary.jpg')
        addDir3('[COLOR aqua]מדע[/COLOR]','plugin://plugin.video.youtube/kodion/search/query/?q=science%20documentary',35,art + 'documentary.jpg')
        addDir3('[COLOR aqua]דינוזאורים[/COLOR]','plugin://plugin.video.youtube/kodion/search/query/?q=dinosaur%20documentary',35,art + 'documentary.jpg')
        addDir3('[COLOR aqua]חיות קטלניות[/COLOR]','plugin://plugin.video.youtube/kodion/search/query/?q=deadly%20animals',35,art + 'documentary.jpg')
        addDir3('[COLOR aqua]כרישים[/COLOR]','plugin://plugin.video.youtube/kodion/search/query/?q=sharks%20documentary',35,art + 'documentary.jpg')
        addDir3('[COLOR aqua]נחשים[/COLOR]','plugin://plugin.video.youtube/kodion/search/query/?q=snakes%20documentary',35,art + 'documentary.jpg')        
        addDir3('[COLOR aqua]ציפורים[/COLOR]','plugin://plugin.video.youtube/kodion/search/query/?q=birds%20documentary',35,art + 'documentary.jpg')
        #addDir('[COLOR aqua]תנינים[/COLOR]','PLnzhIyrsnB5YPDK-se-BkGWaDjPER-0jp',1,art + 'documentary.jpg')
        #addDir('[COLOR aqua]דובים[/COLOR]','PLnzhIyrsnB5ZuhAQyz6kzcmlAl_K18Jvl',1,art + 'documentary.jpg')
        #addDir('[COLOR aqua]אריות[/COLOR]','PLnzhIyrsnB5bFPCKp6A5afJiE0S1-s_C6',1,art + 'documentary.jpg')
        #addDir('[COLOR aqua]חרקים[/COLOR]','PL1bLcCen2CCeRW-XeL1Nvgn7hpeSlqab7',1,art + 'documentary.jpg')
        #addDir('[COLOR aqua]צמחים[/COLOR]','PL1bLcCen2CCcObVIYmrFePh4J2oy3ITWJ',1,art + 'documentary.jpg')
        addDir3('[COLOR aqua]איך זה פועל[/COLOR]',"plugin://plugin.video.youtube/playlist/PLLgqOez346ZPcqnmLsDkqr0kPjuRz5Rjo/?page=1",35,art + 'documentary.jpg')
        addDir3('[COLOR aqua]חוצנים[/COLOR]','plugin://plugin.video.youtube/kodion/search/query/?q=aliens%20documentary',35,art + 'documentary.jpg')
        addDir3('[COLOR aqua]קונספירציות לועזית[/COLOR]','plugin://plugin.video.youtube/kodion/search/query/?q=conspiracy%20documentary',35,art + 'documentary.jpg')
        addDir3('[COLOR aqua]מערכת השמש[/COLOR]','plugin://plugin.video.youtube/kodion/search/query/?q=solar%20system%20documentary',35,art + 'documentary.jpg')
        addDir3('[COLOR aqua]חורים שחורים [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=חורים שחורים&search_type=playlist",35,art + 'documentary.jpg')
        #addDir('[COLOR aqua]סיפורים מעוררי השראה[/COLOR]','PLUkdT9ljJ1cYE-Mxn43WRf_0Gq4oWa-QD',1,art + 'documentary.jpg')		
        #addDir('[COLOR aqua]חיות מחמד יוצאות דופן[/COLOR]','PLUkdT9ljJ1caovAwonqPel9hYzk8V1j4l',1,art + 'documentary.jpg')		
        addDir3('[COLOR aqua]היסטוריה[/COLOR]','plugin://plugin.video.youtube/kodion/search/query/?q=history%20documentary',35,art + 'documentary.jpg')
        #addDir('[COLOR aqua]ערוץ ההיסטוריה DECISIVE BATTLES[/COLOR]','PL3H6z037pboH81MoHl8zcbugf2onvFcDc',1,art + 'documentary.jpg')
        #addDir('[COLOR aqua]ערוץ ההיסטוריה THE REAL WILD WEST[/COLOR]','PL3H6z037pboG9_flx9II9XMO5VE_1qHtR',1,art + 'documentary.jpg')
        #addDir('[COLOR aqua]ערוץ ההיסטוריה The Conquerors[/COLOR]','PLSBILXkL0K2tuApKAbXqwkoRgkq2ixifw',1,art + 'documentary.jpg')
		
def Musicy():
        addDir('[COLOR aqua] מוזיקה מהארץ ומהעולם [/COLOR]','url',98765199,art + 'Music.png')
        addDir('[COLOR aqua]הופעות חיות [/COLOR]','url',9876516,art + 'liveshows.png')
        addDir3('[COLOR aqua]מוזיקה ישראלית[/COLOR]','plugin://plugin.video.youtube/kodion/search/query/?q=%d7%9e%d7%95%d7%96%d7%99%d7%a7%d7%94%20%d7%99%d7%a9%d7%a8%d7%90%d7%9c%d7%99%d7%aa&search_type=playlist',35,art + 'Music.png')
        addDir3('[COLOR aqua]מוזיקה לועזית[/COLOR]','plugin://plugin.video.youtube/kodion/search/query/?q=%d7%9e%d7%95%d7%96%d7%99%d7%a7%d7%94%20%d7%9c%d7%95%d7%a2%d7%96%d7%99%d7%aa&search_type=playlist',35,art + 'Music.png')
        addDir3('[COLOR aqua]שירים ישראליים מכל הזמנים [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=שירים ישראליים מכל הזמנים&search_type=playlist",35,art + 'Music.png')
        #addDir('[COLOR aqua]שירים ישראליים מרגשים[/COLOR]','PLryjW6BWLS1Q_xeVOlPfXJF4S3G0purex',1,art + 'Music.png')
        addDir3('[COLOR aqua]דאנס מזרחי[/COLOR]','plugin://plugin.video.youtube/kodion/search/query/?q=%d7%93%d7%90%d7%a0%d7%a1%20%d7%9e%d7%96%d7%a8%d7%97%d7%99',35,art + 'Music.png')
        addDir3('[COLOR aqua]מזרחית קצבית [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=מזרחית קצבית&search_type=playlist",35,art + 'Music.png')
        #addDir('[COLOR aqua]טראקים לחדר כושר[/COLOR]','PL9239ABA016845864',1,art + 'Music.png')
        #addDir('[COLOR aqua]פלייליסט אירובי[/COLOR]','PL1oz4IM59QGMmlAYTP2d1l9GeV4TS0hXV',1,art + 'Music.png')
        #addDir('[COLOR aqua]סרטונים חדשים[/COLOR]','PLrEnWoR732-D67iteOI6DPdJH1opjAuJt',1,art + 'Music.png')
        #addDir('[COLOR aqua]סרטוני וידאו פופולריים[/COLOR]','PLFgquLnL59alCl_2TQvOiD5Vgm1hCaGSI',1,art + 'Music.png')
        addDir3('[COLOR aqua]Billboard[/COLOR]','plugin://plugin.video.youtube/kodion/search/query/?q=Billboard',35,art + 'Music.png')
        addDir3('[COLOR aqua]Mtv[/COLOR]','plugin://plugin.video.youtube/kodion/search/query/?q=mtv&search_type=playlist',35,art + 'Music.png')
        addDir3('[COLOR aqua]Vevo [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=Vevo&search_type=playlist",35,art + 'Music.png')
        addDir3('[COLOR aqua]שנות ה 80&90[/COLOR]','plugin://plugin.video.youtube/kodion/search/query/?q=80s%20music&search_type=playlist',35,art + 'Music.png')
        #addDir('[COLOR aqua]שנות ה 80&90[/COLOR]','PL3485902CC4FB6C67',1,art + 'Music.png')
        addDir3('[COLOR aqua]להיטי שנות ה 70[/COLOR]',"plugin://plugin.video.youtube/playlist/PLGBuKfnErZlAkaUUy57-mR97f8SBgMNHh/?page=1",35,art + 'Music.png')
        addDir3('[COLOR aqua]להיטי שנות ה 60[/COLOR]',"plugin://plugin.video.youtube/playlist/PLhg3Za9X1ghLtZHr_OUp3Q_KK7ZWW9NtZ/?page=1",35,art + 'Music.png')
        addDir3('[COLOR aqua]להיטי שנות ה 50[/COLOR]',"plugin://plugin.video.youtube/playlist/PLdwHUKkVU9r-FyFfee5SfxMu8FONV3-7I/?page=1",35,art + 'Music.png')
        #addDir('[COLOR aqua]להיטי קאנטרי[/COLOR]','PL2BN1Zd8U_MsyMeK8r9Vdv1lnQGtoJaSa',1,art + 'Music.png')
		
def travely():

        addDir3('[COLOR aqua]ערוץ הטיולים - לטייל[/COLOR]',"plugin://plugin.video.youtube/playlist/PLeh1TPHGKHcC0frpxT30gpX32Mc1DMStx/?page=1",35,art + 'travel.png')
        addDir3('[COLOR aqua]המדריך לתייר בגלקסיה[/COLOR]',"plugin://plugin.video.youtube/playlist/PLeh1TPHGKHcAriEIJEPLnZ7Qsm3Fh6ELx/?page=1",35,art + 'travel.png')
        addDir3('[COLOR aqua]אוכל רחוב מסביב לעולם [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=אוכל רחוב מסביב לעולם&search_type=playlist",35,art + 'travel.png')
        addDir3('[COLOR aqua]סקי וסנובורד[/COLOR]',"plugin://plugin.video.youtube/playlist/PLFZHg-6S5_GcrVsP97cT7KoYQQD5vNEQr/?page=1",35,art + 'travel.png')
        addDir3('[COLOR aqua]טיולי משפחות[/COLOR]',"plugin://plugin.video.youtube/playlist/PLFZHg-6S5_GfMOlbWErniSqxw9ygllSGL/?page=1",35,art + 'travel.png')
        addDir3('[COLOR aqua]טיולים בעולם[/COLOR]',"plugin://plugin.video.youtube/playlist/PLFZHg-6S5_GcIWZJp6-o4lo4vSuDQrrPt/?page=1",35,art + 'travel.png')
        addDir3('[COLOR aqua]מדריכי טיולים - אשת טורס[/COLOR]',"plugin://plugin.video.youtube/playlist/PL1E93715FC3C00F68/?page=1",35,art + 'travel.png')
        addDir3('[COLOR aqua]עצות המומחים - כל מה שצריך לדעת על ציוד טיולים[/COLOR]',"plugin://plugin.video.youtube/playlist/PLFZHg-6S5_GcQdP7V_Q3-6HF9pTUWQ8I_/?page=1",35,art + 'travel.png')
        addDir3('[COLOR aqua]'+translate(70003)+'[/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=המסע המופלא של אהרוני וגידי&search_type=playlist",35,art + 'travel.png')
        addDir3('[COLOR aqua]'+translate(70004)+'[/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=אוכל רחוב&search_type=playlist",35,art + 'travel.png')
        addDir3('[COLOR aqua]ערים בעולם - מדריך טיולים[/COLOR]',"plugin://plugin.video.youtube/playlist/PLe9OS0jiMKcJ28LhxyvJzHrVGfI2AJe-q/?page=1",35,art + 'travel.png')
        addDir3('[COLOR aqua]אירופה - מדריך טיולים[/COLOR]',"plugin://plugin.video.youtube/playlist/PLDlvzhdA4-Pdv-zwkSUGr5-Bu_nn_33bP/?page=1",35,art + 'travel.png')
        addDir3('[COLOR aqua]צפון אמריקה - מדריך טיולים[/COLOR]',"plugin://plugin.video.youtube/playlist/PLdgCSoJzrmKHhvEWqmb3-1tUQmT8ZWBrv/?page=1",35,art + 'travel.png')
        addDir3('[COLOR aqua]אפריקה - מדריך טיולים[/COLOR]',"plugin://plugin.video.youtube/playlist/PLDlvzhdA4-PeKVe1Tyf8EZYhxCunhYwgG/?page=1",35,art + 'travel.png')
        addDir3('[COLOR aqua]יפן - מדריך טיולים[/COLOR]',"plugin://plugin.video.youtube/playlist/PL14F9F774CE8798C3/?page=1",35,art + 'travel.png')
        addDir3('[COLOR aqua]ארצות הברית - מדריך טיולים[/COLOR]',"plugin://plugin.video.youtube/playlist/PLOVadUHX1B-Kv1gRgHpJoe33hGodcPi8R/?page=1",35,art + 'travel.png')
        addDir3('[COLOR aqua]מדריך טיולים לערים שונות בעולם[/COLOR]',"plugin://plugin.video.youtube/playlist/PL-NQ0KYodq5MkFgQJEpWTGELcEaLIJdVx/?page=1",35,art + 'travel.png')
        addDir3('[COLOR aqua]רומא - מדריך טיולים[/COLOR]',"plugin://plugin.video.youtube/playlist/PLEC3E8FCF38E57252/?page=1",35,art + 'travel.png')
        addDir3('[COLOR aqua]סרטונים פופולריים – Travel Channel[/COLOR]',"plugin://plugin.video.youtube/playlist/PL_xzw4jKGLrlQKx7hvUF5B5FvVhzUtvw6/?page=1",35,art + 'travel.png')
        addDir3('[COLOR aqua]אוכל ביזארי עם Andrew Zimmern[/COLOR]',"plugin://plugin.video.youtube/playlist/PL7Yaf7nQHP3CM6bLT6acdsOhQoKCmb75c/?page=1",35,art + 'travel.png')
        addDir3('[COLOR aqua]סרטונים פופולריים – Aerial America[/COLOR]',"plugin://plugin.video.youtube/playlist/PLnr8iIChmNnEy89DZIe6DKSeS4qKAe1hx/?page=1",35,art + 'travel.png')
        addDir3('[COLOR aqua]סרטונים פופולריים – Hotel Impossible[/COLOR]',"plugin://plugin.video.youtube/playlist/PLF_H8SZXratCdL4Mv3fHRVfnj2SYw3bxr/?page=1",35,art + 'travel.png')
		
def cookingy():

        addDir3('[COLOR aqua]מתכונים כלליים[/COLOR]',"plugin://plugin.video.youtube/playlist/PLF685A5B80B86FE3B/?page=1",35,art + 'cooking.png')
        addDir3('[COLOR aqua]מתכונים כשרים[/COLOR]',"plugin://plugin.video.youtube/playlist/PL3zcxKFd7HIKL3oSXq6rCH-fvFGCaOaS9/?page=1",35,art + 'cooking.png')
        addDir3('[COLOR aqua]מתכונים. מטבח יהודי ומזרח ים תיכוני[/COLOR]',"plugin://plugin.video.youtube/playlist/PLRUtxvlnaqwx3KugKPtd4C3Iexv0Ee5U3/?page=1",35,art + 'cooking.png')
        addDir3('[COLOR aqua]'+translate(70002)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLLttfoK87AdWKMbzk5YZ1Zi3hMYGr6xrE/?page=1",35,art + 'cooking.png')
        addDir3('[COLOR aqua]'+translate(70004)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLeh1TPHGKHcB3YRXfu8VHylS9ghgpoD3z/?page=1",35,art + 'cooking.png')       
        addDir3('[COLOR aqua]סודות מתוקים [/COLOR]',"plugin://plugin.video.youtube/playlist/PLasHtCerUASTvxNs2P5LFzuF3_CnsYdTF/?page=1",35,art + 'cooking.png')
        addDir3('[COLOR aqua]משה שגב במטבח[/COLOR]',"plugin://plugin.video.youtube/playlist/PLasHtCerUASQ-_205phAMWJFRJfzQ6JYE/?page=1",35,art + 'cooking.png')         
        addDir3('[COLOR aqua]מיקי שמו [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=מיקי שמו&search_type=playlist",35,art + 'cooking.png')
        addDir3('[COLOR aqua]בישולים[/COLOR]',"plugin://plugin.video.youtube/playlist/PLkSacTgmGKr6a6sPE1F7q3VF7T00lffQc/?page=1",35,art + 'cooking.png')
        addDir3('[COLOR aqua]בישולים 2[/COLOR]',"plugin://plugin.video.youtube/playlist/PLdDyYBhRKiyG21-epuoI57b7zBfAyQcvI/?page=1",35,art + 'cooking.png') 
      

        addDir3('[COLOR aqua]לאון אל דנטה[/COLOR]',"plugin://plugin.video.youtube/playlist/PL8jMo70ebRM7nnRez1MyfKBFLTj9jzl1V/?page=1",35,art + 'cooking.png')
        addDir3('[COLOR aqua]במטבח עם אמא[/COLOR]',"plugin://plugin.video.youtube/playlist/PL8jMo70ebRM6gYuy9d7yoPLTGg1asK78w/?page=1",35,art + 'cooking.png')
        addDir3('[COLOR aqua]מיקי שמו עושה בית ספר - עונה ראשונה[/COLOR]',"plugin://plugin.video.youtube/playlist/PL8jMo70ebRM7tvFCZsiXhakIsbDwHOe9c/?page=1",35,art + 'cooking.png')         
        addDir3('[COLOR aqua]מועדון ארוחת הבוקר עם אביב משה[/COLOR]',"plugin://plugin.video.youtube/playlist/PL8jMo70ebRM6CAq8sKdjfI4_N3qUO5U1j/?page=1",35,art + 'cooking.png')
        addDir3('[COLOR aqua]פשוט לאפות[/COLOR]',"plugin://plugin.video.youtube/playlist/PL8jMo70ebRM6aT0ZciSlv_YhP2Kjp1tuk/?page=1",35,art + 'cooking.png')
        addDir3('[COLOR aqua]המטבחון של ירון[/COLOR]',"plugin://plugin.video.youtube/playlist/PL156601B302C8F462/?page=1",35,art + 'cooking.png')
		
def liveshowsy():
        addDir3('[COLOR aqua]זמרים ישראליים[/COLOR]',"plugin://plugin.video.youtube/playlist/PLnzhIyrsnB5Ydr8diBFqJ368vCrqAlfbS/?page=1",35,art + 'liveshows.png')
        addDir3('[COLOR aqua]הופעות חיות לועזית[/COLOR]','plugin://plugin.video.youtube/kodion/search/query/?q=live%20music%20concerts',35,art + 'liveshows.png')
        addDir3('[COLOR aqua]זמרים לועזית[/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=זמרים לועזית/?page=1",35,art + 'liveshows.png')
        addDir3('[COLOR aqua]מוזיקה אלקטרונית[/COLOR]','plugin://plugin.video.youtube/kodion/search/query/?q=live%20music%20concerts%20electro',35,art + 'liveshows.png')
        addDir3('[COLOR aqua]להקות רוק[/COLOR]','plugin://plugin.video.youtube/kodion/search/query/?q=live%20rock%20music%20concerts',35,art + 'liveshows.png')
        addDir3('[COLOR aqua]פופ[/COLOR]','plugin://plugin.video.youtube/kodion/search/query/?q=live%20pop%20music%20concerts',35,art + 'liveshows.png')
        addDir3('[COLOR aqua]שנות השמונים[/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=זמרים לועזית שנות ה 80&search_type=playlist",35,art + '80.jpg')
        addDir3('[COLOR aqua]שנות התשעים [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=זמרים לועזית שנות ה 90&search_type=playlist",35,art + '90.jpg')
        addDir3('[COLOR aqua]טראנס [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=טראנס&search_type=playlist",35,art + 'liveshows.png')
        addDir3('[COLOR aqua]אופרה וקונצרטים [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=אופרה וקונצרטים&search_type=playlist",35,art + 'liveshows.png')
        #addDir('[COLOR aqua]קאנטרי[/COLOR]','PLnzhIyrsnB5bt4BgqZt_p5qs3sewWKYMs',1,art + 'liveshows.png')
        addDir3('[COLOR aqua]סול [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=סול&search_type=playlist",35,art + 'liveshows.png.jpg')
        addDir3('[COLOR aqua]בלוז [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=בלוז&search_type=playlist",35,art + 'liveshows.png.jpg')
        addDir3('[COLOR aqua]ראפ & היפ הופ [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=ראפ & היפ הופ&search_type=playlist",35,art + 'liveshows.png.jpg')
        addDir3('[COLOR aqua]גאז [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=גאז&search_type=playlist",35,art + 'liveshows.png.jpg')
		
def Sportsy():     
        addDir('[COLOR aqua]SPORTEXTREME[/COLOR]','url',9876510011,'http://extremesportsphilippines.com/wp-content/uploads/2017/09/cropped-extreme-sports-philippines-logo.png')
        addDir('[COLOR aqua]POLARIS[/COLOR]','url',9876510008,'https://www.psyshop.com/img/soc1dw081_b.jpg')
        addDir('[COLOR aqua]ספורט דוקומנטרי [/COLOR]','url',9876520011,'https://images.squarespace-cdn.com/content/v1/54ac152ee4b0a068ceceeb7a/1421701286623-IWCUL6YSXVNJ37TROLRZ/ke17ZwdGBToddI8pDm48kGfiFqkITS6axXxhYYUCnlRZw-zPPgdn4jUwVcJE1ZvWQUxwkmyExglNqGp0IvTJZUJFbgE-7XRK3dMEBRBhUpx1B3uKuIxKkeNobmVrkfsvhi7vfNIYPwuNoe0YQqN5qRcQyCP0lZkCSDZ8KLElTzs/Film_Squares_002.jpg')   
        addDir('[COLOR aqua]כדורסל[/COLOR]','url',9876532,art + 'bas.jpg')	
        addDir('[COLOR aqua]כדורגל[/COLOR]','url',9876533,art + 'Soccer.jpg')
        addDir('[COLOR aqua]איגרוף[/COLOR]','url',9876534,'https://toppng.com/uploads/preview/running-vector-png-image-illustration-sport-shoes-box-11563270780mksrhmytod.png')

        addDir3('[COLOR aqua]קרבות מלאים WWE [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q= WWE&search_type=playlist",35,art + 'Sports.png')
        addDir3('[COLOR aqua]קרבות UFC [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q= UFC&search_type=playlist",35,art + 'Sports.png')
        addDir3('[COLOR aqua]פיתוח גוף[/COLOR]',"plugin://plugin.video.youtube/playlist/PLYMK_Nbs-rsvOuko4Hqv4Uw6NF2Q3-eCP/?page=1",35,'https://lh3.googleusercontent.com/QT50L302rYQQkxsjNbw-RZMAnIExQVrfdqy8UazD1U1QqlIr6NR3pR83BJUpIjS4CME')
        addDir3('[COLOR aqua]טניס[/COLOR]',"plugin://plugin.video.youtube/playlist/PL1bLcCen2CCdPEMJ8B5S6Z9RzLjMnFNvT/?page=1",35,art + 'Sports.png')	
        #addDir('[COLOR aqua]אתלטיקה קלה[/COLOR]','PLnzhIyrsnB5aAsPRtalXMLlCW8GflCkUY',32,art + 'Sports.png')
        #addDir('[COLOR aqua]כדורעף[/COLOR]','PLnzhIyrsnB5aAsPRtalXMLlCW8GflCkUY',32,art + 'Sports.png')	
        #addDir('[COLOR aqua]כדוריד[/COLOR]','PLnzhIyrsnB5aAsPRtalXMLlCW8GflCkUY',32,art + 'Sports.png')
        #addDir('[COLOR aqua]שחיה[/COLOR]','PLnzhIyrsnB5aAsPRtalXMLlCW8GflCkUY',32,art + 'Sports.png')
        #addDir('[COLOR aqua]כושר ואירובי[/COLOR]','PLnzhIyrsnB5aAsPRtalXMLlCW8GflCkUY',32,art + 'Sports.png')
        #addDir('[COLOR aqua]מרוצי מכוניות[/COLOR]','PLnzhIyrsnB5aAsPRtalXMLlCW8GflCkUY',32,art + 'Sports.png')
        #addDir('[COLOR aqua]ספורט אתגרי[/COLOR]','PLnzhIyrsnB5aAsPRtalXMLlCW8GflCkUY',32,art + 'Sports.png')		
       		
		

      
		
def baskety():        
        addDir('[COLOR aqua]NBA[/COLOR]','url',9876531,art + 'Sports.png')	
        addDir3('[COLOR aqua]משחקים מלאים NCAA[/COLOR]',"plugin://plugin.video.youtube/playlist/PL6Bd4hQKgOo81RSUYKV9ko4KzNFPoKgVB/?page=1",35,art + 'Sports.png')
        addDir3('[COLOR aqua]משחקי כדורסל מלאים ישראל [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=משחקי כדורסל מלאים ישראל&search_type=playlist",35,art + 'Sports.png')
        addDir3('[COLOR aqua]כדורסל מכבי תל אביב משחקים מלאים [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=כדורסל מכבי תל אביב משחקים מלאים&search_type=playlist",35,art + 'Sports.png')
        addDir3('[COLOR aqua]כדורסל מכבי תל אביב משחקים מלאים[/COLOR]',"plugin://plugin.video.youtube/playlist/PLGU699iLiZVtqvNmge4rcS10ZBvsZ4CIU/?page=1",35,art + 'Sports.png')
        addDir3('[COLOR aqua]כדורסל מכבי תל אביב רגעים גדולים  [/COLOR]',"plugin://plugin.video.youtube/channel/UCVlaHqhBqzBD70sBUpjzXOA/playlist/PLD209279A5534F91E/",35,art + 'Sports.png')
        addDir3('[COLOR aqua]הפועל ירושלים משחקים מלאים[/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=הפועל ירושלים כדורסל משחקים מלאים &search_type=playlist",35,art + 'Sports.png')


def soccery():        
        addDir3('[COLOR aqua]מנהלת הליגות לכדורגל [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=מנהלת הליגות לכדורגל ipfl&search_type=playlist",35,art + 'Soccer.jpg')
        addDir3('[COLOR aqua]ספורט ישראלי [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=תקצירי ספורט באיכות גבוהה&search_type=playlist",35,art + 'Soccer.jpg')
        addDir3('[COLOR aqua]ליגת העל 2019/20 תקצירים [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=ליגת העל 2019/20 תקצירים&search_type=playlist",35,art + '30034.jpg')	       	
        addDir3('[COLOR aqua]ליגת העל 2019/20  משחקים מלאים [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=ליגת העל 2019/20  משחקים מלאים&search_type=playlist",35,art + '30034.jpg')
        addDir3('[COLOR aqua]ליגת העל 2019-20 - משחקים מלאים ספורט 1 [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=ליגת העל 2019-20 - משחקים מלאים ספורט 1 &search_type=playlist",35,art + '30034.jpg')
        addDir3('[COLOR aqua]גביע המדינה 2015-16 - משחקים מלאים ספורט 1[/COLOR]',"plugin://plugin.video.youtube/playlist/PLTu-AmawV8D1AFZcpPwWw6FbvFVAXTSLD/?page=1",35,art + 'Soccer.jpg')

        addDir3('[COLOR aqua]ספורט ONE מכבי חיפה[/COLOR]',"plugin://plugin.video.youtube/playlist/PLTu-AmawV8D2yNMxtKOmc1leheIrXgbfp/?page=1",35,art + 'Soccer.jpg')
        addDir3('[COLOR aqua]ספורט ONE מכבי תל אביב[/COLOR]',"plugin://plugin.video.youtube/playlist/PLTu-AmawV8D1I2RLIuqCgn4ivpV5wqPjO/?page=1",35,art + 'Soccer.jpg')
        addDir3('[COLOR aqua]ספורט ONE הפועל תל אביב[/COLOR]',"plugin://plugin.video.youtube/playlist/PLTu-AmawV8D0C5KPwVlurnJP4KkjIkgMo/?page=1",35,art + 'Soccer.jpg')
        addDir3('[COLOR aqua]ספורט ONE ביתר ירושלים[/COLOR]',"plugin://plugin.video.youtube/playlist/PLTu-AmawV8D3b16u3378Sx6xOlGzc5ZDj/?page=1",35,art + 'Soccer.jpg')
        addDir3('[COLOR aqua]ספורט ONE מכבי נתניה[/COLOR]',"plugin://plugin.video.youtube/playlist/PLTu-AmawV8D1mWDpHPOD8qts2GoSin1xU/?page=1",35,art + 'Soccer.jpg')
        addDir3('[COLOR aqua]ספורט ONE מכבי פתח תקווה[/COLOR]',"plugin://plugin.video.youtube/playlist/PLTu-AmawV8D1usI_4UHXslajV6oBm3ibo/?page=1",35,art + 'Soccer.jpg')
		
def NBAy():
        addDir3('[COLOR aqua]NBA-כללי [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=NBA-כדורסל &search_type=playlist",35,'https://steemitimages.com/DQmcKBum4urqE9n83hDYNP1LUeKYvk2SG631CnysukpxbTD/nba.png')
        addDir3('[COLOR aqua]2019-20 Top 10s of the Week[/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=2019-20 Top 10s of the Week &search_type=playlist",35,'https://steemitimages.com/DQmcKBum4urqE9n83hDYNP1LUeKYvk2SG631CnysukpxbTD/nba.png')
        addDir3('[COLOR aqua]2020 All-Star Top 10[/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=2020 All-Star Top 10 &search_type=playlist",35,'https://steemitimages.com/DQmcKBum4urqE9n83hDYNP1LUeKYvk2SG631CnysukpxbTD/nba.png')
        addDir3('[COLOR aqua]Nba Hardwood Classic Games[/COLOR]',"plugin://plugin.video.youtube/playlist/PLgaLmcSQmPmypokd-3BPPJqtKjzgRdRZu/?page=1",35,'https://steemitimages.com/DQmcKBum4urqE9n83hDYNP1LUeKYvk2SG631CnysukpxbTD/nba.png')
        addDir3('[COLOR aqua]Inside the NBA Funniest Moments[/COLOR]',"plugin://plugin.video.youtube/playlist/PLFHl_hR47OGIqrn4A1tlQmteFKBKTskGx/?page=1",35,'https://steemitimages.com/DQmcKBum4urqE9n83hDYNP1LUeKYvk2SG631CnysukpxbTD/nba.png')

        addDir3('[COLOR aqua]inside the nba - 2019-2020 NBA Season[/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=inside the nba - 2019-2020 NBA Season &search_type=playlist",35,'https://steemitimages.com/DQmcKBum4urqE9n83hDYNP1LUeKYvk2SG631CnysukpxbTD/nba.png')
        addDir3('[COLOR aqua]inside the nba - 2015-2016 NBA Season[/COLOR]',"plugin://plugin.video.youtube/playlist/PL7XTBoSLULm16wQ6MiXEoRc9oGuj0geNZ/?page=1",35,'https://steemitimages.com/DQmcKBum4urqE9n83hDYNP1LUeKYvk2SG631CnysukpxbTD/nba.png')
        addDir3('[COLOR aqua]המשחקים הגדולים ביותר של NBA[/COLOR]',"plugin://plugin.video.youtube/playlist/PL0k1yKb93AELcXLQt4lkPURg-w-DNZNfz/?page=1",35,'https://steemitimages.com/DQmcKBum4urqE9n83hDYNP1LUeKYvk2SG631CnysukpxbTD/nba.png')
        addDir3('[COLOR aqua]סרטונים פופולריים – דראפט ה-NBA & 2020 NBA draft[/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=NBA  2020 NBA draft&search_type=playlist",35,'https://steemitimages.com/DQmcKBum4urqE9n83hDYNP1LUeKYvk2SG631CnysukpxbTD/nba.png')

def boxy():

        addDir3('[COLOR aqua]אגרוף - TOP 10[/COLOR]',"plugin://plugin.video.youtube/playlist/PL3mFKGDe2IPs5Zx51hw0jEmmL_CFsu2az/?page=1",35,'https://toppng.com/uploads/preview/running-vector-png-image-illustration-sport-shoes-box-11563270780mksrhmytod.png')

        addDir3('[COLOR aqua]קרבות אגרוף קלאסיים[/COLOR]',"plugin://plugin.video.youtube/playlist/PL0i1N-wlFfiDEdYCjp6nvHR-sEpJGBGXZ/?page=1",35,'https://toppng.com/uploads/preview/running-vector-png-image-illustration-sport-shoes-box-11563270780mksrhmytod.png')
        addDir3('[COLOR aqua]קרבות גדולים[/COLOR]',"plugin://plugin.video.youtube/playlist/PLQcJnkxSzA8ypDBwz9wbP87MN4dNwklBO/?page=1",35,'https://toppng.com/uploads/preview/running-vector-png-image-illustration-sport-shoes-box-11563270780mksrhmytod.png')
        addDir3('[COLOR aqua]קרבות מלאים 1[/COLOR]',"plugin://plugin.video.youtube/playlist/PL-KAIrL6czM_bnmP8z41QdEVCXcj0UjEA/?page=1",35,'https://toppng.com/uploads/preview/running-vector-png-image-illustration-sport-shoes-box-11563270780mksrhmytod.png')
        addDir3('[COLOR aqua]קרבות מלאים 2[/COLOR]',"plugin://plugin.video.youtube/playlist/PLF3785E12178259EE/?page=1",35,'https://toppng.com/uploads/preview/running-vector-png-image-illustration-sport-shoes-box-11563270780mksrhmytod.png')
        addDir3('[COLOR aqua]המלחמות הגדולות ביותר באגרוף[/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=קרבות איגרוף פופלרי בעולם &search_type=playlist/?page=1",35,'https://toppng.com/uploads/preview/running-vector-png-image-illustration-sport-shoes-box-11563270780mksrhmytod.png')


def Documentarysporty():



        addDir('[COLOR aqua]דרך (יוטיוב) [/COLOR]','url',9876520011,'https://images.squarespace-cdn.com/content/v1/54ac152ee4b0a068ceceeb7a/1421701286623-IWCUL6YSXVNJ37TROLRZ/ke17ZwdGBToddI8pDm48kGfiFqkITS6axXxhYYUCnlRZw-zPPgdn4jUwVcJE1ZvWQUxwkmyExglNqGp0IvTJZUJFbgE-7XRK3dMEBRBhUpx1B3uKuIxKkeNobmVrkfsvhi7vfNIYPwuNoe0YQqN5qRcQyCP0lZkCSDZ8KLElTzs/Film_Squares_002.jpg')



def Documentarysport2y():



        addDir3('[B][COLOR]Serviceil[/COLOR][/B] [COLOR FFffc4227b][B]Basketball[/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=documentary%20basketball/?page=1",35,'https://images.squarespace-cdn.com/content/v1/54ac152ee4b0a068ceceeb7a/1421701286623-IWCUL6YSXVNJ37TROLRZ/ke17ZwdGBToddI8pDm48kGfiFqkITS6axXxhYYUCnlRZw-zPPgdn4jUwVcJE1ZvWQUxwkmyExglNqGp0IvTJZUJFbgE-7XRK3dMEBRBhUpx1B3uKuIxKkeNobmVrkfsvhi7vfNIYPwuNoe0YQqN5qRcQyCP0lZkCSDZ8KLElTzs/Film_Squares_002.jpg')

        addDir3('[B][COLOR]Serviceil[/COLOR][/B] [COLOR FFff059229][B]Football[/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=documentary%20football/?page=1",35,'https://images.squarespace-cdn.com/content/v1/54ac152ee4b0a068ceceeb7a/1421701286623-IWCUL6YSXVNJ37TROLRZ/ke17ZwdGBToddI8pDm48kGfiFqkITS6axXxhYYUCnlRZw-zPPgdn4jUwVcJE1ZvWQUxwkmyExglNqGp0IvTJZUJFbgE-7XRK3dMEBRBhUpx1B3uKuIxKkeNobmVrkfsvhi7vfNIYPwuNoe0YQqN5qRcQyCP0lZkCSDZ8KLElTzs/Film_Squares_002.jpg')

        addDir3('[B][COLOR]Serviceil[/COLOR][/B] [COLOR FFff88acb2][B]Rugby (Real Football)[/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=documentary%20rugby/?page=1",35,'https://images.squarespace-cdn.com/content/v1/54ac152ee4b0a068ceceeb7a/1421701286623-IWCUL6YSXVNJ37TROLRZ/ke17ZwdGBToddI8pDm48kGfiFqkITS6axXxhYYUCnlRZw-zPPgdn4jUwVcJE1ZvWQUxwkmyExglNqGp0IvTJZUJFbgE-7XRK3dMEBRBhUpx1B3uKuIxKkeNobmVrkfsvhi7vfNIYPwuNoe0YQqN5qRcQyCP0lZkCSDZ8KLElTzs/Film_Squares_002.jpg')

        addDir3('[B][COLOR]Serviceil[/COLOR][/B] [COLOR FFffa987d9][B]Baseball[/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=documentary%20baseball/?page=1",35,'https://images.squarespace-cdn.com/content/v1/54ac152ee4b0a068ceceeb7a/1421701286623-IWCUL6YSXVNJ37TROLRZ/ke17ZwdGBToddI8pDm48kGfiFqkITS6axXxhYYUCnlRZw-zPPgdn4jUwVcJE1ZvWQUxwkmyExglNqGp0IvTJZUJFbgE-7XRK3dMEBRBhUpx1B3uKuIxKkeNobmVrkfsvhi7vfNIYPwuNoe0YQqN5qRcQyCP0lZkCSDZ8KLElTzs/Film_Squares_002.jpg')

        addDir3('[B][COLOR]Serviceil[/COLOR][/B] [COLOR FFff0240ac][B]Ice Hockey[/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=documentary%20ice%20hockey/?page=1",35,'https://images.squarespace-cdn.com/content/v1/54ac152ee4b0a068ceceeb7a/1421701286623-IWCUL6YSXVNJ37TROLRZ/ke17ZwdGBToddI8pDm48kGfiFqkITS6axXxhYYUCnlRZw-zPPgdn4jUwVcJE1ZvWQUxwkmyExglNqGp0IvTJZUJFbgE-7XRK3dMEBRBhUpx1B3uKuIxKkeNobmVrkfsvhi7vfNIYPwuNoe0YQqN5qRcQyCP0lZkCSDZ8KLElTzs/Film_Squares_002.jpg')

        addDir3('[B][COLOR]Serviceil[/COLOR][/B] [COLOR FFffdf265e][B]Tennis[/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=documentary%20tennis/?page=1",35,'https://images.squarespace-cdn.com/content/v1/54ac152ee4b0a068ceceeb7a/1421701286623-IWCUL6YSXVNJ37TROLRZ/ke17ZwdGBToddI8pDm48kGfiFqkITS6axXxhYYUCnlRZw-zPPgdn4jUwVcJE1ZvWQUxwkmyExglNqGp0IvTJZUJFbgE-7XRK3dMEBRBhUpx1B3uKuIxKkeNobmVrkfsvhi7vfNIYPwuNoe0YQqN5qRcQyCP0lZkCSDZ8KLElTzs/Film_Squares_002.jpg')

        addDir3('[B][COLOR]Serviceil[/COLOR][/B] [COLOR FFff06d364][B]Golf[/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=documentary%20golf/?page=1",35,'https://images.squarespace-cdn.com/content/v1/54ac152ee4b0a068ceceeb7a/1421701286623-IWCUL6YSXVNJ37TROLRZ/ke17ZwdGBToddI8pDm48kGfiFqkITS6axXxhYYUCnlRZw-zPPgdn4jUwVcJE1ZvWQUxwkmyExglNqGp0IvTJZUJFbgE-7XRK3dMEBRBhUpx1B3uKuIxKkeNobmVrkfsvhi7vfNIYPwuNoe0YQqN5qRcQyCP0lZkCSDZ8KLElTzs/Film_Squares_002.jpg')

        addDir3('[B][COLOR]Serviceil[/COLOR][/B] [COLOR FFff940aee][B]Boxing[/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=documentary%20boxing/?page=1",35,'https://images.squarespace-cdn.com/content/v1/54ac152ee4b0a068ceceeb7a/1421701286623-IWCUL6YSXVNJ37TROLRZ/ke17ZwdGBToddI8pDm48kGfiFqkITS6axXxhYYUCnlRZw-zPPgdn4jUwVcJE1ZvWQUxwkmyExglNqGp0IvTJZUJFbgE-7XRK3dMEBRBhUpx1B3uKuIxKkeNobmVrkfsvhi7vfNIYPwuNoe0YQqN5qRcQyCP0lZkCSDZ8KLElTzs/Film_Squares_002.jpg')

        addDir3('[B][COLOR]Serviceil[/COLOR][/B] [COLOR FFff6a4093][B]UFC[/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=documentary%20ufc/?page=1",35,'https://images.squarespace-cdn.com/content/v1/54ac152ee4b0a068ceceeb7a/1421701286623-IWCUL6YSXVNJ37TROLRZ/ke17ZwdGBToddI8pDm48kGfiFqkITS6axXxhYYUCnlRZw-zPPgdn4jUwVcJE1ZvWQUxwkmyExglNqGp0IvTJZUJFbgE-7XRK3dMEBRBhUpx1B3uKuIxKkeNobmVrkfsvhi7vfNIYPwuNoe0YQqN5qRcQyCP0lZkCSDZ8KLElTzs/Film_Squares_002.jpg')

        addDir3('[B][COLOR]Serviceil[/COLOR][/B] [COLOR FFff698fdc][B]Wrestling[/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=documentary%20wwe/?page=1",35,'https://images.squarespace-cdn.com/content/v1/54ac152ee4b0a068ceceeb7a/1421701286623-IWCUL6YSXVNJ37TROLRZ/ke17ZwdGBToddI8pDm48kGfiFqkITS6axXxhYYUCnlRZw-zPPgdn4jUwVcJE1ZvWQUxwkmyExglNqGp0IvTJZUJFbgE-7XRK3dMEBRBhUpx1B3uKuIxKkeNobmVrkfsvhi7vfNIYPwuNoe0YQqN5qRcQyCP0lZkCSDZ8KLElTzs/Film_Squares_002.jpg')

        addDir3('[B][COLOR]Serviceil[/COLOR][/B] [COLOR FFff65b49a][B]Nascar[/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=documentary%20nascar/?page=1",35,'https://images.squarespace-cdn.com/content/v1/54ac152ee4b0a068ceceeb7a/1421701286623-IWCUL6YSXVNJ37TROLRZ/ke17ZwdGBToddI8pDm48kGfiFqkITS6axXxhYYUCnlRZw-zPPgdn4jUwVcJE1ZvWQUxwkmyExglNqGp0IvTJZUJFbgE-7XRK3dMEBRBhUpx1B3uKuIxKkeNobmVrkfsvhi7vfNIYPwuNoe0YQqN5qRcQyCP0lZkCSDZ8KLElTzs/Film_Squares_002.jpg')

        addDir3('[B][COLOR]Serviceil[/COLOR][/B] [COLOR FFffa80612][B]Formula 1[/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=documentary%20Formula1/?page=1",35,'https://images.squarespace-cdn.com/content/v1/54ac152ee4b0a068ceceeb7a/1421701286623-IWCUL6YSXVNJ37TROLRZ/ke17ZwdGBToddI8pDm48kGfiFqkITS6axXxhYYUCnlRZw-zPPgdn4jUwVcJE1ZvWQUxwkmyExglNqGp0IvTJZUJFbgE-7XRK3dMEBRBhUpx1B3uKuIxKkeNobmVrkfsvhi7vfNIYPwuNoe0YQqN5qRcQyCP0lZkCSDZ8KLElTzs/Film_Squares_002.jpg')

        addDir3('[B][COLOR]Serviceil[/COLOR][/B] [COLOR FFff5a5698][B]Indycar[/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=documentary%20indycar/?page=1",35,'https://images.squarespace-cdn.com/content/v1/54ac152ee4b0a068ceceeb7a/1421701286623-IWCUL6YSXVNJ37TROLRZ/ke17ZwdGBToddI8pDm48kGfiFqkITS6axXxhYYUCnlRZw-zPPgdn4jUwVcJE1ZvWQUxwkmyExglNqGp0IvTJZUJFbgE-7XRK3dMEBRBhUpx1B3uKuIxKkeNobmVrkfsvhi7vfNIYPwuNoe0YQqN5qRcQyCP0lZkCSDZ8KLElTzs/Film_Squares_002.jpg')

        addDir3('[B][COLOR]Serviceil[/COLOR][/B] [COLOR FFff41dd3b][B]Motorcycle Racing[/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=documentary%20motorcycle%20racing/?page=1",35,'https://images.squarespace-cdn.com/content/v1/54ac152ee4b0a068ceceeb7a/1421701286623-IWCUL6YSXVNJ37TROLRZ/ke17ZwdGBToddI8pDm48kGfiFqkITS6axXxhYYUCnlRZw-zPPgdn4jUwVcJE1ZvWQUxwkmyExglNqGp0IvTJZUJFbgE-7XRK3dMEBRBhUpx1B3uKuIxKkeNobmVrkfsvhi7vfNIYPwuNoe0YQqN5qRcQyCP0lZkCSDZ8KLElTzs/Film_Squares_002.jpg')







def Dgllllllly():
        addDir('[COLOR blue]Ultimate Music Collection[/COLOR]','url',987652000,'https://i.ytimg.com/vi/OPo6T7lreqw/hqdefault.jpg')
        addDir('[COLOR blue]Top In Music[/COLOR]','url',987652001,'https://i.ytimg.com/vi/9vjTCyO2K7k/hqdefault.jpg')
        addDir('[COLOR blue]Popular Full Concerts[/COLOR]','url',987652002,'https://d26oc3sg82pgk3.cloudfront.net/files/media/edit/image/5440/square_thumb%403x.jpg')
        addDir('[COLOR blue]Wendy Williams Show - Mini Concerts[/COLOR]','url',987652003,'https://i.ytimg.com/vi/JrZtc_lWYIs/default.jpg')

      













def kttgty():
        addDir('[COLOR blue]Ultimate Music Collection[/COLOR]','url',987652100,'https://i.ytimg.com/vi/OPo6T7lreqw/hqdefault.jpg')
        addDir('[COLOR blue]Top In Music[/COLOR]','url',987652101,'https://i.ytimg.com/vi/9vjTCyO2K7k/hqdefault.jpg')
        addDir('[COLOR blue]Popular Full Concerts[/COLOR]','url',987652102,'https://d26oc3sg82pgk3.cloudfront.net/files/media/edit/image/5440/square_thumb%403x.jpg')
        addDir('[COLOR blue]Wendy Williams Show - Mini Concerts[/COLOR]','url',987652103,'https://i.ytimg.com/vi/JrZtc_lWYIs/default.jpg')



def rockcollectionly():
        addDir3('[COLOR orchid][B]GREATEST SLOW ROCK SONGS[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLq0ajtdli5G8idRnNPS_ei1eBimVu8tcn/?page=1",35,art + 'tbum.jpg')
        addDir3('[COLOR blue][B]80S SOFT ROCK LOVE SONGS[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLq0ajtdli5G8idRnNPS_ei1eBimVu8tcn&index=1/?page=1",35,art + 'tbum.jpg')
        addDir3('[COLOR yellow][B]ROCK SONGS HITS ALL TIME[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLp56AzR7YZeulJwWZc4yur7ooDg_UtKhD/?page=1",35,art + 'tbum.jpg')
        addDir3('[COLOR lime][B]CLASSIC SONGS 80S 90S[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLLlgdvO0Nffb3KR4mVLu7j3shB2ViZLGP/?page=1",35,art + 'tbum.jpg')
        addDir3('[COLOR orange][B]MOST BEAUTIFUL LOVE SONGS[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLAN2ijY9WzlwYR6_WtieIZtqZ94Wke5o9/?page=1",35,art + 'tbum.jpg')
        addDir3('[COLOR dodgerblue][B]BEST SONGS EVER[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLjZf72-EsullE1D-3zZj1Q1AVQS-zBzj5/?page=1",35,art + 'tbum.jpg')
        addDir3('[COLOR red][B]GREATEST HITS OF THE 80[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLEffX5-5DhPtWTyU3r8nm-ha6DySzKzoW&index=2/?page=1",35,art + 'tbum.jpg')
        addDir3('[COLOR darkmagenta][B]GREATEST HITS OF THE 70s 80s[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL8ICnoVYi7pc7AftMD5aY98hSkv3K0BEB/?page=1",35,art + 'tbum.jpg')
        addDir3('[COLOR cyan][B]BEST MOTOWN SONGS OF ALL TIME[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLwXYgB2CtnVM4M_yqVtxYpnJB3I95HU-l/?page=1",35,art + 'tbum.jpg')
        addDir3('[COLOR darkgoldenrod][B]BEST OLDIES LOVE SONGS OF ALL TIME[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLwXYgB2CtnVOLnv_SCr4V6YMKYwj92fhk/?page=1",35,art + 'tbum.jpg')
        addDir3('[COLOR orangered][B]GREATEST SOUL SONGS[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL00ZqAjyF5PW5uT90RAcS4UrEijLucslj/?page=1",35,art + 'tbum.jpg')
        addDir3('[COLOR salmon][B]GREATEST 70S 80S ROCK SONGS[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLYUQMTiCwszIPKuHfAaA7pcaM0Y6ljT6g/?page=1",35,art + 'tbum.jpg')
        addDir3('[COLOR chartreuse][B]BEST ROMANTIC ENGLISH LOVE SONGS[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLFjbVJl7eR36JfQl-_KbWf32e9aUwrJhO/?page=1",35,art + 'tbum.jpg')
        addDir3('[COLOR darkturquoise][B]CLASSIC OF THE 1986[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLtmCPKUMm2qafI6JvTqhIXwOK-LdtwXDv/?page=1",35,art + 'tbum.jpg')
        addDir3('[COLOR fuchsia][B]BALLADS 70 80 90 MIX[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLcKqw5e0etEDWf-kpMeDUE-4ZliLUha9J/?page=1",35,art + 'tbum.jpg')
        addDir3('[COLOR goldenrod][B]SLOW ROCK MEDLEY SONGS[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLa-b2dUvu_lB15vHu4qROJBKzPzVTbml2/?page=1",35,art + 'tbum.jpg')
        addDir3('[COLOR lawngreen][B]CLASSIC COLLECTION[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLmE-U8SJLN0TXSlUFjbq0c03jdig1920P/?page=1",35,art + 'tbum.jpg')
        addDir3('[COLOR limegreen][B]ROMANTIC SONGS EVER[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLjZf72-EsullE1D-3zZj1Q1AVQS-zBzj5/?page=1",35,art + 'tbum.jpg')
        addDir3('[COLOR maroon][B]DISCO 70S 80S 90S[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLGKE0rBZEgcN1z4AdApz9TSK7jkvO3SOh/?page=1",35,art + 'tbum.jpg')
        addDir3('[COLOR limegreen][B]THE BEST ARTIST ALL TIMES[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLmE-U8SJLN0TXSlUFjbq0c03jdig1920P/?page=1",35,art + 'tbum.jpg')
        addDir3('[COLOR limegreen][B]CLASSIC SONGS ALL TIMES[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL3485902CC4FB6C67/?page=1",35,art + 'tbum.jpg')		
        addDir3('[COLOR limegreen][B]PHILL COLLINS[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL78645F08099E55F9/?page=1",35,art + 'tbum.jpg')
        addDir3('[COLOR limegreen][B]BRIAN ADAMS[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL54D3F57300A406FA/?page=1",35,art + 'tbum.jpg')
        addDir3('[COLOR limegreen][B]BON JOVI[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL574FBF341B72DAD5/?page=1",35,art + 'tbum.jpg')
        addDir3('[COLOR limegreen][B]GUNS AND ROSES[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLE6EB681577F21B3C/?page=1",35,art + 'tbum.jpg')
        addDir3('[COLOR limegreen][B]LED ZEPPELIN[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLjH4YJfu1WfE2bciiQZ7Ci0TiIDzYE3HJ/?page=1",35,art + 'tbum.jpg')
        addDir3('[COLOR limegreen][B]QUIET RIOT[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLPTh1c6pC1BxPCNypTxkzSpbWcOgpstC6/?page=1",35,art + 'tbum.jpg')
        addDir3('[COLOR limegreen][B]SCORPIONS[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL8AB0F5120809FF19/?page=1",35,art + 'tbum.jpg')
        addDir3('[COLOR limegreen][B]QUEENS[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLqDzNilwDj_dm_BOGxoCRmvA6CheRwAiw/?page=1",35,art + 'tbum.jpg')
        addDir3('[COLOR limegreen][B]TWISTED SISTER[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL29662FBF0FC8F98D/?page=1",35,art + 'tbum.jpg')
        addDir3('[COLOR limegreen][B]DEEP PURPLE[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL8384361C552AE037/?page=1",35,art + 'tbum.jpg')
        addDir3('[COLOR limegreen][B]AC DC[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLQlc99hV-nkGWDaG-gJxwOfqp8jxyHaaQ/?page=1",35,art + 'tbum.jpg')
        addDir3('[COLOR limegreen][B]KISS[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL71A9E09DEF0CE017/?page=1",35,art + 'tbum.jpg')
        addDir3('[COLOR limegreen][B]EUROPE[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLDD6E90D62FC64610/?page=1",35,art + 'tbum.jpg')
        addDir3('[COLOR limegreen][B]BARON ROJO[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL79E4245F0137AA18/?page=1",35,art + 'tbum.jpg')
        addDir3('[COLOR limegreen][B]BONNIE TYLER[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLvz78UNxtDruCicAvERgXFk2XVgiBn_4y/?page=1",35,art + 'tbum.jpg')
        addDir3('[COLOR limegreen][B]TOTO[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLyNIUJIA6jp58gmBKIUQ5zh4UWRxQtXKe/?page=1",35,art + 'tbum.jpg')
        addDir3('[COLOR limegreen][B]FOREIGNER[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL72D7EDFFBD267A94/?page=1",35,art + 'tbum.jpg')
        addDir3('[COLOR limegreen][B]KANSAS[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLCCAB3C8590D69DC1/?page=1",35,art + 'tbum.jpg')
        addDir3('[COLOR limegreen][B]BEE GEES[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLE572452B578F4B90/?page=1",35,art + 'tbum.jpg')
        addDir3('[COLOR limegreen][B]ROLLING STONE[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLP02sRgldWRb9LjuQgJ4AfxCd4cxygDrA/?page=1",35,art + 'tbum.jpg')
        addDir3('[COLOR limegreen][B]BEATLES[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLmo4pBukfRoN8SB5RKvfiY9CTl9pI_IFc/?page=1",35,art + 'tbum.jpg')
        addDir3('[COLOR limegreen][B]THE DOORS[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL7DlGI0vwP4S6tlQ-kMqrl6VCaN053_BN/?page=1",35,art + 'tbum.jpg')
        addDir3('[COLOR limegreen][B]JIMI HENDRIX[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLMKA5kzkfqk2GEImRCIqGqWmQvKYygUhG/?page=1",35,art + 'tbum.jpg')
        addDir3('[COLOR limegreen][B]VAN HALEN[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLoIh3u70c_PKEjlagdBAK3cEe_wXKSee2/?page=1",35,art + 'tbum.jpg')		
        addDir3('[COLOR limegreen][B]THE EAGLE[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLwNBAifp_VilC7ch4uI0SQgxkRch4qzPh/?page=1",35,art + 'tbum.jpg')
        addDir3('[COLOR limegreen][B]THE POLICE[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL36494E8634856791/?page=1",35,art + 'tbum.jpg')
        addDir3('[COLOR limegreen][B]U2[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL57CDBF4FB33C5BC1/?page=1",35,art + 'tbum.jpg')
        addDir3('[COLOR limegreen][B]NIRVANA[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLF1D793B61571DD4A/?page=1",35,art + 'tbum.jpg')
        addDir3('[COLOR limegreen][B]METALLICA[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL926CCB27995D3E94/?page=1",35,art + 'tbum.jpg')
        addDir3('[COLOR limegreen][B]THE WHO[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLB2359E68D19BA3C0/?page=1",35,art + 'tbum.jpg')
        addDir3('[COLOR limegreen][B]PINK FLOYD[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL8CQIFqDrjYUVdJbkHe4--PkWZYBB3NoW/?page=1",35,art + 'tbum.jpg')
        addDir3('[COLOR limegreen][B]AEROSMITH[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9E80D3CB56F329AF/?page=1",35,art + 'tbum.jpg')
        addDir3('[COLOR limegreen][B]ALICE COOPER[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLzMhF_Kgqw3iZBdZ4sX-kdVaWPCEo3q9B/?page=1",35,art + 'tbum.jpg')
        addDir3('[COLOR limegreen][B]MEAT LOAF[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLslHapSMmen25gJiJ1h4ljKgGctdoRMbM/?page=1",35,art + 'tbum.jpg')
        addDir3('[COLOR limegreen][B]OZZY OSBOURNE[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLjsINEkV8yYEvi_6VtsI8BSqFXM1QtQwM/?page=1",35,art + 'tbum.jpg')





def topinmusicly():
        addDir3('[COLOR aqua]R&B[/COLOR]',"plugin://plugin.video.youtube/playlist/PLAKw47hquUsIWArq-QR2v_wR-JZIjASWv/?page=1",35,'https://i.ytimg.com/vi/0habxsuXW4g/hqdefault.jpg')
        addDir3('[COLOR aqua]Hip Hop[/COLOR]',"plugin://plugin.video.youtube/playlist/PLAKw47hquUsLe6xcBQjOLBf69HFyPwhCZ/?page=1",35,'https://i.ytimg.com/vi/9vjTCyO2K7k/hqdefault.jpg')
        addDir3('[COLOR aqua]Sex Tunes (Freaky R&B, Rap) [/COLOR]',"plugin://plugin.video.youtube/playlist/PLA3D4CE0630E72D50/?page=1",35,'https://i.ytimg.com/vi/E98IYokujSY/hqdefault.jpg')
        addDir3('[COLOR aqua]Mix - MARIAH CAREY - Its Like That - #1 to Infinity 7/18/17[/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=MARIAH%20CAREY%20-%20It%27s%20Like%20That%20-%20%231%20to%20Infinity%207%2f18%2f17%20LIVE/?page=1",35,'https://i.ytimg.com/vi/Fw_mWEv-Zdc/hqdefault.jpg')
        addDir3('[COLOR aqua]DEVO - Mix[/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=DEVO - Mix/?page=1",35,'https://i.ytimg.com/vi/aAcOuOaFwyY/hqdefault.jpg')
        addDir3('[COLOR aqua]Lindsey Stirling - Mix[/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=Lindsey Stirling - Mix/?page=1",35,'https://i.ytimg.com/vi/1A3i0GATnRI/hqdefault.jpg')
        addDir3('[COLOR aqua]2CELLOS - 2 Beautiful CELLOS[/COLOR]',"plugin://plugin.video.youtube/playlist/PLoGeCeQU-L930yQ7zQg4Mlq3TEnT-cm_g/?page=1",35,'https://i.ytimg.com/vi/UdHopftQD3A/hqdefault.jpg')

def topinmusic2ly():
        addDir3('[COLOR aqua]Popular Full Concerts[/COLOR]',"plugin://plugin.video.youtube/playlist/PLoGeCeQU-L907nwZ3LVFrj31-0cxK3frP/?page=1",35,'https://i.ytimg.com/vi/UdHopftQD3A/hqdefault.jpg')

def topinmusic3ly():
        addDir3('[COLOR aqua]Wendy Williams Show - Mini Concerts[/COLOR]',"plugin://plugin.video.youtube/playlist/PL7B8F77DCC58E8531/?page=1",35,'https://i.ytimg.com/vi/UdHopftQD3A/hqdefault.jpg')

def Daay():
        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffd0e5ae][B][COLOR aqua]**DBs Saved Movie List**[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLoGeCeQU-L93iEHLQnyBLcq8V0t_Jn0Fc/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff91a420][B][COLOR aqua]**Sci-Fi Movies and TV Shows**[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLc5RR1k57YQ2CKiFmK21y-TeyZg354OeZ/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff15d5b6][B][COLOR aqua]**Western Tv Series**[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/UUI3jCHxTrdgLs2BNIfSlfSQ/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff77077c][B][COLOR aqua]**Film Noir Full Movies - Rare and Classics**[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLajqNV0-qkKdGiFNzmK5BA16MujBJ0bvv/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff58ebc5][B][COLOR aqua]**1930-1960S COMEDY MOVIES**[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL4T8ftYa82pZGq-2UZ0QPlgq6Ek74D0sK/?page=1",35,art + 'movies.png')
        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff1e0ec3][B][COLOR aqua]**Sci-Fi Movies 1950 s**[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLRk8KBuNEEmUWIBjIXp_7t4M1iMhuZuJB/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff5f4a79][B][COLOR aqua]**Classic Horror Movies III**[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLprCz0PxKdOdl8OBeNAFyweZHztTb_XAf/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffe1c5ff][B][COLOR aqua]**Pizza Creatures**[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLmHgXUJMN1TUtIOqNXDYVesjjWKOziQq5/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff9cf719][B][COLOR aqua]**Ghosts, Haunted Houses, Who Dun It**[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLX9_I-EOJPdHqVwm5nCOChM_MdJc-_MqM/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff08b33b][B][COLOR aqua]**Rare and Classic Grindhouse Movies**[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLajqNV0-qkKdfaARIBraH6VtFPVMXqaZd/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffe908f9][B][COLOR aqua]**True Crime TV Movies**[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL8yCb7LeIHjL1R7sKIBgLYtxVFGnf__JF/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff03cfab][B][COLOR aqua]**Over 600 Full Horror Movies**[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLkzvgsq3ySHBduUI5DSAwpJylNKkGYjqg/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffaaa511][B][COLOR aqua]**Pre-Code Films 1 - (1929-1934)**[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLwALQdqjNQHPgGZ5xShmhd1GfTsvjdP5c/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff85dfc6][B][COLOR aqua]**Pre-Code Films 2 - (1929-1934)**[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL8Nn95jd6kYWA991-obM9SuFfYBavgHlg/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff0efcd9][B][COLOR aqua]**Over 500 Classic & Cult Films & Series**[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL9ZTfmHep3gO88QRhLuMEZCEPd6QX0nr6/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff014be9][B][COLOR aqua]**Shirley Temple**[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLoGeCeQU-L91U4juM8C5QygkZKda8h12e/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff7fa712][B][COLOR aqua]Pre-Code Hollywood[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=pre-code%20hollywood/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffa5f8c9][B][COLOR aqua]Sci-Fi/Horror[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=full%20hollywood%20scifi%20horror%20movie/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFfff34756][B][COLOR aqua]Mystery Science Theater 3000[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=MST3K/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffaff181][B][COLOR aqua]Kings Of Horror Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=kingsofhorror/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff1cb718][B][COLOR aqua]FilmRise Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=filmrise%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff0c1791][B][COLOR aqua]FilmRise Horror[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=filmrise%20horror/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffc7436e][B][COLOR aqua]FilmRise All[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=filmrise/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff55053d][B][COLOR aqua]More Westrens[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=full%20hollywood%20action%20western%20movie/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffa1c9f2][B][COLOR aqua]Snagfilms Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=snagfilms/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff61335b][B][COLOR aqua]Maverick Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=maverickent%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffee79a4][B][COLOR aqua]LifeTime Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=lifetime%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff8893c9][B][COLOR aqua]HallMark Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=hallmark%20movies/?page=1",35,art + 'movies.png')


        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff5f76c1][B][COLOR aqua]**PizzaFlix**[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/UUE34fwgW7kWr7tc7YiOWtRw/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff37db87][B][COLOR aqua]**Movie Holic**[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/UURHcpjAIeJpAVhnSaa_I2hQ/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff0291fd][B][COLOR aqua]**Viewster**[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/UUSUMyPPmunaDKk0YHxCK-cw/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffa29195][B][COLOR aqua]**All things Laurel and Hardy**[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/UUQ1Ix_zcD2Fa8n-bEyEEVXA/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffe1c724][B][COLOR aqua]**British Movies**[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/channel/UCBB5iiT4wElEH4vse4siklw/playlist/PLRXjtfMCvJBUIbFnKgseWtmrYT9v94jSC/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffa5732a][B][COLOR aqua]**British Mysteries**[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/channel/UCBB5iiT4wElEH4vse4siklw/playlist/PLHlHyIsMbQWxNg8AqV91h74rZyrtwvKET/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff81f573][B][COLOR aqua]**British Comedy Movies**[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL152bjytsMC4nnIPwEe_bzE-lMdTbMDrh/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffb14eb7][B][COLOR aqua]**Classic BBC Mysteries**[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/channel/UCBB5iiT4wElEH4vse4siklw/playlist/PL-QrWtkF-hBXqQslPleMFyAzjP7W7rF3u/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffbf4e9a][B][COLOR aqua]**Classic British Comedy**[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/channel/UCBB5iiT4wElEH4vse4siklw/playlist/PLTLojg5eHFQ59oHFEGLi1boK1oN-BGw7a/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff7ede54][B][COLOR aqua]**British Tv Dramas**[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=british%20tv%20drama%20full%20episode&quot%3b%2creturn)/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff9a1902][B][COLOR aqua]**Britains Darkest Taboos**[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/channel/UCBB5iiT4wElEH4vse4siklw/playlist/PL9ASawzn6_CKyM0xHcysyg507OEMbSUA8/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff99f2d9][B][COLOR aqua]**British Detective Series**[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/channel/UCBB5iiT4wElEH4vse4siklw/playlist/PLRXjtfMCvJBVcxF6HFk2Xkctaz0Gy-ZT8/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffd8cc88][B][COLOR aqua]**British History Documentaries**[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/channel/UCBB5iiT4wElEH4vse4siklw/playlist/PLA0AOrR2wsGCcfnxKHjw9YaBySwp-_ocI/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff9bbbcc][B][COLOR aqua]**U.K. Music Documentaries**[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/channel/UCBB5iiT4wElEH4vse4siklw/playlist/PLEEvR9jL5sqYEPrf7TrMsuJF2TVNLeBVA/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffafb5dd][B][COLOR aqua]**Blaxploitation movies 1970-80s**[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLqZdaedwfP_hUEuvsN0fssh1zJpirpXpz/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffa300ae][B][COLOR aqua]**Blaxploitation movies**[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL-KqxyRbNyKAy87-QnE06CMnW8i5gU_Ms/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff0c41ad][B][COLOR aqua]Black Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=black%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff8a2a80][B][COLOR aqua]Classic Black Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=classic%20black%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffedc888][B][COLOR aqua]Short Black Films[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=short%20black%20films/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffc96c0a][B][COLOR aqua]Urban Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=urban%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff820f93][B][COLOR aqua]Hood Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=hood%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff513038][B][COLOR aqua]Gangster Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=gangster%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff99f145][B][COLOR aqua]Mobster Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=mobster%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFfff4f6a5][B][COLOR aqua]-Real Street Fights[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=worldstarhiphop%20street%20fights/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff22e5f9][B][COLOR aqua]-Wu Tang Collection - 2,611 Videos[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/channel/UCUpbgPbDccjoB9PxI-nI7oA/playlist/PLcG66PDG1cyuZBuU7eeUh4b2nGkudDFRn/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff421dcf][B][COLOR aqua]-Superheroines - Girl Power![/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/channel/UCUpbgPbDccjoB9PxI-nI7oA/playlist/PLcG66PDG1cytzsrbJGJwxurHYa6MaOnuy/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff88f0dd][B][COLOR aqua]-1,475 - Kung Fu Films (Youtube)[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLSvPwyvZG6xZXHU1NtfyLUKiqgtzf8i84/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff151556][B][COLOR aqua]Martial Arts Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=martial%20arts%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff1d0598][B][COLOR aqua]Kung Fu Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=kung%20fu%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFfff21de7][B][COLOR aqua]-[/COLOR][COLOR aqua]Bruce Lee[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=bruce%20lee/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff2b2173][B][COLOR aqua]-[/COLOR][COLOR aqua]Chuck Norris[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=Chuck%20Norris/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff35797d][B][COLOR aqua]-[/COLOR][COLOR aqua]Chuck Norris VS. ????[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=Chuck%20Norris%20vs/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff339d1f][B][COLOR aqua]-[/COLOR][COLOR aqua]Steven Seagal[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=Steven%20Seagal/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFfff0c344][B][COLOR aqua]-[/COLOR][COLOR aqua]Jackie Chan[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=Jackie%20Chan/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffce1c08][B][COLOR aqua]-[/COLOR][COLOR aqua]Jean-Claude Van Damme[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=Jean-Claude%20Van%20Damme/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff9b397e][B][COLOR aqua]-[/COLOR][COLOR aqua]Dolph Lundgren[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=Dolph%20Lundgren/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff9eb856][B][COLOR aqua]-[/COLOR][COLOR aqua]Cynthia Rothrock[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=Cynthia%20Rothrock/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff4c21ec][B][COLOR aqua]Action Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=action%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffff7fcf][B][COLOR aqua]Adventure Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=adventure%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff5d8be9][B][COLOR aqua]Animation Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=animation%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffc741be][B][COLOR orange]-[/COLOR] [COLOR aqua]Cartoons Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=cartoons%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffc2d444][B][COLOR aqua]Anime Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=anime%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff71bde5][B][COLOR aqua]Biker Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=biker%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff911721][B][COLOR aqua]Classic Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=classic%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff3b36f4][B][COLOR aqua]Comedy Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=comedy%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff816232][B][COLOR aqua]Crime Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=crime%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff390168][B][COLOR aqua]Dance Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=dance%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff39f1c5][B][COLOR aqua]Disaster Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=disaster%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffb09ee4][B][COLOR aqua]Drama Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=drama%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffe17e01][B][COLOR aqua]Family Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=family%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffd52669][B][COLOR aqua]Fantasy Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=fantasy%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffc201cf][B][COLOR aqua]Horror Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=horror%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff6181cc][B][COLOR orange]-[/COLOR] [COLOR aqua]Zombie Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=zombie%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff7811f1][B][COLOR aqua]Musical Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=musical%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff60e6b7][B][COLOR aqua]Mystery Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=mystery%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff75a844][B][COLOR aqua]Road Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=road%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFfff05698][B][COLOR aqua]Romance Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=romance%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff57e4ae][B][COLOR aqua]Science Fiction Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=science%20fiction%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff646e64][B][COLOR orange]-[/COLOR] [COLOR aqua]Star Trek[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=startrek%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFfff0381f][B][COLOR orange]-[/COLOR] [COLOR aqua]Star Wars[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=starwars%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffc29c58][B][COLOR aqua]Serial Killers[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=serialkiller%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffc3ecf9][B][COLOR aqua]Sports Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=sports%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffe13ffe][B][COLOR aqua]Super Heroes DC Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=dc%20full%20lenght%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff1cc262][B][COLOR aqua]Super Heroes Marvel And DC Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=marvel%20dc%20comic%20full%20lenght%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff3c34ef][B][COLOR aqua]Thriller Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=thriller%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff4347f3][B][COLOR aqua]TV Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=tv%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff894389][B][COLOR aqua]Western Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=western%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff08a2ab][B][COLOR aqua]Spaghetti Western Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=western%20spaghetti%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFfff8adc0][B][COLOR orange]-[/COLOR] [COLOR aqua]Western TV[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=western%20tv/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffdcfd92][B][COLOR aqua]War Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=war%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFfff69c89][B][COLOR aqua]1990s Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=1990%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff6aacac][B][COLOR aqua]1980s Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=1980%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffebadb0][B][COLOR aqua]1970s Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=1970%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffa999d0][B][COLOR aqua]1960s Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=1960%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff80cff9][B][COLOR aqua]1950s Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=1950%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff78bf6f][B][COLOR aqua]1940s Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=1940%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff7cb4cc][B][COLOR aqua]1930s Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=1930%20movies/?page=1",35,art + 'movies.png')












def THEATERy():
        addDir('[COLOR aqua]סרטים [/COLOR]','url',987655930,art + 'movies.png')

        addDir('[COLOR aqua]סרטי קונג פו  [/COLOR]','url',987655937,art + 'Kung Fu.png')

        addDir('[COLOR aqua]סדרות  [/COLOR]','url',987655931,art + 'tv-shows.png')

        addDir('[COLOR aqua]סרטים-קטגוריות  [/COLOR]','url',987655933,art + 'movies.png')

        addDir('[COLOR aqua]סרטים וסדרוות לילדים  [/COLOR]','url',987655935,art + 'animals.jpg')


def THEATERBy():


        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFfffe0cee][B][COLOR aqua]80s & 90s Classic TV show intros[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLRRYo_lypDLQRApKo-g2-GYuQXGwB8wzL/?page=1",35,art + 'tv-shows.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff3e38a4][B][COLOR aqua]The Addams Family[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLwwhtOnMyjuxQy81h7uJMCdsR-bS-uVaD/?page=1",35,art + 'tv-shows.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff623492][B][COLOR aqua]Adult Wednesday Adams[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL0XAjui-xK6XE4PRT64WAthU6j1NmrOqU/?page=1",35,art + 'tv-shows.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff586362][B][COLOR aqua]Classic Mr Bean[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/UUEwIUtFBhaI2L2PuKv0KL2g/?page=1",35,art + 'tv-shows.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffe51acf][B][COLOR aqua]WesternTvSeries[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/UUI3jCHxTrdgLs2BNIfSlfSQ/?page=1",35,art + 'tv-shows.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffca4c94][B][COLOR aqua]All things Laurel and Hardy[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/UUQ1Ix_zcD2Fa8n-bEyEEVXA/?page=1",35,art + 'tv-shows.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFfffacec7][B][COLOR aqua]Sanford and Son[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLghomqhgT3Ql2r34G1Kw7nUuEMmEUH-7q/?page=1",35,art + 'tv-shows.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffdebcf8][B][COLOR aqua]The Others (Complete Series)[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL6fJmjt84zZhVlt_nTOeWQM8FCOEg4V4s/?page=1",35,art + 'tv-shows.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff7e725d][B][COLOR aqua]Ghost Story-Circle of Fear (TV)[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLeagipoZmyflMOu9SoIBHmjcgj2kQjEjF/?page=1",35,art + 'tv-shows.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFfff78dd1][B][COLOR aqua]Gimmea Break[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/UUDv7pmSdRYBwT69y-4c1Pnw/?page=1",35,art + 'tv-shows.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffd4883c][B][COLOR aqua]The Fall Guy[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/UUiWAQA4Mza-QFdLJhaEycJA/?page=1",35,art + 'tv-shows.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff586b90][B][COLOR aqua]Starman[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/UUCbNAYyyggXCgDcqRZndLzA/?page=1",35,art + 'tv-shows.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffad587e][B][COLOR aqua]The Lucy Show LUCILLE BALL 30 Full Episodes[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLmHgXUJMN1TXCZbl3w_RYofN_XMCRDtdy/?page=1",35,art + 'tv-shows.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff71b612][B][COLOR aqua]Shado UFO TV Series[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLLdwL8EUvbQFy2xuckcawapK8023drPQI/?page=1",35,art + 'tv-shows.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff502b6c][B][COLOR aqua]Gigantor Season 1[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL6UfctxfSOoFMQCkXuUMjNzwRWPoKeiPc/?page=1",35,art + 'tv-shows.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffd9a9b4][B][COLOR aqua]The Swiss Family Robinson Season 1[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL6UfctxfSOoEdk0S4qZvwlqfQk9s1g-4h/?page=1",35,art + 'tv-shows.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff0a77f9][B][COLOR aqua]Blakes 7[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/channel/UCLIv-DVrjhZJqb7hvTVgL_w/?page=1",35,art + 'tv-shows.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff4c0627][B][COLOR aqua]Nowhere Man (Complete)[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLeagipoZmyfmeKpbCdBkjSXczL3gioTIL/?page=1",35,art + 'tv-shows.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffe34175][B][COLOR aqua]Timecop (Complete)[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL6fJmjt84zZhp5eGS7ceZhYmyvyT8VtP0/?page=1",35,art + 'tv-shows.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffc558cf][B][COLOR aqua]THE COMEDY SHOP - Season 1[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL6UfctxfSOoFGFAUDe1EnGW44yM_ewrt4/?page=1",35,art + 'tv-shows.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff61e6f4][B][COLOR aqua]THE COMEDY SHOP - Season 2[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL6UfctxfSOoFZ3ORIfJV8xFzORsW3mclA/?page=1",35,art + 'tv-shows.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffd334da][B][COLOR aqua]Land of the Lost (Complete)[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL6fJmjt84zZhV4hZGR_VgBZxl2fAPA9Ed/?page=1",35,art + 'tv-shows.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff837877][B][COLOR aqua]The Invisible Man 1975 (Complete)[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLeagipoZmyfm1K3A2qNxleEpXJ5gUKTvk/?page=1",35,art + 'tv-shows.png')
        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff82633e][B][COLOR aqua]The Invisible Man 1984 (complete)[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLWBUT4nrnPf5CVi3zYyGLhkoxIR7gPubu/?page=1",35,art + 'tv-shows.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffbd98f1][B][COLOR aqua]It Takes a Thief Season 1[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLlTsHN-xkgl3RFB_CrnpAUlUUJm_Cy9MB/?page=1",35,art + 'tv-shows.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff997f9d][B][COLOR aqua]It Takes a Thief Season 2[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLlTsHN-xkgl243QxcnGEWTtFuaVCtp8Rp/?page=1",35,art + 'tv-shows.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffb62d12][B][COLOR aqua]It Takes a Thief Season 3[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLlTsHN-xkgl2pPgWXYMImAj4rS18id7nG/?page=1",35,art + 'tv-shows.png')

        addDir3('"[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffa22408][B][COLOR aqua]Flash Gordon (TV)[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLdwYgKHNxoDuH9wlEuEFvUQUEdkZ-tkn-/?page=1",35,art + 'tv-shows.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff1ff626][B][COLOR aqua]The Twilight Zone 2002 (TV)[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLbxdxEWxTqX81L3NnAU3nEwvPhkT7FuRm/?page=1",35,art + 'tv-shows.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffd15253][B][COLOR aqua]The Tribe (260 episodes Complete)[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL6fJmjt84zZiTh5wcoWV7RkUyzmU5swBL/?page=1",35,art + 'tv-shows.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff426175][B][COLOR aqua]Highlander (TV)[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL6fJmjt84zZgL4pcnB8DiV6cIZ9Cs8BVW/?page=1",35,art + 'tv-shows.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffe3c093][B][COLOR aqua]Taken (Mini Series)[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLgPqH4b_oLyrCExWaUbnLl6CI8cae82ZQ/?page=1",35,art + 'tv-shows.png')



        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff026767][B][COLOR aqua]I Spy-Season 1[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL6UfctxfSOoFvQKYAikolHyKt9oi8MGuT/?page=1",35,art + 'tv-shows.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffccfe4e][B][COLOR aqua]I Spy-Season 2[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL6UfctxfSOoEN39ge-JguunSJecncCK3P/?page=1",35,art + 'tv-shows.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff3706c3][B][COLOR aqua]I Spy-Season 3[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL6UfctxfSOoEZiHt-asBSUl34TMYLO4HC/?page=1",35,art + 'tv-shows.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff598ae6][B][COLOR aqua]My Favorite Martian - Season 1[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL6UfctxfSOoG0gEYp_ecXWBB5SFm0ZjE-/?page=1",35,art + 'tv-shows.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff727e58][B][COLOR aqua]My Favorite Martian - Season 2[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL6UfctxfSOoH5w_4W4Y50GhlZftrn9-2Q/?page=1",35,art + 'tv-shows.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffcff498][B][COLOR aqua]My Favorite Martian - Season 3[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL6UfctxfSOoGQXeR-IdwMW4iWXC__RuHW/?page=1",35,art + 'tv-shows.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffe6f3ee][B][COLOR aqua]The Rifleman Season 1[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL6UfctxfSOoE9alavdl37U-IHNJ4AyGE3/?page=1",35,art + 'tv-shows.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff4c45f6][B][COLOR aqua]The Rifleman Season 2[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL6UfctxfSOoEH0GGLqVVjeKaqkTLpY3QQ/?page=1",35,art + 'tv-shows.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff1375eb][B][COLOR aqua]The Rifleman Season 3[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL6UfctxfSOoFeZ7bJvniB-D8z-x88cQWe/?page=1",35,art + 'tv-shows.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff11b491][B][COLOR aqua]The Rifleman Season 4[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL6UfctxfSOoFuuWF3AUkfrpu-jmdvK1zD/?page=1",35,art + 'tv-shows.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff31b68c][B][COLOR aqua]The Rifleman Season 5[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL6UfctxfSOoGpAPi9a-0xyUZF_Pr88KVq/?page=1",35,art + 'tv-shows.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff79eac8][B][COLOR aqua]Captain Power & The Soldiers Of The Future[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL632DEFF5485C77A6/?page=1",35,art + 'tv-shows.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff0ff9a2][B][COLOR aqua]Thunderbirds[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLK7mXBqD4M5goOUVhnt8yQTgMeUMsdOKh/?page=1",35,art + 'tv-shows.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffb91e71][B][COLOR aqua]Captain America (1944) - Full Classic Series[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLnuZTQf1M64ydgAOg1hbyjabfTTqABiZJ/?page=1",35,art + 'tv-shows.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff1373f0][B][COLOR aqua]Voyage to the Bottom of the Sea[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLDbpGbv-wloF1WbRswE67MVemXtZS06Yy/?page=1",35,art + 'tv-shows.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff554648][B][COLOR aqua]The Beverly Hillbillies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL1V2SSERycssvC_FFdtBA16Qhiityw_ii/?page=1",35,art + 'tv-shows.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffe0e2fe][B][COLOR aqua]Whirlybirds[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLehwzgbsMqvXjmh1QmMsH1AQtIihO-Whh/?page=1",35,art + 'tv-shows.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff55bbe6][B][COLOR aqua]Highway Patrol[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLehwzgbsMqvWub0Kw0sfqGgpBXMevYaiI/?page=1",35,art + 'tv-shows.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffda9039][B][COLOR aqua]Edmond OBrien: Johnny Midnight[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLehwzgbsMqvW36b3-Vc22LrD_kLMNjB-Z/?page=1",35,art + 'tv-shows.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff18b644][B][COLOR aqua]The Invisible Man[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLehwzgbsMqvWNy5Z7BvyifFLM2XeITgl0/?page=1",35,art + 'tv-shows.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff0c94fb][B][COLOR aqua]BRIAN DONLEVY: Dangerous Assignment COMPLETE TV series[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLmHgXUJMN1TUumnyP9bMaYcEz-ftSyOjQ/?page=1",35,art + 'tv-shows.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffe7849f][B][COLOR aqua]One Step Beyond: Complete Season (1)[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLR9KUynF_6Fr2duXEUNiab8K8FWaNkzF9/?page=1",35,art + 'tv-shows.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff26442c][B][COLOR aqua]One Step BeyondOne: Complete Season (2)[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLR9KUynF_6FrmR90dRNIGI-rfNaL-1ZrE/?page=1",35,art + 'tv-shows.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff446bc5][B][COLOR aqua]The Abbott and Costello Show[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLehwzgbsMqvVZRTGNi9wFPrKokoHpOxee/?page=1",35,art + 'tv-shows.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFfff18403][B][COLOR aqua]BETTY WHITE: Life with Elizabeth[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLmHgXUJMN1TVZPk6F53tc1SS2U6JPav34/?page=1",35,art + 'tv-shows.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffd5d63d][B][COLOR aqua]CHARLES BRONSON: MAN WITH A CAMERA[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLmHgXUJMN1TXd7QFw5NeggEB0bbHpqxMP/?page=1",35,art + 'tv-shows.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff29067c][B][COLOR aqua]RICHARD BOONE: Medic[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLmHgXUJMN1TVRnTnRJKZ9cUSZA6YRDuQa/?page=1",35,art + 'tv-shows.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff1882dd][B][COLOR aqua]Combat![/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLehwzgbsMqvUDQKneLZcPvrm3w3wOcps1/?page=1",35,art + 'tv-shows.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffc3f634][B][COLOR aqua]Rat Patrol[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLehwzgbsMqvXVDiH62UyEAyQYMQ7qfnR-/?page=1",35,art + 'tv-shows.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff32603f][B][COLOR aqua]Petticoat Junction[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLmHgXUJMN1TW2LG21_pjI3ey-io5UF79J/?page=1",35,art + 'tv-shows.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffdde9db][B][COLOR aqua]DUSTYS TRAIL[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLmHgXUJMN1TVJkqn6ze4ktkzdFf9elYOa/?page=1",35,art + 'tv-shows.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff998606][B][COLOR aqua]THE CISCO KID[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLmHgXUJMN1TXOK8GD6u1rVnVWpNP_4K6V/?page=1",35,art + 'tv-shows.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffa499af][B][COLOR aqua]The Adventures of Ozzie & Harriet[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLmHgXUJMN1TVBtNLHmnCSdEZJtIl526B_/?page=1",35,art + 'tv-shows.png')



def THEATERB2ay():


        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff082740][B][COLOR aqua]Action Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=action%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff583ec3][B][COLOR aqua]Adventure Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=adventure%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFfffe74af][B][COLOR aqua]Animation Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=animation%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFfff763bc][B][COLOR orange]-[/COLOR] [COLOR aqua]Cartoons Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=cartoons%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFfffc298f][B][COLOR aqua]Anime Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=anime%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff571259][B][COLOR aqua]Biker Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=biker%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff7e93c1][B][COLOR aqua]Classic Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=classic%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff00bed3][B][COLOR orange]-[/COLOR] [COLOR aqua]Pre-Code Hollywood[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=pre-code%20hollywood/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffac3f31][B][COLOR aqua]Comedy Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=comedy%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff65d6a6][B][COLOR aqua]Crime Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=crime%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff7de992][B][COLOR aqua]Dance Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=dance%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffc74933][B][COLOR aqua]Disaster Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=disaster%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff0118b6][B][COLOR aqua]Drama Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=drama%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff0c2208][B][COLOR aqua]Family Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=family%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff05e42c][B][COLOR aqua]Fantasy Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=fantasy%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff17cd67][B][COLOR aqua]Horror Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=horror%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff189902][B][COLOR orange]-[/COLOR] [COLOR aqua]Zombie Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=zombie%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFfffbb086][B][COLOR aqua]Musical Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=musical%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff927e3b][B][COLOR aqua]Mystery Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=mystery%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFfff181d8][B][COLOR aqua]Road Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=road%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff872d6e][B][COLOR aqua]Romance Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=romance%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffcfef0a][B][COLOR aqua]Science Fiction Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=science%20fiction%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFfff4c790][B][COLOR orange]-[/COLOR] [COLOR aqua]Star Trek[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=startrek%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff9f3daf][B][COLOR orange]-[/COLOR] [COLOR aqua]Star Wars[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=starwars%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff8ce8ce][B][COLOR aqua]Serial Killers[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=serialkiller%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFfffd9e31][B][COLOR aqua]Sports Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=sports%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff27e363][B][COLOR aqua]Super Heroes DC Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=dc%20full%20lenght%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff562f97][B][COLOR aqua]Super Heroes Marvel And DC Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=marvel%20dc%20comic%20full%20lenght%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffcab3fe][B][COLOR aqua]Thriller Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=thriller%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffc80f8d][B][COLOR aqua]TV Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=tv%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff3c23b6][B][COLOR aqua]Western Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=western%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff7c11f3][B][COLOR aqua]Spaghetti Western Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=western%20spaghetti%20movies/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff93be08][B][COLOR orange]-[/COLOR] [COLOR aqua]Western TV[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=western%20tv/?page=1",35,art + 'movies.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff2ca866][B][COLOR aqua]War Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=war%20movies/?page=1",35,art + 'movies.png')



def THEATERB3ay():

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff5eaec2][B][COLOR aqua]Animation Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=animation%20movies/?page=1",35,art + 'animals.jpg')
        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff0f6f49][B][COLOR aqua]Cartoons Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=cartoons%20movies/?page=1",35,art + 'animals.jpg')
        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff43a196][B][COLOR aqua]Anime Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=anime%20movies/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff03a462][B]ABC Kid.tv[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UCbCmjCuTUZos6Inko4u57UQ/playlists/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff16c772][B]Baby Joy Joy[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UCkIz27-hS4O-mCiChXZgNKw/playlists/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff9e3f3a][B]Blues Clues[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UCesJOpRA7VlQV87nRPPeKlA/playlists/?page=1",35,art + 'animals.jpg')
        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFfff68169][B]Bob the Builder[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UCZLYbETi-hygKzyCerJ5daw/playlists/?page=1",35,art + 'animals.jpg')
        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffd2e85e][B]Bob the Builder (Australia)[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UC4-ct2mbZsOwSDf000L8bNg/playlists/?page=1",35,art + 'animals.jpg')
        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffe9e42b][B]Bob the Builder (US)[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UCXv3404_UQsWG46lTgx2MRQ/playlists/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil - [/COLOR][/B] [COLOR FFffb78eb1][B]The Brain Scoop[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UCkyfHZ6bY2TjqbJhiH8Y2QQ/playlists/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil[/COLOR][/B] [COLOR FFffc0bde4][B]Caillou[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UC4yQCVlLhTmOqX5kUkAGr0g/playlists/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil[/COLOR][/B] [COLOR FFff171fa4][B]Caillou - Full HD Episodes[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLC9Qdm15h_EVixE4J9SbZgkWLBNqEldS9/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff3162ac][B]Crash Course Kids[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UCONtPx56PSebXJOxbFv-2jQ/playlists/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffbc5ff7][B]Farmees - Nursery Rhymes And Kids Songs[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UCu9MYfF0vosVcK38oNnnJxw/playlists/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil - [/COLOR][/B] [COLOR FFffb98bf5][B]Geek Gurl Diaries[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UCxrp2coE9wRrnlOO3V3UmdQ/playlists/?page=1",35,art + 'animals.jpg')
        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff7ed003][B]HooplaKidz - Official Nursery Rhymes Channel[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UC3djj8jS0370cu_ghKs_Ong/playlists/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff2f9981][B]HooplaKidz How To - DIY Crafts and Play Doh Videos[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UCxkkhCFRexEyFHUHEcH5Uzg/playlists/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff31fecb][B]HooplaKidz TV - Funny Cartoons For Children[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UCMfZ_z0LUm805JOZLktl2QQ/playlists/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffa182b8][B]HooplaKidz TV - Hoopla Lab[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UCZYqWTQJzJaMW7jFG16p8ug/playlists/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff834548][B]HooplaKidz TV - Hoopla Recipes[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UC-vObULK1w635bdFQpNlbQA/playlists/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffb3e2f7][B]HooplaKidz TV - Hoopla Kids Education[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UCaIS49HEvpCrHuVCVEAYKWA/playlists/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff13ee93][B]Junior Squad - nursery rhymes & kids songs[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UCkOny4N1-Qn9UTx7pYnEL3A/playlists/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff5ae49b][B]Kids Channel - Cartoon Videos for Kids[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UC3KknIJZXRygH2pZ6MDtGbg/playlists/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff3c637b][B]Kids Hut[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UChz5aEi3dfrDVC8-YJsMUDA/playlists/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffeab388][B]Kids Rhymes - Cartoon Videos for Children[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UCf4-1iHEgNgNWH_HKmYAtcw/playlists/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffeb4d34][B]Kids TV[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UC7Pq3Ko42YpkCB_Q4E981jw/playlists/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil - [/COLOR][/B] [COLOR FFff26f1b8][B]Little Baby Bum[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UCKAqou7V9FAWXpZd9xtOg3Q/playlists/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil - [/COLOR][/B] [COLOR FFff2c73fd][B]LBB Junior[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UC3_PaZ3Eso1JkuJyE_v4-3g/playlists/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff528b73][B]Little Eddie - Nursery Rhymes and Kids Songs[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UCXKuQPLe82SCtxtua4wWm8g/playlists/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil - [/COLOR][/B] [COLOR FFff24d5fd][B]Mother Goose Club[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UCJkWoS4RsldA1coEIot5yDA/playlists/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil - [/COLOR][/B] [COLOR FFff4602d1][B]Mother Goose Club - Playhouse[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UC6zPzUJo8hu-5TzUk8IEC2Q/playlists/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil - [/COLOR][/B] [COLOR FFffa6d4ed][B]PBS KIDS[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UCrNnk0wFBnCS1awGjq_ijGQ/playlists/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff50acf6][B]Peppa Pig[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UCAOtE1V7Ots4DjM8JLlrYgg/playlists/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff81cb47][B]Peppa Pig - Full Episodes[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UC1aLdPsHl5R81q4Ga0YBkBw/playlists/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff5feab6][B]Peppa Pig English Channel[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UCmIZUrJjE4bgRqhd8BVvxsg/playlists/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffc516c1][B]SciShow Kids[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UCRFIPG2u1DxKLNuE3y2SjHA/playlists/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFfff04f4c][B]SmartGirls[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UCi_BjZoqPnMmkCLv2FlyBxQ/playlists/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff658428][B]Videogyan Kids Shows - Cartoon Animation For Kids[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UCCc1DMB-AcOssKJ7KweLXBg/playlists/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff14c9a3][B]Mr Tumble[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLaOdVmh27CVV-8ZOTM94zKAz0crRCYede/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff58db05][B]T-Series Kids Hut[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UChz5aEi3dfrDVC8-YJsMUDA/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff4cdcd8][B]ABC kid TV - Nursery Rhymes[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UCbCmjCuTUZos6Inko4u57UQ/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff21093a][B]Super Simple Songs - Kids Songs[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UCLsooMJoIpl_7ux2jvdPB-Q/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff9ff346][B]Super Simple TV - Kids Shows & Cartoons[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UCdIWg_E1ckuONPTsdvevYgg/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff253d68][B]Blippi[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UC5PYHgAzJ1wLEidB58SK6Xw/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffcf5f5e][B]All Kids Songs[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UCqxyozOILLj8EtMbKELaZEw/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff43ac38][B]Geethanjali Kids - Rhymes and Stories[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UCGVrxaJHUQHbPSUVDZ8sUVQ/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff2aece7][B]FlickBox Studios - Nursery Rhymes and Kids Songs[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UCBMiY29jmxd9PGU74eT1xPg/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff8ebbc5][B]ChuChu TV Nursery Rhymes & Kids Songs[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/UCBnZ16ahKA2DZ_T5W0FPUXg/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffb9aed0][B]LooLoo Kids - Nursery Rhymes and Childrens Songs[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UC4NALVCmcmL5ntpV0thoH6w/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff1f4ba8][B]Teletubbies[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UCOk55dAgB8VnMlhaTEMeX5A/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff16cd95][B]Sesame Street[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UCoookXUzPciGrEZEXmh4Jjg/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff8b1242][B]StoryBots[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UCAJnyTWJPpKXuwgWQDdNWrQ/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff650a08][B]Pingu TV[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UCQAhOfRafGt-Zn23xSXQONQ/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff0db3b4][B]Fairy Tales and Stories for Kids[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UCOPzf8kf-FUDs32E7F2wGdg/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFfff07f87][B]Little Treehouse Nursery Rhymes and Kids Songs[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UCpzYfBXbEHHQHU2e89jM9Tg/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff469a07][B]ABC Heroes - Kids Nursery Rhymes TV And Baby Songs[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UCeA2JrCAqRohEHHwAFJNY4Q/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFfff6b7f8][B]Farmees - Nursery Rhymes And Kids Songs[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UCu9MYfF0vosVcK38oNnnJxw/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff9f0a55][B]Ben and Holly’s Little Kingdom[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UC2UhuvjTIrR0Ck2KrkvRcuA/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffa29407][B]Fireman Sam[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UCAJetkuJ2zz92WOJCrQvfkw/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff9fad1e][B]Postman pat[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UCqrVPwN_DhavUC386xH9SDw/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff76ef6d][B]The Childrens Channel[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UC5ymceNk75lJuXJdFpYpubg/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFfff18e66][B]Little Charley Bear[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UCydekQV_GkprQFYMdgc8e6A/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff359d75][B]Little Red Tractor[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UCLiE5PSUBr6OOsHOqvCJ0QQ/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffb70a32][B]Fifi and The Flowertots[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UC0j36_NCIX_eSc1nXfNGXVQ/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff323773][B]Veggie Tales[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UChddokv0fxIN3BS-KZpxFfA/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff1cb2e7][B]Raa Raa the Noisy Lion[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UC9y5Bed2UVb-kxBOt1nwQIQ/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffe80311][B]Olivia The Pig[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UCKe-7-MbrHXAUB3hYTa6pkw/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff5de79f][B]Finley The Fire Engine[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UCvPaNPcE3xkn2ysrwWlDKrg/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff3202b8][B]Woody Woodpecker[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UCB2aeGGPNj7l5Z71bYNqX-Q/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff58e012][B]George of the Jungle[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UCOiiCp4BVYqUvnLP8G38Iow/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffea3724][B]He Man[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UCWV0Qgo4Yz7E5_oNF4VJ6Rg/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFfff891e3][B]She Ra Princess of Power[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UCUh6BtszC2-ubKiv0hLf6gQ/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff489adc][B]WildBrain - Cartoon Super Heroes[/B][/COLOR]',"plugin://plugin.video.youtube/channel/UCUVnfQaEmCIhFZC5d_JniyQ/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffe915b0][B]Trumpton[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLh-Mj_oSkpi54CNCXpfrrBUqLsAsIoYx5/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff0a604e][B]Camberwick Green[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLh-Mj_oSkpi6ji7pGGdLH2iabfVs2lv4g/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff064fd5][B]The Flumps[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLh-Mj_oSkpi46fvEp93UJGJy7jKpgDXCS/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff848e36][B]Mr Benn[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLh-Mj_oSkpi78njyijHli8BvcuQfCArtB/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff60a0c7][B]Bagpuss[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLh-Mj_oSkpi75Oxs3r-LbWTKQ0a3RnWMZ/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffe1abc5][B]Ivor The Engine[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLh-Mj_oSkpi589iXBX3sO5g0LRC3GJDKu/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff8dbda6][B]Postman Pat Series 1[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLAQe205T2kVfRqwUiGOXlaMNcNFLRHc7x/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff06897c][B]Postman Pat Series 2[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLAQe205T2kVfIUjMOCml5yIRoQe_T_V03/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff06d5ae][B]Postman Pat: The Specials[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLAQe205T2kVfcayTqAPEDLExTw6x004-y/?page=1",35,art + 'animals.jpg')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffdf0096][B]Hectors House[/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PL4CF4BE8E833147A1/?page=1",35,art + 'animals.jpg')



def KungFu1y():


        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff4bae97][B][COLOR aqua]-Real Street Fights[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=worldstarhiphop%20street%20fights/?page=1",35,art + 'Kung Fu.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffb2e8cf][B][COLOR aqua]-Wu Tang Collection - 2,611 Videos[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/channel/UCUpbgPbDccjoB9PxI-nI7oA/playlist/PLcG66PDG1cyuZBuU7eeUh4b2nGkudDFRn/?page=1",35,art + 'Kung Fu.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff17681a][B][COLOR aqua]-Superheroines - Girl Power![/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/channel/UCUpbgPbDccjoB9PxI-nI7oA/playlist/PLcG66PDG1cytzsrbJGJwxurHYa6MaOnuy/?page=1",35,art + 'Kung Fu.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFfffd3d3d][B][COLOR aqua]-1,475 - Kung Fu Films (Youtube)[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/playlist/PLSvPwyvZG6xZXHU1NtfyLUKiqgtzf8i84/?page=1",35,art + 'Kung Fu.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff758c44][B][COLOR aqua]Martial Arts Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=martial%20arts%20movies/?page=1",35,art + 'Kung Fu.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff5ece75][B][COLOR aqua]Kung Fu Movies[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=kung%20fu%20movies/?page=1",35,art + 'Kung Fu.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff325645][B][COLOR aqua]-[/COLOR][COLOR aqua]Bruce Lee[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=bruce%20lee/?page=1",35,art + 'Kung Fu.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff9d886e][B][COLOR aqua]-[/COLOR][COLOR aqua]Chuck Norris[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=Chuck%20Norris/?page=1",35,art + 'Kung Fu.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffde0eb6][B][COLOR aqua]-[/COLOR][COLOR aqua]Chuck Norris VS. ????[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=Chuck%20Norris%20vs/?page=1",35,art + 'Kung Fu.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff6c21a5][B][COLOR aqua]-[/COLOR][COLOR aqua]Steven Seagal[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=Steven%20Seagal/?page=1",35,art + 'Kung Fu.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffe8717a][B][COLOR aqua]-[/COLOR][COLOR aqua]Jackie Chan[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=Jackie%20Chan/?page=1",35,art + 'Kung Fu.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff68882a][B][COLOR aqua]-[/COLOR][COLOR aqua]Jean-Claude Van Damme[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=Jean-Claude%20Van%20Damme/?page=1",35,art + 'Kung Fu.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFff7994f6][B][COLOR aqua]-[/COLOR][COLOR aqua]Dolph Lundgren[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=Dolph%20Lundgren/?page=1",35,art + 'Kung Fu.png')

        addDir3('[B][COLOR]Serviceil [/COLOR][/B] [COLOR FFffeab8e3][B][COLOR aqua]-[/COLOR][COLOR aqua]Cynthia Rothrock[/COLOR][/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?amp%3bsearch_type=video%22%2creturn)&q=Cynthia%20Rothrock/?page=1",35,art + 'Kung Fu.png')







def zozozoy():
        addDir('[COLOR aqua]זומבה [/COLOR]','url',987659010,art + 'zomba1.png')
        addDir('[COLOR aqua]פילאטיס [/COLOR]','url',987659011,art + 'pilates1.png')
        addDir('[COLOR aqua]אירובי [/COLOR]','url',987659012,art + 'aerobic1.png')
        addDir('[COLOR aqua]יוגה [/COLOR]','url',987659013,art + 'yoga1.png')
        addDir('[COLOR aqua]טיפוח נשים [/COLOR]','url',987659014,art + 'makeup1.png')
        addDir('[COLOR aqua]תזונה נכונה [/COLOR]','url',987659015,art + 'nutrition1.png')
        addDir('[COLOR aqua]רפואת נשים וילדים [/COLOR]','url',987659016,art + 'health1.png')
        addDir('[COLOR aqua]ספורט נשים [/COLOR]','url',987659017,art + 'sports1.png')
        addDir('[COLOR aqua]בידור ופנאי [/COLOR]','url',987659018,art + 'bidor1.png')
        addDir('[COLOR aqua]לייף סטייל [/COLOR]','url',9876510,art + 'lifestyle.png')


def zombay():
        addDir3('[COLOR aqua]זומבה דאנס[/COLOR]',"plugin://plugin.video.youtube/playlist/PLiRWC7Q54GioOmt7R89JpPsy9t0c9vLp8/?page=1",35,art + 'zomba.png')
        addDir3('[COLOR aqua]שיעורי זומבה[/COLOR]',"plugin://plugin.video.youtube/playlist/PLiRWC7Q54GioKGl8no2GUbVp3Qbbg2Utk/?page=1",35,art + 'zomba.png')




def pilatesy():
        addDir3('[COLOR aqua]שיעורי פילאטיס[/COLOR]',"plugin://plugin.video.youtube/playlist/PLiRWC7Q54Giob_DoXgZvAmjZyNjV3t7OR/?page=1",35,art + 'pilates.png')


def aerobicy():
        addDir3('[COLOR aqua]May Mor-כללי [/COLOR]',"plugin://plugin.video.youtube/channel/UCVuuZ4WcW-dSApMdfzW4iSw/?page=1",35,'https://maymor.tv/wp-content/uploads/2018/06/more_may-1.jpg')
        addDir3('[COLOR aqua]אימוני כושר[/COLOR]',"plugin://plugin.video.youtube/playlist/PLiRWC7Q54Gio1RYbFvueHFyFdrmxUsY8X/?page=1",35,art + 'aerobic.png')
        addDir3('[COLOR aqua]כושר בכייף עם המאמנת מאיה אמיתי[/COLOR]',"plugin://plugin.video.youtube/playlist/PLiRWC7Q54Gir8caN-f8jL5K9W1FXBBRgd/?page=1",35,art + 'aerobic.png')
        addDir3('[COLOR aqua]מאמן כושר אירובי[/COLOR]',"plugin://plugin.video.youtube/playlist/PLiRWC7Q54GipUXwBhfIJy6pzJRetK5Nv2/?page=1",35,art + 'aerobic.png')
        addDir3('[COLOR aqua]כושר ואירובי - תרגילים לחיטוב ועיצוב הגוף[/COLOR]',"plugin://plugin.video.youtube/playlist/PLiRWC7Q54GirImmtEfQkLgYgcl3_aHm55/?page=1",35,art + 'aerobic.png')
        addDir3('[COLOR aqua]אימוני כושר ביתיים - עם מאמנת הכושר לירון שני בירן[/COLOR]',"plugin://plugin.video.youtube/playlist/PLOZ5nscrPV88ehnfWI7UmuQ_fwtIu3a68/?page=1",35,art + 'aerobic.png')
        addDir3('[COLOR aqua]תרגילי כושר ואירובי[/COLOR]',"plugin://plugin.video.youtube/playlist/PLMHMyl3oeyh0ryXE6ypetk9c89oe5HL5u/?page=1",35,art + 'aerobic.png')
        addDir3('[COLOR aqua]תרגילי כושר ואירובי-2[/COLOR]',"plugin://plugin.video.youtube/playlist/PL1c41tQdiDhPTthizOvwpHsV4kaRVEatr/?page=1",35,art + 'aerobic.png')
        addDir3('[COLOR aqua]תרגילי כושר ואירובי-3[/COLOR]',"plugin://plugin.video.youtube/playlist/PL1c41tQdiDhPsKxBxXIWIUDxb6thKBK8R/?page=1",35,art + 'aerobic.png')
        addDir3('[COLOR aqua]תרגילי כושר כדור קפיצה[/COLOR]',"plugin://plugin.video.youtube/playlist/PLiRWC7Q54GipT9LzDiyiUcgliv-KrGRae/?page=1",35,art + 'aerobic.png')
        addDir3('[COLOR aqua]Gym Laura - תרגילי כושר[/COLOR]',"plugin://plugin.video.youtube/playlist/PLsPcs4lOzaD0luf_PeFBCB6uwILXybLBc/?page=1",35,art + 'aerobic.png')
        addDir3('[COLOR aqua]Gym Lower Body - תרגילי כושר[/COLOR]',"plugin://plugin.video.youtube/playlist/PLsPcs4lOzaD2pg6TWXr0ZcMGjw7Qgx40q/?page=1",35,art + 'aerobic.png')
        addDir3('[COLOR aqua] Gym TABATA - תרגילי כושר[/COLOR]',"plugin://plugin.video.youtube/playlist/PLsPcs4lOzaD0donVsJC_598bIRuTa-MZL/?page=1",35,art + 'aerobic.png')
        addDir3('[COLOR aqua] Gym Julia Bognar - תרגילי כושר[/COLOR]',"plugin://plugin.video.youtube/playlist/PLsPcs4lOzaD3Hze49tFRIC-EKQHDS22DS&index=42/?page=1",35,art + 'aerobic.png')
        addDir3('[COLOR aqua]Gym Christine Khuri -  תרגילי כושר[/COLOR]',"plugin://plugin.video.youtube/playlist/PLsPcs4lOzaD37I2dyaIPwmhbjjQ_km55P/?page=1",35,art + 'aerobic.png')
        addDir3('[COLOR aqua]Gym Cardio  -  תרגילי כושר[/COLOR]',"plugin://plugin.video.youtube/playlist/PLsPcs4lOzaD19MaOusgNDSBY79K0DDZuu/?page=1",35,art + 'aerobic.png')
        addDir3('[COLOR aqua]'+translate(930048)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLsPcs4lOzaD3LSSZtz6UnPkGOD7rnxkqI/?page=1",35,art + 'aerobic.png')
        addDir3('[COLOR aqua]Gym Stability Ball - תרגילי כושר[/COLOR]',"plugin://plugin.video.youtube/playlist/PLsPcs4lOzaD078QrnTh7tMQ_vBj26ZI3I/?page=1",35,art + 'aerobic.png')
        addDir3('[COLOR aqua]'+translate(930050)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PL9kERLsITKLoWpL-FOdMqTLQjhaeHKPHd/?page=1",35,art + 'aerobic.png')
        addDir3('[COLOR aqua]'+translate(930051)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PL9kERLsITKLr_ZNw01ONH2H8GkUqoQsc9/?page=1",35,art + 'aerobic.png')
        addDir3('[COLOR aqua]'+translate(930052)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PL254A5A4C3C292D34/?page=1",35,art + 'aerobic.png')
        addDir3('[COLOR aqua]'+translate(930053)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PL9kERLsITKLrBrU-0repW-vA5surKwTO6/?page=1",35,art + 'aerobic.png')

		
def yogay():
        addDir('[COLOR aqua]תדרים בינאורלים [/COLOR]','url',9876510012,art + 'yoga.png')
        addDir3('[COLOR aqua]'+translate(950001)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLui6Eyny-Uzx2jQYA8MS73ND2kUMHyII8/?page=1",35,art + 'yoga.png')
        addDir3('[COLOR aqua]'+translate(950002)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLui6Eyny-UzxL6NjFMYD5-vESNii8_aLi/?page=1",35,art + 'yoga.png')
        addDir3('[COLOR aqua]'+translate(950003)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLui6Eyny-UzzoiewtypZsiw2OIUz2btnD/?page=1",35,art + 'yoga.png')
        addDir3('[COLOR aqua]'+translate(950004)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLui6Eyny-UzzyYOtKfMfLl0h94mjsUKv9/?page=1",35,art + 'yoga.png')
        addDir3('[COLOR aqua]'+translate(950005)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLui6Eyny-Uzx5BRNB2_Kvycrn5h9OsaHC/?page=1",35,art + 'yoga.png')
        addDir3('[COLOR aqua]'+translate(950006)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLui6Eyny-UzzVLhyWdH7UAMd4dOQFCAhP/?page=1",35,art + 'yoga.png')
        addDir3('[COLOR aqua]'+translate(950007)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLui6Eyny-UzzWwB4h9y7jAzLbeuCUczAl/?page=1",35,art + 'yoga.png')
        addDir3('[COLOR aqua]'+translate(950008)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLui6Eyny-Uzw1DKEgFQZ5m38iZAXF1Xk5/?page=1",35,art + 'yoga.png')
        addDir3('[COLOR aqua]'+translate(950009)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLui6Eyny-Uzwzd-9fi_cmhz3UW9gS1raf/?page=1",35,art + 'yoga.png')
        addDir3('[COLOR aqua]'+translate(950010)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLui6Eyny-UzwheLDyEScgdgbh7z3FgNCX/?page=1",35,art + 'yoga.png')
        addDir3('[COLOR aqua]'+translate(950011)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLui6Eyny-UzwmsJ9vILet4TJwqcINCz4j/?page=1",35,art + 'yoga.png')
        addDir3('[COLOR aqua]'+translate(950012)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLui6Eyny-UzxMFVoPmxcPX1MOeLyV5uKQ/?page=1",35,art + 'yoga.png')
        addDir3('[COLOR aqua]'+translate(950013)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLui6Eyny-UzyugJTu3l1YFL0k3nGIlaz9/?page=1",35,art + 'yoga.png')
        addDir3('[COLOR aqua]'+translate(950014)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLui6Eyny-UzwCnJ3-L2ATvLNHE3zsunZi/?page=1",35,art + 'yoga.png')
        addDir3('[COLOR aqua]'+translate(950015)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLui6Eyny-UzxIFYEeJgFNaSJTGZLuwHUY/?page=1",35,art + 'yoga.png')
        addDir3('[COLOR aqua]'+translate(950016)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLui6Eyny-UzwxbWCWDbTzEwsZnnROBTIL/?page=1",35,art + 'yoga.png')
        addDir3('[COLOR aqua]'+translate(950017)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLiRWC7Q54GiqQ5YTQkyqT4IoyVY83qn-h/?page=1",35,art + 'yoga.png')
        addDir3('[COLOR aqua]'+translate(950018)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLiRWC7Q54GiotNNwM2EHiMTqv-Kc838On/?page=1",35,art + 'yoga.png')




def makeupy():
        addDir3('[COLOR aqua]'+translate(960001)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLFXDHq8EOmDn2pbbDjKxmozigY_xSznd7/?page=1",35,art + 'makeup.png')
        addDir3('[COLOR aqua]'+translate(960002)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLFXDHq8EOmDk96Zi8ibHerZ7pkQD3_bsr/?page=1",35,art + 'makeup.png')
        addDir3('[COLOR aqua]'+translate(960003)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLFXDHq8EOmDlro7O-7ehHR1zvBGybh1gq/?page=1",35,art + 'makeup.png')
        addDir3('[COLOR aqua]'+translate(960004)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLFXDHq8EOmDmHeuxiQskYVRnmvQmBsYhi/?page=1",35,art + 'makeup.png')
        addDir3('[COLOR aqua]'+translate(960005)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLFXDHq8EOmDncTAQrC9W990a0dBtUFVyH/?page=1",35,art + 'makeup.png')
        addDir3('[COLOR aqua]'+translate(960006)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLFXDHq8EOmDkL26eSMDUXFdr3_zZ1HrPM/?page=1",35,art + 'makeup.png')
        addDir3('[COLOR aqua]'+translate(960007)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLFXDHq8EOmDnupay8fnrOSKvXXnbB-SOW/?page=1",35,art + 'makeup.png')
        addDir3('[COLOR aqua]'+translate(960009)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLFXDHq8EOmDnDeKTJ_pSx38KgMgISFJe_/?page=1",35,art + 'makeup.png')
        addDir3('[COLOR aqua]'+translate(960010)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLFXDHq8EOmDkP2UQ5QDu8DdWZELEt_SkQ/?page=1",35,art + 'makeup.png')
        addDir3('[COLOR aqua]'+translate(960011)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLFXDHq8EOmDl98smEUzA8FT9Vq4QSk9zQ/?page=1",35,art + 'makeup.png')
        addDir3('[COLOR aqua]'+translate(960012)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLFXDHq8EOmDla8l08ACyq9HHUbspDUW4f/?page=1",35,art + 'makeup.png')
        addDir3('[COLOR aqua]'+translate(960013)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLqrO4mc6RUZ1_qzjLQXdwDAZ64G2FC9G6/?page=1",35,art + 'makeup.png')
        addDir3('[COLOR aqua]'+translate(960014)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLqrO4mc6RUZ0235ria9ERbja6KYJjfFsI/?page=1",35,art + 'makeup.png')
        addDir3('[COLOR aqua]'+translate(960015)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLqrO4mc6RUZ2tz5hzygNN_V534AueUrr9/?page=1",35,art + 'makeup.png')
        addDir3('[COLOR aqua]'+translate(960016)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLqrO4mc6RUZ16Fo-07RdO1tWI52QV0EPU/?page=1",35,art + 'makeup.png')
        addDir3('[COLOR aqua]'+translate(960017)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLqrO4mc6RUZ2yOt-tN_39_RLx2-jTNvrk/?page=1",35,art + 'makeup.png')
        addDir3('[COLOR aqua]'+translate(960018)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLqrO4mc6RUZ3dIAlWlmEuGbhmRDZMkTfF/?page=1",35,art + 'makeup.png')
        addDir3('[COLOR aqua]'+translate(960019)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLqrO4mc6RUZ09_liYs7AF1SkTWifaYvAI/?page=1",35,art + 'makeup.png')
        addDir3('[COLOR aqua]'+translate(960021)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLqrO4mc6RUZ36DDv8xQVtEvh5vZys6eYV/?page=1",35,art + 'makeup.png')
        addDir3('[COLOR aqua]'+translate(960022)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLqrO4mc6RUZ2wfo7JsLyUcsHN4iAA4FrL/?page=1",35,art + 'makeup.png')
        addDir3('[COLOR aqua]'+translate(960023)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLqrO4mc6RUZ31heO5EEuPhJnukmCXrbhz/?page=1",35,art + 'makeup.png')
        addDir3('[COLOR aqua]'+translate(960024)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLzVhGARzals0Mq60Vh45rHJ-O5CO77aZv/?page=1",35,art + 'makeup.png')
        addDir3('[COLOR aqua]'+translate(960025)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLzVhGARzals1SsNYtgViwCaVkis6blrPA/?page=1",35,art + 'makeup.png')
        addDir3('[COLOR aqua]'+translate(960026)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLzVhGARzals3nwticn-2TdWye7NkXXPyX/?page=1",35,art + 'makeup.png')
        addDir3('[COLOR aqua]'+translate(960027)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLzVhGARzals1TmxNY8UqVj3Hflpl_jqtH/?page=1",35,art + 'makeup.png')
        addDir3('[COLOR aqua]'+translate(960028)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLzVhGARzals0QMJFzdKG2h23bZqGytzJ1&index=4/?page=1",35,art + 'makeup.png')
        addDir3('[COLOR aqua]'+translate(960029)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLzVhGARzals1BfbV-QmAcxi4sBwN1B5gI/?page=1",35,art + 'makeup.png')
        addDir3('[COLOR aqua]'+translate(960030)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLiRWC7Q54GioXKgbaifrEfR-MFOMgibc2/?page=1",35,art + 'makeup.png')
        addDir3('[COLOR aqua]'+translate(960031)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLiRWC7Q54GioxI08Rv1TfklGBElDQAN43/?page=1",35,art + 'makeup.png')



def nutritiony():
        addDir('[COLOR aqua]אוכל ובישול [/COLOR]','url',9876517,art + 'cooking.png')
        addDir3('[COLOR aqua]'+translate(970001)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLOZ5nscrPV8-A-8jwKUa5o5gCoOEyLhIn/?page=1",35,art + 'nutrition.png')
        addDir3('[COLOR aqua]'+translate(970002)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLiRWC7Q54Gioo6w9A2nNdL-mrGUh78V-n/?page=1",35,art + 'nutrition.png')
        addDir3('[COLOR aqua]'+translate(970003)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLiRWC7Q54Giq6Dz1S0SV2JwP2jjCI1rGZ/?page=1",35,art + 'nutrition.png')
        addDir3('[COLOR aqua]'+translate(970004)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLiRWC7Q54GipTRJBIkECddRvS2rlJ8Pm7/?page=1",35,art + 'nutrition.png')
        addDir3('[COLOR aqua]'+translate(970005)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLRASpuvjMTWacQDUkuj8fEps665OyWwRB/?page=1",35,art + 'nutrition.png')
        addDir3('[COLOR aqua]'+translate(970006)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLiRWC7Q54Gio9WFuWPNfimkR3PAzUUKEp/?page=1",35,art + 'nutrition.png')


def healthy():
        addDir3('[COLOR aqua]'+translate(980001)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLOZ5nscrPV89p2nUMt0NhA3x7_r2PSR8Z/?page=1",35,art + 'health.png')
        addDir3('[COLOR aqua]'+translate(980002)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLiRWC7Q54GiqCc46RphIDB-z2v2gvcSjI/?page=1",35,art + 'health.png')
        addDir3('[COLOR aqua]'+translate(980003)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLFXDHq8EOmDmBoNj0sL8fxBhvTwcXbh8q/?page=1",35,art + 'health.png')
        addDir3('[COLOR aqua]'+translate(980004)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLOZ5nscrPV8_RBfntU95GGO06xZP7oPTX/?page=1",35,art + 'health.png')
        addDir3('[COLOR aqua]'+translate(980005)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLOZ5nscrPV8_QjeLeLPoWDiwIthS-wCio/?page=1",35,art + 'health.png')
        addDir3('[COLOR aqua]'+translate(980006)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLOZ5nscrPV884L8qUfArGFJLUOBw7DZdn/?page=1",35,art + 'health.png')
        addDir3('[COLOR aqua]'+translate(980007)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLOZ5nscrPV8-ERQ71bqMoZDGC_j5RRUvD/?page=1",35,art + 'health.png')
        addDir3('[COLOR aqua]'+translate(980008)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLOZ5nscrPV882yCk_t1reNvyNaFR-HTgG/?page=1",35,art + 'health.png')
        addDir3('[COLOR aqua]'+translate(980011)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLOZ5nscrPV8_LUZgY4LeYHH3BX3vz1Bsw/?page=1",35,art + 'health.png')
        addDir3('[COLOR aqua]'+translate(980012)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLiRWC7Q54GipLl8pJriQw_G5pTY4yCwaX/?page=1",35,art + 'health.png')
        addDir3('[COLOR aqua]'+translate(980013)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLiRWC7Q54GipPDl1tX2m9K6vy2mxUIJ1O/?page=1",35,art + 'health.png')
        addDir3('[COLOR aqua]'+translate(980014)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLiRWC7Q54GioJgKYb-INFeeAVRzUQWheC/?page=1",35,art + 'health.png')
        addDir3('[COLOR aqua]'+translate(980015)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLiRWC7Q54Gir72RvSiYQRpp_UsJA_K7uu/?page=1",35,art + 'health.png')
        addDir3('[COLOR aqua]'+translate(980016)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLiRWC7Q54Gir-8ToAGOlr7kEjxnEzJXck/?page=1",35,art + 'health.png')
        addDir3('[COLOR aqua]'+translate(980017)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLN7ydbvoUTMU41t1mRrkpEkXvXnK5a3ie&index=4/?page=1",35,art + 'health.png')
        addDir3('[COLOR aqua]'+translate(980018)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLtJVSAZ-prxoe7rT17G6KHTWeZKxUtUpA&index=3/?page=1",35,art + 'health.png')
        addDir3('[COLOR aqua]'+translate(980019)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLRASpuvjMTWafSsLquQKZxptsqKUCBxuM/?page=1",35,art + 'health.png')
        addDir3('[COLOR aqua]'+translate(980020)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLiRWC7Q54GioRMDeVmPmSE9E2VcCd1KFF/?page=1",35,art + 'health.png')
        addDir3('[COLOR aqua]'+translate(980021)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLRASpuvjMTWb8wkRYVoDJaP87PPgOzOvX/?page=1",35,art + 'health.png')
        addDir3('[COLOR aqua]'+translate(980022)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLRASpuvjMTWalheVtnAjthpSd5gCKfjav/?page=1",35,art + 'health.png')





def sportsy():
        addDir3('[COLOR aqua]'+translate(990001)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLMHMyl3oeyh3BqeGm4CTfixEQ1oGKGe4A/?page=1",35,art + 'sports.png')
        addDir3('[COLOR aqua]'+translate(990002)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLMHMyl3oeyh00NqGBY-Y4WxPRInh9s5ul/?page=1",35,art + 'sports.png')
        addDir3('[COLOR aqua]'+translate(990003)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLMHMyl3oeyh2TOD62h5_ljtiyqwE9i2pU/?page=1",35,art + 'sports.png')
        addDir3('[COLOR aqua]'+translate(990004)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLMHMyl3oeyh2X2Cf3kQ7RWJX2sb3CWZ_-/?page=1",35,art + 'sports.png')
        addDir3('[COLOR aqua]'+translate(990005)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLMHMyl3oeyh1zWX_45mwhUyY31o2yYwd2/?page=1",35,art + 'sports.png')
        addDir3('[COLOR aqua]'+translate(990008)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLiRWC7Q54GipVZHs1YGurwFNK-gktSd3T/?page=1",35,art + 'sports.png')


def bidory():
        addDir3('[COLOR aqua]'+translate(911001)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PL9Pg1--nVI-CoPB9IdwmSkRufOgpuCl7z/?page=1",35,art + 'bidor.png')
        addDir3('[COLOR aqua]'+translate(911002)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PL9Pg1--nVI-Dec23P2ZkgwLxKJNfLtRHT/?page=1",35,art + 'bidor.png')
        addDir3('[COLOR aqua]'+translate(911003)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PL9Pg1--nVI-DPm0PZafI_RrVUbs00KR4V&index=8/?page=1",35,art + 'bidor.png')
        addDir3('[COLOR aqua]'+translate(911004)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PL9Pg1--nVI-BzGNV3cOUQfuGH0HGFPA3c/?page=1",35,art + 'bidor.png')
        addDir3('[COLOR aqua]'+translate(911005)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PL9Pg1--nVI-A_YA5q6FJRJCU-2eun-XvL/?page=1",35,art + 'bidor.png')
        addDir3('[COLOR aqua]'+translate(911006)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PL9Pg1--nVI-A-ZyCv5VWIf1w18Z9o7lnB/?page=1",35,art + 'bidor.png')
        addDir3('[COLOR aqua]'+translate(911007)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PL9Pg1--nVI-CmL20prVKQypHq80yD8O5c/?page=1",35,art + 'bidor.png')
        addDir3('[COLOR aqua]'+translate(911008)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLiRWC7Q54GiqaoOxINXZftJyCxA0vlcfn/?page=1",35,art + 'bidor.png')
        addDir3('[COLOR aqua]'+translate(911009)+'[/COLOR]',"plugin://plugin.video.youtube/playlist/PLSYnaPG2TDbw1RSrTSf7JRL6bLUkpbfFP/?page=1",35,art + 'bidor.png')












def daty():

        addDir('[COLOR aqua]זמני הדלקת נרות [/COLOR]','url',10001,'https://www.kipa.co.il/images/shabbat_times.jpg')
        addDir('[COLOR aqua]חגי ישראל [/COLOR]','url',987651928,'https://d3m9l0v76dty0.cloudfront.net/system/photos/2425670/large/237190d8c6cf6079514a1093ad4c08c6.jpg')

        addDir3('[COLOR aqua]ענפים-מיטב הרבנים[/COLOR]',"plugin://plugin.video.youtube/channel/UCP8gwVljbOwSfO-Qs8zR7VA/?page=1",35,'https://lh3.googleusercontent.com/de7wDKbbGqxMvthIjin6IbSG2z3tPlzAvYvDOkcMyQZVfVsPFPoJxJuVDOQAtkUWw4I')


        addDir3('[COLOR aqua]ענפים-מיטב הרבנים(פלייליסטים)[/COLOR]',"plugin://plugin.video.youtube/channel/UCP8gwVljbOwSfO-Qs8zR7VA?description=פלייליסטים&fanart= &iconimage= &mode=8&name=פלייליסטים&url=https://www.youtube.com/channel/UCP8gwVljbOwSfO-Qs8zR7VA/playlists/?page=1",35,'https://lh3.googleusercontent.com/de7wDKbbGqxMvthIjin6IbSG2z3tPlzAvYvDOkcMyQZVfVsPFPoJxJuVDOQAtkUWw4I')

        addDir3('[COLOR aqua]סרטי יהדות[/COLOR]',"plugin://plugin.video.youtube/playlist/PLNv4kSCPbshmAORCqOUqIX1PkA8x8ubEw/?page=1",35,'https://i.ytimg.com/vi/WorpPgAJ-Qc/maxresdefault.jpg')

        addDir3('[COLOR aqua]אליהו הנביא שידור[/COLOR]',"plugin://plugin.video.youtube/channel/UCMSN4UwZXeXTMLiBjacrEcQ/?page=1",35,'https://yt3.ggpht.com/a-/AAuE7mCmHdQaddshBoXQ5kDwdNxuMcavlAL5lz-A0A=s900-mo-c-c0xffffffff-rj-k-no')


        addDir3('[COLOR aqua]עולם היהדות והקבלה[/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=%d7%a2%d7%95%d7%9c%d7%9d%20%d7%94%d7%99%d7%94%d7%93%d7%95%d7%aa%20%d7%95%d7%94%d7%a7%d7%91%d7%9c%d7%94&search_type=playlist",35,'https://yt3.ggpht.com/a-/AAuE7mDUH15GkcDahJJORg9y_Ry3P973shqkJa-fvQ=s900-mo-c-c0xffffffff-rj-k-no')

        addDir3('[COLOR aqua]יהדות תוכן כללי[/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=%d7%99%d7%94%d7%93%d7%95%d7%aa&search_type=playlist",35,'https://lh3.googleusercontent.com/8DHyOIbBsY_ncTLXmrP027y03-cnohrbH-nRZT-Do_Oj3Bz-DekDJ_wxGLJGydIJaa4')

        addDir3('[COLOR aqua]ברסלב ישראל [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=ברסלב ישראל &search_type=playlist",35,'https://cdn1.player.fm/images/6562898/series/wOxTJ6S3rfnSW9D0/512.jpg ')

        addDir3('[COLOR aqua]הידברות HD[/COLOR]',"plugin://plugin.video.youtube/channel/UCQDDeGFnMl4Wj7QogO_5Gvg/?page=1",35,'https://is2-ssl.mzstatic.com/image/thumb/Purple4/v4/db/dd/c9/dbddc9ea-5011-ed96-8a70-df2dac5735c0/source/512x512bb.jpg')

        addDir3('[COLOR aqua]ניצוצות של קדושה[/COLOR]',"plugin://plugin.video.youtube/channel/UConTSc42kuOIIL29oBUGkPw/?page=1",35,'http://img.sur.ly/thumbnails/620x343/n/nitzotzotonline.com.png')


        addDir3('[COLOR aqua]מוסאיוף שיעורי תורה[/COLOR]',"plugin://plugin.video.youtube/channel/UCzo-VlvApSjAocpmQ_uQb8w/?page=1",35,'https://i.ytimg.com/vi/GwqDZA7wEtM/hqdefault.jpg')


        addDir3('[COLOR aqua]הרב רונן שאולוב [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=הרב רונן שאולוב &search_type=playlist",35,'https://yt3.ggpht.com/a/AGF-l797HZ0ZEcvD37LUxjBW8NlAMA_dNqtjsngccw=s900-mo-c-c0xffffffff-rj-k-no ')

        addDir3('[COLOR aqua]הרב אהרון לוי [/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=הרב אהרון לוי &search_type=playlist",35,'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSnv0in5E0fvaJ0_uGIfCS-gTPvIOOxnlIefv6eQRen492xbAP0 ')


        addDir3('[COLOR aqua]ערכים[/COLOR]',"plugin://plugin.video.youtube/channel/UCzcBbfqNUNyC3Vd0SGBTi_Q/?page=1",35,'https://yt3.ggpht.com/-x0wEBEM22Nc/AAAAAAAAAAI/AAAAAAAAAAA/6yHUMyB1mv8/s240-c-k-no-mo-rj-c0xffffff/photo.jpg')

        addDir3('[COLOR aqua]יהדות ברשת[/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=יהדות ברשת&search_type=playlist",35,'https://i.ytimg.com/vi/1wHD77jb0L0/hqdefault.jpg')




def dat1():

        addDir3('[COLOR red]יש צורך בהרחבת לייב סטרים פרו[/COLOR]',"777",35,'https://raw.githubusercontent.com/Gujal00/GujalKodiWork/master/upto_leia/zips/plugin.video.live.streamspro/icon.png')

        addDir3('[COLOR aqua]ירושלים[/COLOR]',"plugin://plugin.video.live.streamspro/?fanart=C%3a%5cUsers%5cUser%5cAppData%5cRoaming%5cKodi%5caddons%5cplugin.video.live.streamspro%5cfanart.jpg&mode=1&name=%d7%99%d7%a8%d7%95%d7%a9%d7%9c%d7%99%d7%9d&url=https%3a%2f%2fwww.hebcal.com%2fshabbat%2f%3fcfg%3dr%26geonameid%3d281184%26i%3don%26m%3d50%26pubDate%3d0%26lg%3dh",35,'http://www.aljanh.net/data/archive/img/164569631.jpeg')

        addDir3('[COLOR aqua]חיפה[/COLOR]',"plugin://plugin.video.live.streamspro/?fanart=C%3a%5cUsers%5cUser%5cAppData%5cRoaming%5cKodi%5caddons%5cplugin.video.live.streamspro%5cfanart.jpg&mode=1&name=%d7%97%d7%99%d7%a4%d7%94&url=https%3a%2f%2fwww.hebcal.com%2fshabbat%2f%3fcfg%3dr%26geonameid%3d294801%26i%3don%26m%3d50%26pubDate%3d0%26lg%3dh",35,'https://kanweb.blob.core.windows.net/download/pictures/cat37427_img616817293.jpg')

        addDir3('[COLOR aqua]תל אביב[/COLOR]',"plugin://plugin.video.live.streamspro/?fanart=C%3a%5cUsers%5cUser%5cAppData%5cRoaming%5cKodi%5caddons%5cplugin.video.live.streamspro%5cfanart.jpg&mode=1&name=%d7%aa%d7%9c%20%d7%90%d7%91%d7%99%d7%91&url=https%3a%2f%2fwww.hebcal.com%2fshabbat%2f%3fcfg%3dr%26geonameid%3d293397%26i%3don%26m%3d50%26pubDate%3d0%26lg%3dh",35,'https://i.ytimg.com/vi/NWOeWOwJHvA/maxresdefault.jpg')

        addDir3('[COLOR aqua]טבריה[/COLOR]',"plugin://plugin.video.live.streamspro/?fanart=C%3a%5cUsers%5cUser%5cAppData%5cRoaming%5cKodi%5caddons%5cplugin.video.live.streamspro%5cfanart.jpg&mode=1&name=%d7%98%d7%91%d7%a8%d7%99%d7%94&url=https%3a%2f%2fwww.hebcal.com%2fshabbat%2f%3fcfg%3dr%26geonameid%3d293322%26i%3don%26m%3d50%26pubDate%3d0%26lg%3dh",35,'https://images.globes.co.il/images/NewGlobes/big_image_800/2017/tv800.jpg')

        addDir3('[COLOR aqua]אילת[/COLOR]',"plugin://plugin.video.live.streamspro/?fanart=C%3a%5cUsers%5cUser%5cAppData%5cRoaming%5cKodi%5caddons%5cplugin.video.live.streamspro%5cfanart.jpg&mode=1&name=%d7%90%d7%99%d7%9c%d7%aa&url=https%3a%2f%2fwww.hebcal.com%2fshabbat%2f%3fcfg%3dr%26geonameid%3d295277%26i%3don%26m%3d50%26pubDate%3d0%26lg%3dh",35,'https://www.ynet.co.il/PicServer5/2019/03/06/9105175/888.PNG')







def dok3y():




        addDir3('[COLOR aqua]Alien & UFO Documentaries[/COLOR]',"plugin://plugin.video.youtube/playlist/PLZT-q12T7cjjUC5BE6cZ77uD_cwCfpfyU/?page=1",35,'https://i.imgur.com/OcIWNOl.jpg')

        addDir3('[COLOR aqua]Alien & UFO Documentaries (2)[/COLOR]',"plugin://plugin.video.youtube/playlist/PL3OtDBB37OBjqge_LtrPprNgbeJmm-dsM/?page=1",35,'https://i.imgur.com/OcIWNOl.jpg')



        addDir3('[COLOR aqua]American Experience Documentary[/COLOR]',"plugin://plugin.video.youtube/playlist/PLUxyHtHaofGb6gA9-btv4LIIqDjeahOPe/?page=1",35,'https://i.imgur.com/OcIWNOl.jpg')

        addDir3('[COLOR aqua]American History Documentary[/COLOR]',"plugin://plugin.video.youtube/playlist/PLF1C3AE92622C2780/?page=1",35,'https://i.imgur.com/OcIWNOl.jpg')



        addDir3('[COLOR aqua]BBC Documentaries[/COLOR]',"plugin://plugin.video.youtube/playlist/PLDVZNJR18KqBfusnr5G4D6Ft6ge-lJhWK/?page=1",35,'https://i.imgur.com/OcIWNOl.jpg')

        addDir3('[COLOR aqua]BBC History Documentaries[/COLOR]',"plugin://plugin.video.youtube/playlist/PL2XMHriRjzy0-VocW_OoTdVA9o_GuJcE0/?page=1",35,'https://i.imgur.com/OcIWNOl.jpg')

        addDir3('[COLOR aqua]BBC Music Documentaries[/COLOR]',"plugin://plugin.video.youtube/playlist/PLOvXkB5eFXm7lfggMnEO1TWzENy-0YhVP/?page=1",35,'https://i.imgur.com/OcIWNOl.jpg')

        addDir3('[COLOR aqua]Biography/History Channel Documentaries[/COLOR]',"plugin://plugin.video.youtube/playlist/PLvowN7rzMGUFOMOiA4hqKMDWnb1_cagKx/?page=1",35,'https://i.imgur.com/OcIWNOl.jpg')

        addDir3('[COLOR aqua]Boxing Documentaries[/COLOR]',"plugin://plugin.video.youtube/playlist/PLtCY5b9Q0auBpDAYD-BSvQzq4CbABhLXQ/?page=1",35,'https://i.imgur.com/OcIWNOl.jpg')

        addDir3('[COLOR aqua]British Army Documentary[/COLOR]',"plugin://plugin.video.youtube/playlist/PLaJSCDqmHPo4xrGMvRiIrfp2MIFVTlhGk/?page=1",35,'https://i.imgur.com/OcIWNOl.jpg')

        addDir3('[COLOR aqua]British Military & History Documentary[/COLOR]',"plugin://plugin.video.youtube/playlist/PL57C1E76348A209F3/?page=1",35,'https://i.imgur.com/OcIWNOl.jpg')

        addDir3('[COLOR aqua]Conspiracy theory & Documentary[/COLOR]',"plugin://plugin.video.youtube/playlist/PLQy6xVkiQuV77b7P116vfxLxf0D4V2nOK/?page=1",35,'https://i.imgur.com/OcIWNOl.jpg')

        addDir3('[COLOR aqua]Crime & Story Documentary[/COLOR]',"plugin://plugin.video.youtube/playlist/PLjYTdfYGUqXWdPPBppWuk3hOpXiLwZXoM/?page=1",35,'https://i.imgur.com/OcIWNOl.jpg')



        addDir3('[COLOR aqua]Cycling Documentaries[/COLOR]',"plugin://plugin.video.youtube/playlist/PL7cCA7f-KRxN_w78iKFxC9DyPHfw3t_5-/?page=1",35,'https://i.imgur.com/OcIWNOl.jpg')

        addDir3('[COLOR aqua]Documentaries[/COLOR]',"plugin://plugin.video.youtube/playlist/PL991qh8jWvSdM-kydtQh5X9-nUXUgu8b_/?page=1",35,'https://i.imgur.com/OcIWNOl.jpg')

        addDir3('[COLOR aqua]Drink & Drugs Documentaries[/COLOR]',"plugin://plugin.video.youtube/playlist/PL6fAGtJIQh9urgOktKP3umtMXwBckN6TU/?page=1",35,'https://i.imgur.com/OcIWNOl.jpg')



        addDir3('[COLOR aqua]FBI Files[/COLOR]',"plugin://plugin.video.youtube/playlist/PL5q8VRGX_yLL_CruUIU-ZE3d0L7JJH-ee/?page=1",35,'https://i.imgur.com/OcIWNOl.jpg')

        addDir3('[COLOR aqua]Football Documentaries[/COLOR]',"plugin://plugin.video.youtube/playlist/PLPG-HjhZmZfN6t7pn0KkhEC6mQOlP1ZKo/?page=1",35,'https://i.imgur.com/OcIWNOl.jpg')

        addDir3('[COLOR aqua]History,Military & War Documentary[/COLOR]',"plugin://plugin.video.youtube/playlist/PLa1-vLrslkqlMbVRAw5QIw7UknJ0fTcnz/?page=1",35,'https://i.imgur.com/OcIWNOl.jpg')

        addDir3('[COLOR aqua]History/Archaeology Documentaries[/COLOR]',"plugin://plugin.video.youtube/playlist/PLwJVQxW2IAat6kGzPQy5xjRcXbxwhEcar/?page=1",35,'https://i.imgur.com/OcIWNOl.jpg')



        addDir3('[COLOR aqua]Long History Documentaries[/COLOR]',"plugin://plugin.video.youtube/playlist/PLZctZ0yYTg4W4dvyFca9Yu6RK9inYHLtp/?page=1",35,'https://i.imgur.com/OcIWNOl.jpg')



        addDir3('[COLOR aqua]Military & War Documentary[/COLOR]',"plugin://plugin.video.youtube/playlist/PLEE2489E06F15D873/?page=1",35,'https://i.imgur.com/OcIWNOl.jpg')

        addDir3('[COLOR aqua]Mobsters Documentary[/COLOR]',"plugin://plugin.video.youtube/playlist/PL5q8VRGX_yLL9M8v6PWXFjNJYIA5771Lr/?page=1",35,'https://i.imgur.com/OcIWNOl.jpg')



        addDir3('[COLOR aqua]My Crime Stories Documentaries[/COLOR]',"plugin://plugin.video.youtube/playlist/PLYsohyI13lcQPTEcBz8YxvDWtSsxRgstD/?page=1",35,'https://i.imgur.com/OcIWNOl.jpg')

        addDir3('[COLOR aqua]NBA Documentaries[/COLOR]',"plugin://plugin.video.youtube/playlist/PL394rozWCpDdV9yacdy4oAZ3qiXYf4dT5/?page=1",35,'https://i.imgur.com/OcIWNOl.jpg')

        addDir3('[COLOR aqua]NFL Documentaries[/COLOR]',"plugin://plugin.video.youtube/playlist/PLnzcLTdWZeqKLI_cW4tHYzVYalsTFMgrW/?page=1",35,'https://i.imgur.com/OcIWNOl.jpg')

        addDir3('[COLOR aqua]National Geographic Documentary[/COLOR]',"plugin://plugin.video.youtube/playlist/PLlHanBMNk-DLSFPn4hK24KzwdKHA5H934/?page=1",35,'https://i.imgur.com/OcIWNOl.jpg')

        addDir3('[COLOR aqua]Nature Documentaries[/COLOR]',"plugin://plugin.video.youtube/playlist/PL5o3ll3G4acxgDMSO7JXvDsosQ-UDPL6n/?page=1",35,'https://i.imgur.com/OcIWNOl.jpg')

        addDir3('[COLOR aqua]Northern Ireland Documentary[/COLOR]',"plugin://plugin.video.youtube/playlist/PLuBt-Sf8Ynx2BuLQhjx5v8-svqIf_1phj/?page=1",35,'https://i.imgur.com/OcIWNOl.jpg')



        addDir3('[COLOR aqua]PDS Nova Documentaries[/COLOR]',"plugin://plugin.video.youtube/playlist/PLlHanBMNk-DKQzkktkFKGvJR_9gSRDhBr/?page=1",35,'https://i.imgur.com/OcIWNOl.jpg')

        addDir3('[COLOR aqua]Paranormal Documentaries[/COLOR]',"plugin://plugin.video.youtube/playlist/PLFA4FDF0842092039/?page=1",35,'https://i.imgur.com/OcIWNOl.jpg')

        addDir3('[COLOR aqua]Rare UFO Documentaries[/COLOR]',"plugin://plugin.video.youtube/playlist/PLajqNV0-qkKeZtNvbNCBzoDrZ5NCmD7QK/?page=1",35,'https://i.imgur.com/OcIWNOl.jpg')

        addDir3('[COLOR aqua]Real Crime Uk Documentaries[/COLOR]',"plugin://plugin.video.youtube/playlist/PL152bjytsMC7X2jHHtOAKGBeq1bvx87aE/?page=1",35,'https://i.imgur.com/OcIWNOl.jpg')

        addDir3('[COLOR aqua]Scotland Yard Documentary[/COLOR]',"plugin://plugin.video.youtube/playlist/PLECCBBA5FD7BD6165/?page=1",35,'https://i.imgur.com/OcIWNOl.jpg')



        addDir3('[COLOR aqua]Serial Killers Global Documentary[/COLOR]',"plugin://plugin.video.youtube/playlist/PLvQ9zpL9arDylTPwOVygvegBCGqOltidW/?page=1",35,'https://i.imgur.com/OcIWNOl.jpg')

        addDir3('[COLOR aqua]ShowTime Documentaries[/COLOR]',"plugin://plugin.video.youtube/playlist/PL-7ED26K3EdTHbydPw8xTVF93n0XQ7sRf/?page=1",35,'https://i.imgur.com/OcIWNOl.jpg')

        addDir3('[COLOR aqua]Sports Documentaries[/COLOR]',"plugin://plugin.video.youtube/playlist/PLT0ii4_I8EN50KMtVsAjB5dLRbyLT6xZD/?page=1",35,'https://i.imgur.com/OcIWNOl.jpg')

        addDir3('[COLOR aqua]Spy Documentary[/COLOR]',"plugin://plugin.video.youtube/playlist/PLKh8r07IjZ4riZvDv0m_DfDKeeu5EuRfE/?page=1",35,'https://i.imgur.com/OcIWNOl.jpg')

        addDir3('[COLOR aqua]Spy Documentary[/COLOR]',"plugin://plugin.video.youtube/playlist/PLKh8r07IjZ4riZvDv0m_DfDKeeu5EuRfE/?page=1",35,'https://i.imgur.com/OcIWNOl.jpg')



        addDir3('[COLOR aqua]The Ripperologists Jack the Ripper Documentaries[/COLOR]',"plugin://plugin.video.youtube/playlist/PLK7KBLQJFmZUrjhaEUcIeGkWwWSAf1T9I/?page=1",35,'https://i.imgur.com/OcIWNOl.jpg')

        addDir3('[COLOR aqua]The best of Ancient Aliens & UFO Documentaries[/COLOR]',"plugin://plugin.video.youtube/playlist/PLTjuA49CCFCDyfD76teqnPzB_EH_WKH2J/?page=1",35,'https://i.imgur.com/OcIWNOl.jpg')

        addDir3('[COLOR aqua]Time Watch Documentaries[/COLOR]',"plugin://plugin.video.youtube/playlist/PL6aq1PBlrtR7rgc03uveAtgMWtTArxXSJ/?page=1",35,'https://i.imgur.com/OcIWNOl.jpg')



        addDir3('[COLOR aqua]Unsealed Alien Files Documentaries[/COLOR]',"plugin://plugin.video.youtube/playlist/PLnr-o7LcbD14eZPSB715kNsYOEQ6GmihT/?page=1",35,'https://i.imgur.com/OcIWNOl.jpg')

        addDir3('[COLOR aqua]VIETNAM War Documentary[/COLOR]',"plugin://plugin.video.youtube/playlist/PLDx09dtcE4z5qSZ1oDkKQ3qyBULjlME3O/?page=1",35,'https://i.imgur.com/OcIWNOl.jpg')

        addDir3('[COLOR aqua]Very Interesting Documentary[/COLOR]',"plugin://plugin.video.youtube/playlist/PLhGe8UxzOI2PFve_KHoYxCKgTrT4IJ4PS/?page=1",35,'https://i.imgur.com/OcIWNOl.jpg')



        addDir3('[COLOR aqua]Wild Series Documentaries[/COLOR]',"plugin://plugin.video.youtube/playlist/PL6aq1PBlrtR5D4xslD4VBos7zk0GSTuBb/?page=1",35,'https://i.imgur.com/OcIWNOl.jpg')

        addDir3('[COLOR aqua]Witness Documentaries[/COLOR]',"plugin://plugin.video.youtube/playlist/PL2CCCAC08769C2FE9/?page=1",35,'https://i.imgur.com/OcIWNOl.jpg')

        addDir3('[COLOR aqua]World History Documentaries[/COLOR]',"plugin://plugin.video.youtube/playlist/PLR3SowCQah02FYPAFXOFH2Vy1qcAmIJ_A/?page=1",35,'https://i.imgur.com/OcIWNOl.jpg')


def trlrsrty():



        addDir3('[COLOR aqua]הטוב ביותר בישראל![/COLOR]',"plugin://plugin.video.youtube/channel/UCnY51bp10OxDUwNDKKnCMgg/playlists/?page=1",35,'https://yt3.ggpht.com/-l0S3cJpdAXI/AAAAAAAAAAI/AAAAAAAAAAA/OmClcgO7WyI/nd/photo.jpg')

        addDir3('[COLOR aqua]הטוב ביותר בעולם![/COLOR]',"plugin://plugin.video.youtube/channel/UCRX7UEyE8kp35mPrgC2sosA/playlists/?page=1",35,'https://yt3.ggpht.com/-l0S3cJpdAXI/AAAAAAAAAAI/AAAAAAAAAAA/OmClcgO7WyI/nd/photo.jpg')

        addDir3('[COLOR aqua]מתורגמים מאתר סרטים[/COLOR]',"plugin://plugin.video.youtube/channel/UCrA1_yVsX8bSaKdNiXj0f-w/?page=1",35,'https://yt3.ggpht.com/-l0S3cJpdAXI/AAAAAAAAAAI/AAAAAAAAAAA/OmClcgO7WyI/nd/photo.jpg')

        addDir3('[COLOR aqua]מתורגמים אתר סרט[/COLOR]',"plugin://plugin.video.youtube/channel/UCwLaLrXo8IYqpNfAipy3CGQ/?page=1",35,'https://yt3.ggpht.com/-l0S3cJpdAXI/AAAAAAAAAAI/AAAAAAAAAAA/OmClcgO7WyI/nd/photo.jpg')

        addDir3('[COLOR aqua]סרטים ישראליים[/COLOR]',"plugin://plugin.video.youtube/channel/UCN5mmIG-0CucLSRmdB5hkTQ/?page=1",35,'https://yt3.ggpht.com/-l0S3cJpdAXI/AAAAAAAAAAI/AAAAAAAAAAA/OmClcgO7WyI/nd/photo.jpg')


def POLARISy():

        addDir('[COLOR aqua]דרך (יוטיוב) [/COLOR]','url',9876510008,'https://www.psyshop.com/img/soc1dw081_b.jpg')






def POLARIS2y():


        addDir3('[B][COLOR burlywood]בקשות מיוחדות [/COLOR][/B]',"plugin://plugin.video.youtube/kodion/search/query/?q=ONE Championship - The Home of Martial Arts/?page=1",35,'https://www.psyshop.com/img/soc1dw081_b.jpg')

        addDir3('[B][COLOR burlywood]חלל וחקר [/COLOR][/B]',"plugin://plugin.video.youtube/kodion/search/query/?q=NASA: Need Some Space?/?page=1",35,'https://www.psyshop.com/img/soc1dw081_b.jpg')

        addDir3('[B][COLOR burlywood]תוכניות בתים [/COLOR][/B]',"plugin://plugin.video.youtube/kodion/search/query/?q=Tiny House Expedition: EPIC Road Trip with a BIG Purpose/?page=1",35,'https://www.psyshop.com/img/soc1dw081_b.jpg')

        addDir3('[B][COLOR burlywood]רעיונות עסקיים [/COLOR][/B]',"plugin://plugin.video.youtube/kodion/search/query/?q=Entrepreneur/?page=1",35,'https://www.psyshop.com/img/soc1dw081_b.jpg')

        addDir3('[B][COLOR burlywood]חיסכון בכסף וחיים [/COLOR][/B]',"plugin://plugin.video.youtube/kodion/search/query/?q=Money saving and life hacks North Star*/?page=1",35,'https://www.psyshop.com/img/soc1dw081_b.jpg')

        addDir3('[B][COLOR burlywood]שעות היום ושיחות הלילה [/COLOR][/B]',"plugin://plugin.video.youtube/kodion/search/query/?q=Daytime & Latenight talk shows/?page=1",35,'https://www.psyshop.com/img/soc1dw081_b.jpg')

        addDir3('[B][COLOR burlywood]מארוול [/COLOR][/B]',"plugin://plugin.video.youtube/kodion/search/query/?q=Dnorth Star*/?page=1",35,'https://www.psyshop.com/img/soc1dw081_b.jpg')

        addDir3('[B][COLOR burlywood]ספורט מטורף [/COLOR][/B]'," plugin://plugin.video.youtube/kodion/search/query/?q=FIFATV/?page=1",35,'https://www.psyshop.com/img/soc1dw081_b.jpg')

        addDir3('[B][COLOR burlywood]עולם המים [/COLOR][/B]',"plugin://plugin.video.youtube/kodion/search/query/?q=JacuzziSurfer/?page=1",35,'https://www.psyshop.com/img/soc1dw081_b.jpg')

        addDir3('[B][COLOR burlywood]קריוקי מטורף [/COLOR][/B]',"plugin://plugin.video.youtube/kodion/search/query/?q=Sing King Karaoke/?page=1",35,'https://www.psyshop.com/img/soc1dw081_b.jpg')

        addDir3('[B][COLOR burlywood]קדחת קריוקי [/COLOR][/B]',"plugin://plugin.video.youtube/kodion/search/query/?q=About KaraFun !/?page=1",35,'https://www.psyshop.com/img/soc1dw081_b.jpg')

        addDir3('[B][COLOR burlywood]Car-e-oke Carpool [/COLOR][/B]',"plugin://plugin.video.youtube/kodion/search/query/?q=Car-e-0ke carpool/?page=1",35,'https://www.psyshop.com/img/soc1dw081_b.jpg')

        addDir3('[B][COLOR burlywood]מוסיקה אקספרס [/COLOR][/B]',"plugin://plugin.video.youtube/kodion/search/query/?q=Music express/?page=1",35,'https://www.psyshop.com/img/soc1dw081_b.jpg')

        addDir3('[B][COLOR burlywood]משחקים [/COLOR][/B]',"plugin://plugin.video.youtube/kodion/search/query/?q=Gamers corner/?page=1",35,'https://www.psyshop.com/img/soc1dw081_b.jpg')



def SPORTEXTREMEy():

        addDir('[COLOR aqua]דרך (יוטיוב) [/COLOR]','url',9876510011,'http://extremesportsphilippines.com/wp-content/uploads/2017/09/cropped-extreme-sports-philippines-logo.png')









def SPORTEXTREME2y():



        addDir3('[B][COLOR red]XGAMES[/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=XGAMES/?page=1",35,'http://extremesportsphilippines.com/wp-content/uploads/2017/09/cropped-extreme-sports-philippines-logo.png')

        addDir3('[B][COLOR red]MONSTER ENERGY[/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=MONSTER ENERGY/?page=1",35,'http://extremesportsphilippines.com/wp-content/uploads/2017/09/cropped-extreme-sports-philippines-logo.png')

        addDir3('[B][COLOR red]NITRO CIRCUS[/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=NITRO CIRCUS/?page=1",35,'http://extremesportsphilippines.com/wp-content/uploads/2017/09/cropped-extreme-sports-philippines-logo.png')

        addDir3('[B][COLOR red]GMBN[/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=GMBN/?page=1",35,'http://extremesportsphilippines.com/wp-content/uploads/2017/09/cropped-extreme-sports-philippines-logo.png')

        addDir3('[B][COLOR red]WRC[/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=WRC/?page=1",35,'http://extremesportsphilippines.com/wp-content/uploads/2017/09/cropped-extreme-sports-philippines-logo.png')

        addDir3('[B][COLOR red]MONSTER JAM[/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=MONSTER JAM/?page=1",35,'http://extremesportsphilippines.com/wp-content/uploads/2017/09/cropped-extreme-sports-philippines-logo.png')

        addDir3('[B][COLOR red]RED BULL[/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=RED BULL/?page=1",35,'http://extremesportsphilippines.com/wp-content/uploads/2017/09/cropped-extreme-sports-philippines-logo.png')

        addDir3('[B][COLOR red]THE HOONIGAN[/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=THE HOONIGAN/?page=1",35,'http://extremesportsphilippines.com/wp-content/uploads/2017/09/cropped-extreme-sports-philippines-logo.png')

        addDir3('[B][COLOR red]FORD RACING[/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=FORD RACING/?page=1",35,'http://extremesportsphilippines.com/wp-content/uploads/2017/09/cropped-extreme-sports-philippines-logo.png')

        addDir3('[B][COLOR red]FORMULA DRIFT[/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=driftstream2010/?page=1",35,'http://extremesportsphilippines.com/wp-content/uploads/2017/09/cropped-extreme-sports-philippines-logo.png')

        addDir3('[B][COLOR red]IMSA[/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=UnitedSportsCar/?page=1",35,'http://extremesportsphilippines.com/wp-content/uploads/2017/09/cropped-extreme-sports-philippines-logo.png')

        addDir3('[B][COLOR red]FREESTYLE MOTOCROSS[/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=NIGHToftheJUMPscom/?page=1",35,'http://extremesportsphilippines.com/wp-content/uploads/2017/09/cropped-extreme-sports-philippines-logo.png')

        addDir3('[B][COLOR red]ICE RACING[/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=ICE RACING/?page=1",35,'http://extremesportsphilippines.com/wp-content/uploads/2017/09/cropped-extreme-sports-philippines-logo.png')

        addDir3('[B][COLOR red]SNOCROSS[/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=SNOCROSS/?page=1",35,'http://extremesportsphilippines.com/wp-content/uploads/2017/09/cropped-extreme-sports-philippines-logo.png')

        addDir3('[B][COLOR red]RED BULL AIR RACE[/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=RED BULL AIR RACE/?page=1",35,'http://extremesportsphilippines.com/wp-content/uploads/2017/09/cropped-extreme-sports-philippines-logo.png')

        addDir3('[B][COLOR red]MONSTER SUPERCROSS[/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=MONSTER SUPERCROSS/?page=1",35,'http://extremesportsphilippines.com/wp-content/uploads/2017/09/cropped-extreme-sports-philippines-logo.png')

        addDir3('[B][COLOR red]EXTREME SPORTS[/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=XTremeVideo/?page=1",35,'http://extremesportsphilippines.com/wp-content/uploads/2017/09/cropped-extreme-sports-philippines-logo.png')

        addDir3('[B][COLOR red]WORLD SURF LEAGUE[/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=ASPWorldTour/?page=1",35,'http://extremesportsphilippines.com/wp-content/uploads/2017/09/cropped-extreme-sports-philippines-logo.png')

        addDir3('[B][COLOR red]GOPRO RACING[/B][/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=GoProMX/?page=1",35,'http://extremesportsphilippines.com/wp-content/uploads/2017/09/cropped-extreme-sports-philippines-logo.png')



def binauraly():








        addDir3('[COLOR aqua]• [/COLOR][COLOR white]Binaural Beats[/COLOR]',"plugin://plugin.video.youtube/playlist/PLbXZkxjs1XppzO3CJXArhUGMMRCftofUn/?page=1",35,art + 'yoga.png')


        addDir3('[COLOR aqua]• [/COLOR][COLOR white]Hypnosis Music[/COLOR]',"plugin://plugin.video.youtube/playlist/PLbXZkxjs1Xpq2yKfEhAGq1y_7xbReo5yW/?page=1",35,art + 'yoga.png')


        addDir3('[COLOR aqua]• [/COLOR][COLOR white]Chakra Healing Meditation[/COLOR]',"plugin://plugin.video.youtube/playlist/PLbXZkxjs1Xpo-RVxXo7RB5bfNV0vUvOqX/?page=1",35,art + 'yoga.png')


        addDir3('[COLOR aqua]• [/COLOR][COLOR white]Solfeggio Frequencies[/COLOR]',"plugin://plugin.video.youtube/playlist/PLbXZkxjs1XprI3lBRn49QbZknCJj1ayuE/?page=1",35,art + 'yoga.png')


        addDir3('[COLOR aqua]• [/COLOR][COLOR white]Manifestation Meditation[/COLOR]',"plugin://plugin.video.youtube/playlist/PLbXZkxjs1XprsiFs2ojYbCbqmpxjWmDw9/?page=1",35,art + 'yoga.png')


        addDir3('[COLOR aqua]• [/COLOR][COLOR white]Deep Sleep Music[/COLOR]',"plugin://plugin.video.youtube/playlist/PLbXZkxjs1Xpqs4UMwyepR4-3dXssvBPPH/?page=1",35,art + 'yoga.png')


        addDir3('[COLOR aqua]• [/COLOR][COLOR white]Concentration & Focus Music[/COLOR]',"plugin://plugin.video.youtube/playlist/PLbXZkxjs1XpqdE9dVu12Rfz1EXPteotSn/?page=1",35,art + 'yoga.png')


        addDir3('[COLOR aqua]• [/COLOR][COLOR white]Stress Relief & Healing[/COLOR]',"plugin://plugin.video.youtube/playlist/PLbXZkxjs1XppowhA3bCFIADxtbA_Mo_yB/?page=1",35,art + 'yoga.png')




def Documentarysport3y():

        addDir3('[COLOR aqua]  *Time Team Seasons 1 - 10   [/COLOR]',"plugin://plugin.video.youtube/playlist/PL152bjytsMC4iT-6j0i5XL0X0iFvzFMSs/?page=1",35,art + 'documentary.jpg')
        addDir3('[COLOR aqua]  *Time Team Seasons 11 - 20  [/COLOR]',"plugin://plugin.video.youtube/playlist/PL152bjytsMC4ZNf81GfG-Zssyy80yO2HZ/?page=1",35,art + 'documentary.jpg')
        addDir3('[COLOR aqua]  *Time Team America, Tony Robinson and More  [/COLOR]',"plugin://plugin.video.youtube/playlist/PL152bjytsMC77DGLArw00z61LWsBXFQmj/?page=1",35,art + 'documentary.jpg')
        addDir3('[COLOR aqua] *Timewatch - Time Travellers*   [/COLOR]',"plugin://plugin.video.youtube/playlist/PL152bjytsMC5Xi648qL0kMADk06InTqgG/?page=1",35,art + 'documentary.jpg')


        addDir3('[COLOR aqua]  Three Kingdoms (95 episodes - Eng sub)  [/COLOR]',"plugin://plugin.video.youtube/playlist/PLCldpz_Pc1FrGQLsaxaV0kVPqmXN_nanN/?page=1",35,art + 'documentary.jpg')

        addDir3('[COLOR aqua]  *The Ancient World  [/COLOR]',"plugin://plugin.video.youtube/playlist/PL152bjytsMC5giQaRkK6f5xQC_2dvAeKb/?page=1",35,art + 'documentary.jpg')
        addDir3('[COLOR aqua]  *History Series (1)  [/COLOR]',"plugin://plugin.video.youtube/playlist/PL152bjytsMC4dn12Yx7CyaIlyTXyfDdrD/?page=1",35,art + 'documentary.jpg')
        addDir3('[COLOR aqua]  *History Series (2)  [/COLOR]',"plugin://plugin.video.youtube/playlist/PL152bjytsMC62UzE1wwOTWfVjRKGYTZvF/?page=1",35,art + 'documentary.jpg')
        addDir3('[COLOR aqua]  *Britain  [/COLOR]',"plugin://plugin.video.youtube/playlist/PL152bjytsMC4-YHtvjpH4H2tNkJCKEd1s/?page=1",35,art + 'documentary.jpg')

        addDir3('[COLOR aqua]  *Roman History  [/COLOR]',"plugin://plugin.video.youtube/playlist/PL152bjytsMC5fdzzzgQf85DZUXJBhudpm/?page=1",35,art + 'documentary.jpg')
        addDir3('[COLOR aqua]  *Greek History  [/COLOR]',"plugin://plugin.video.youtube/playlist/PL152bjytsMC6pVpwLD7Xax1QMhs_B0QMF/?page=1",35,art + 'documentary.jpg')
        addDir3('[COLOR aqua]  *Egyptian History  [/COLOR]',"plugin://plugin.video.youtube/playlist/PL152bjytsMC7XMsTB65J6e9OkQyAXFnf7/?page=1",35,art + 'documentary.jpg')
        addDir3('[COLOR aqua]  *Spain  [/COLOR]',"plugin://plugin.video.youtube/playlist/PL152bjytsMC6ZD1oip2wOk5O_V-Nf51MG/?page=1",35,art + 'documentary.jpg')
        addDir3('[COLOR aqua]  *America  [/COLOR]',"plugin://plugin.video.youtube/playlist/PL152bjytsMC6WvxSjTpTXuJAyE1SC9ANZ/?page=1",35,art + 'documentary.jpg')
        addDir3('[COLOR aqua]  *Russia  [/COLOR]',"plugin://plugin.video.youtube/playlist/PL152bjytsMC7tNpr8_TYaorit57Ckq9hU/?page=1",35,art + 'documentary.jpg')
        addDir3('[COLOR aqua]   *India  [/COLOR]',"plugin://plugin.video.youtube/playlist/PL152bjytsMC4D7uHsQ9Ohm_Rls8HBZS9a/?page=1",35,art + 'documentary.jpg')
        addDir3('[COLOR aqua]   *Chin  [/COLOR]',"plugin://plugin.video.youtube/playlist/PL152bjytsMC7_7ASf9UAA1iJGnjiQfU9A/?page=1",35,art + 'documentary.jpg')
        addDir3('[COLOR aqua]  *Japan  [/COLOR]',"plugin://plugin.video.youtube/playlist/PL152bjytsMC4EPwMUgRcqhBGbsYT9zKFK/?page=1",35,art + 'documentary.jpg')
        addDir3('[COLOR aqua]  *Turkey [/COLOR]',"plugin://plugin.video.youtube/playlist/PL152bjytsMC7cOUG1D4IuQuKvjA0jQDl5/?page=1",35,art + 'documentary.jpg')
        addDir3('[COLOR aqua]  *South America  [/COLOR]',"plugin://plugin.video.youtube/playlist/PL152bjytsMC6cBDD6TWFATb4wJBUL95Rd/?page=1",35,art + 'documentary.jpg')
        addDir3('[COLOR aqua]  *France  [/COLOR]',"plugin://plugin.video.youtube/playlist/PL152bjytsMC5i41MA-Cdcmi9oXrOhRbTG/?page=1",35,art + 'documentary.jpg')
        addDir3('[COLOR aqua]  *Australia  [/COLOR]',"plugin://plugin.video.youtube/playlist/PL152bjytsMC7Rc2GtOF1UL1w01OygvdfE/?page=1",35,art + 'documentary.jpg')
        addDir3('[COLOR aqua]  *Biography  [/COLOR]',"plugin://plugin.video.youtube/playlist/PL152bjytsMC7EjdYnGPuDg6etK8yk-UFN/?page=1",35,art + 'documentary.jpg')
        addDir3('[COLOR aqua]  *History - Movies  [/COLOR]',"plugin://plugin.video.youtube/playlist/PL152bjytsMC6fWFVHqexlDboViFEIsGDg/?page=1",35,art + 'documentary.jpg')
        addDir3('[COLOR aqua]  *World War I  [/COLOR]',"plugin://plugin.video.youtube/playlist/PL152bjytsMC4Np0ckVc83HA-bC3ivxMRI/?page=1",35,art + 'documentary.jpg')
        addDir3('[COLOR aqua]  *World War II [/COLOR]',"plugin://plugin.video.youtube/playlist/PL152bjytsMC5wjqK6bXCARgHM6pRneYKs/?page=1",35,art + 'documentary.jpg')
        addDir3('[COLOR aqua]  *Battles Through History  [/COLOR]',"plugin://plugin.video.youtube/playlist/PL152bjytsMC6o3cTgHXzGzOnFoLVQfvsH/?page=1",35,art + 'documentary.jpg')
        addDir3('[COLOR aqua]  *All At Sea  [/COLOR]',"plugin://plugin.video.youtube/playlist/PL152bjytsMC7UxxXcG2aVCPo_ItqZg-GB/?page=1",35,art + 'documentary.jpg')
        addDir3('[COLOR aqua]  *History - Series (3) [/COLOR]',"plugin://plugin.video.youtube/playlist/PL152bjytsMC7HUL4K5EYsOrsn92JnUh0Z/?page=1",35,art + 'documentary.jpg')
        addDir3('[COLOR aqua]  *History - Documentaries  [/COLOR]',"plugin://plugin.video.youtube/playlist/PL152bjytsMC5GUmj1-v7VNWxDostRymeY/?page=1",35,art + 'documentary.jpg')
        addDir3('[COLOR aqua]  *More History Documentaries [/COLOR]',"plugin://plugin.video.youtube/playlist/PL152bjytsMC4fprSWSah3KMbjvEjZU_5q/?page=1",35,art + 'documentary.jpg')

        addDir3('[COLOR aqua]  *Sporting History  [/COLOR]',"plugin://plugin.video.youtube/playlist/PL152bjytsMC4YagWpnkcayYe7VwoiWv5V/?page=1",35,art + 'documentary.jpg')
        addDir3('[COLOR aqua]  *MegaStructures  [/COLOR]',"plugin://plugin.video.youtube/playlist/PL152bjytsMC6xXamnNsrmDXaZetKL9EXH/?page=1",35,art + 'documentary.jpg')
        addDir3('[COLOR aqua]  *History of Music   [/COLOR]',"plugin://plugin.video.youtube/playlist/PL152bjytsMC6PQ1x_B5JN2MEuTZwH-Y3R/?page=1",35,art + 'documentary.jpg')
        addDir3('[COLOR aqua]  Music Makers - History  [/COLOR]',"plugin://plugin.video.youtube/playlist/PL152bjytsMC5jRx_eUEvTJKudxLOYZfXL/?page=1",35,art + 'documentary.jpg')


        addDir3('[COLOR aqua]  British Military and History  [/COLOR]',"plugin://plugin.video.youtube/playlist/PL57C1E76348A209F3/?page=1",35,art + 'documentary.jpg')

        addDir3('[COLOR aqua]  *Prehistoric Life  [/COLOR]',"plugin://plugin.video.youtube/playlist/PL152bjytsMC4ELQL-cyB4HcR5RR4y8jmI/?page=1",35,art + 'documentary.jpg')
        addDir3('[COLOR aqua]   *Religion   [/COLOR]',"plugin://plugin.video.youtube/playlist/PL152bjytsMC6pOots5SAORgX49LXO7Gfv/?page=1",35,art + 'documentary.jpg')
        addDir3('[COLOR aqua]  *Mysteries at the ...   [/COLOR]',"plugin://plugin.video.youtube/playlist/PL152bjytsMC5D2o3yzMATpE9_S2yP3vuB/?page=1",35,art + 'documentary.jpg')






def Documentarysport4y():
        addDir3('[COLOR aqua]The First 48[/COLOR]',"plugin://plugin.video.youtube/playlist/PLyicTY7J3bULdNAG8fCZOMTM_PeOsomR0/?page=1",35,art + 'documentary.jpg')

        addDir3('[COLOR aqua]A&E The First 48 (& After the First 48)Clips[/COLOR]',"plugin://plugin.video.youtube/playlist/PLcviVtB85dLxNwXqdrnKGSIAg8uL3JKuO/?page=1",35,art + 'documentary.jpg')

        addDir3('[COLOR aqua]48 Hours Mystery[/COLOR]',"plugin://plugin.video.youtube/playlist/PLyLrnNOEPdo430q3kcZmUHtbbPfv4vycg/?page=1",35,art + 'documentary.jpg')


        addDir3('[COLOR aqua]American Justice Cold Case Files[/COLOR]',"plugin://plugin.video.youtube/playlist/PLNlKG_zAzFm63zTKqzp2LqNZBazpjDCFM/?page=1",35,art + 'documentary.jpg')

        addDir3('[COLOR aqua]Uk True Crime Docs[/COLOR]',"plugin://plugin.video.youtube/playlist/PL4HLZHMq05jAiYLlIxWiwoXmEDBbIavBK/?page=1",35,art + 'documentary.jpg')

        addDir3('[COLOR aqua]Juiciest True Crime Shows[/COLOR]',"plugin://plugin.video.youtube/playlist/PL30kO8oVeDkpdNVGciv4YPyL1k4IXiEIF/?page=1",35,art + 'documentary.jpg')

        addDir3('[COLOR aqua]True Crime With Aphrodite Jones[/COLOR]',"plugin://plugin.video.youtube/playlist/PLdiXEhyBHpfWCGocPNSk5Mhtjsh41PsUS/?page=1",35,art + 'documentary.jpg')

        addDir3('[COLOR aqua]On The Case With Paula Zahn[/COLOR]',"plugin://plugin.video.youtube/playlist/PLy7mi56uNHSm1UtIlJB4vppyKf2SvNLIL/?page=1",35,art + 'documentary.jpg')

        addDir3('[COLOR aqua]Homicide Hunter[/COLOR]',"plugin://plugin.video.youtube/playlist/PLD75qpSXCKDDuxGAlwIKoWT08FbSImWLv/?page=1",35,art + 'documentary.jpg')

        addDir3('[COLOR aqua]Deadly Women[/COLOR]',"plugin://plugin.video.youtube/playlist/PLEi83IaZq0XWJ0tKfSQ1QnRRFm5Tn2Hfv/?page=1",35,art + 'documentary.jpg')

        addDir3('[COLOR aqua]Deadly Affairs[/COLOR]',"plugin://plugin.video.youtube/playlist/PLSNE-2y4IBXjJe8SFBK2xXhBwLesTKHk-/?page=1",35,art + 'documentary.jpg')

        addDir3('[COLOR aqua]Nightmare Next Door[/COLOR]',"plugin://plugin.video.youtube/playlist/PLaTIGMOvay0V4nP9DL_Pyrxwb3nTSO4nw/?page=1",35,art + 'documentary.jpg')

        addDir3('[COLOR aqua]Evil Kin[/COLOR]',"plugin://plugin.video.youtube/playlist/PLS7E6enfYOvwG7sGj6Ep8HGwIRJBCInBM/?page=1",35,art + 'documentary.jpg')

        addDir3('[COLOR aqua]Surviving Evil[/COLOR]',"plugin://plugin.video.youtube/playlist/PLosYISkcFffb18AY3Nqu4WisNPOofHeRr/?page=1",35,art + 'documentary.jpg')

        addDir3('[COLOR aqua]Who The Bleep Did I Marry[/COLOR]',"plugin://plugin.video.youtube/playlist/PLDrNp9S9i6UTr--BQeDzxKczdh7ri15GD/?page=1",35,art + 'documentary.jpg')

        addDir3('[COLOR aqua]Fatal Vows[/COLOR]',"plugin://plugin.video.youtube/playlist/PL1T-A-PVavLLc9-gnyzVmcnpqMUilPe5C/?page=1",35,art + 'documentary.jpg')

        addDir3('[COLOR aqua]Wives with Knives[/COLOR]',"plugin://plugin.video.youtube/playlist/PLPXjjzBAKhFOa5F-S9qAYWDc7SfQzWXm4/?page=1",35,art + 'documentary.jpg')

        addDir3('[COLOR aqua]Wicked Attraction[/COLOR]',"plugin://plugin.video.youtube/playlist/PL152bjytsMC4BOcSOdvFFuJZwWXam8FZF/?page=1",35,art + 'documentary.jpg')

        addDir3('[COLOR aqua]Cold Case Files[/COLOR]',"plugin://plugin.video.youtube/playlist/PLdegvhPRrKSuKuqI4IH7nWk-_SCAH9VyX/?page=1",35,art + 'documentary.jpg')

        addDir3('[COLOR aqua]Forensic Files (check playlists)[/COLOR]',"plugin://plugin.video.youtube/channel/UCPar4XXTkknIRtj-JSjiddw/?page=1",35,art + 'documentary.jpg')

        addDir3('[COLOR aqua]Solved[/COLOR]',"plugin://plugin.video.youtube/playlist/PL152bjytsMC5IEbzo4L3uddop8YvCyeXw/?page=1",35,art + 'documentary.jpg')

        addDir3('[COLOR aqua]Dr. G - Medical Examiner[/COLOR]',"plugin://plugin.video.youtube/playlist/PLuiMMfezGgfZ9R0gXNosCAB63YcZ4N1IG/?page=1",35,art + 'documentary.jpg')

        addDir3('[COLOR aqua]Sins and Secrets[/COLOR]',"plugin://plugin.video.youtube/playlist/PL6jkDCwMt49kGNtYI5ZiqexAuTaa7xdqP/?page=1",35,art + 'documentary.jpg')

        addDir3('[COLOR aqua]Behind Mansion Walls[/COLOR]',"plugin://plugin.video.youtube/playlist/PLUQCcRUCOfXbn5ushxnuWKRm8wZ2ZLtRA/?page=1",35,art + 'documentary.jpg')

        addDir3('[COLOR aqua]I Almost Got Away With It[/COLOR]',"plugin://plugin.video.youtube/playlist/PLMJCZB0MS5-N1ZvlfGRvEVCLjTWa4j_mI/?page=1",35,art + 'documentary.jpg')

        addDir3('[COLOR aqua]Americas Most Wanted[/COLOR]',"plugin://plugin.video.youtube/playlist/PLFp4v4wRLrbyYlimv-IU7MlOjHkWdWO1T/?page=1",35,art + 'documentary.jpg')

        addDir3('[COLOR aqua]FilmRise True Crime (check playlists)[/COLOR]',"plugin://plugin.video.youtube/channel/UCU4BHh9Dwfd7-I_xTZ5037Q/?page=1",35,art + 'documentary.jpg')

        addDir3('[COLOR aqua]Medical Detectives (check playlists)[/COLOR]',"plugin://plugin.video.youtube/channel/UCVBTlb6_rQkWY99ZKi2oBMw/?page=1",35,art + 'documentary.jpg')

        addDir3('[COLOR aqua]Sensing Murder[/COLOR]',"plugin://plugin.video.youtube/playlist/PL3E3xn5BmG284rjx3DWakZgXOM4RTj6nJ/?page=1",35,art + 'documentary.jpg')

        addDir3('[COLOR aqua]CRIME Inc. Crime shows[/COLOR]',"plugin://plugin.video.youtube/playlist/PL2OZWqbCOozITQXWNd2R4mrPq502d41v0/?page=1",35,art + 'documentary.jpg')

        addDir3('[COLOR aqua]Real Crime[/COLOR]',"plugin://plugin.video.youtube/playlist/PL152bjytsMC4oS3P5jAh8PrDLSaYHFV17/?page=1",35,art + 'documentary.jpg')

        addDir3('[COLOR aqua]True Crime[/COLOR]',"plugin://plugin.video.youtube/playlist/PL152bjytsMC7Zz0dZN6-x2xNscGts5bpi/?page=1",35,art + 'documentary.jpg')








def Documentarysport5y():





        addDir3('[COLOR aqua]CiNENET[/COLOR]',"plugin://plugin.video.youtube/channel/UCfjp6_4aAvhDGzvSkkAo0Jg/?page=1",35,art + 'movies.png')

        addDir3('[COLOR aqua]Manic Movies[/COLOR]',"plugin://plugin.video.youtube/channel/UCMMLfzsXe-EbRREJgMcb8cQ/?page=1",35,art + 'movies.png')

        addDir3('[COLOR aqua]Western Mania[/COLOR]',"plugin://plugin.video.youtube/channel/UCPUU5swJo5XLqvn77s6FB8g/?page=1",35,art + 'movies.png')

        addDir3('[COLOR aqua]Maverick Movies[/COLOR]',"plugin://plugin.video.youtube/channel/UC2u3R3pjOiPZu4LtTlKkxdw/?page=1",35,art + 'movies.png')


        addDir3('[COLOR aqua]Timeless Classic Movies[/COLOR]',"plugin://plugin.video.youtube/channel/UCOg0aMAXmF3o5m243PxhE5g/?page=1",35,art + 'movies.png')

        addDir3('[COLOR aqua]Timeless Classic Films (see playlists)[/COLOR]',"plugin://plugin.video.youtube/channel/UCWlLgwn2nfjnefINARfcquA/?page=1",35,art + 'movies.png')

        addDir3('[COLOR aqua]Timeless Western Movies[/COLOR]',"plugin://plugin.video.youtube/channel/UCh51cE9j1n206mAZslHtf6A/?page=1",35,art + 'movies.png')

        addDir3('[COLOR aqua]The Video Cellar (see playlists)[/COLOR]',"plugin://plugin.video.youtube/channel/UCBhskwCpv4Df8-xC8_wGxzA/?page=1",35,art + 'movies.png')

        addDir3('[COLOR aqua]Anton Pictures (check playlists)[/COLOR]',"plugin://plugin.video.youtube/channel/UCCq30E9PwvbpXaaM26Btw2g/?page=1",35,art + 'movies.png')

        addDir3('[COLOR aqua]Classic TV Movies[/COLOR]',"plugin://plugin.video.youtube/channel/UC-n2mADCBq--iuhwlroP4ig/?page=1",35,art + 'movies.png')

        addDir3('[COLOR aqua]Froggy Flix[/COLOR]',"plugin://plugin.video.youtube/channel/UCQf0IhUn2-S5-mEP3Mw-Kog/?page=1",35,art + 'movies.png')

        addDir3('[COLOR aqua]Movies (drelbcom)[/COLOR]',"plugin://plugin.video.youtube/channel/UCNLOeImyafrTNvHqdsBpGHQ/?page=1",35,art + 'movies.png')



        addDir3('[COLOR aqua]Classic Movies (one4allfour1)[/COLOR]',"plugin://plugin.video.youtube/channel/UCpqNeR8PGoU8zs86DAf2B0Q/?page=1",35,art + 'movies.png')

        addDir3('[COLOR aqua]Great Classic Movies[/COLOR]',"plugin://plugin.video.youtube/playlist/PLeagipoZmyfnIxkk9qKN-ewkuDeI-JP0i/?page=1",35,art + 'movies.png')

        addDir3('[COLOR aqua]World War Cinema[/COLOR]',"plugin://plugin.video.youtube/playlist/PLmHgXUJMN1TWyW6nJCPdj51WA-sMOozwD/?page=1",35,art + 'movies.png')





       







def PlayLists2y():
 
        addDir3('[COLOR aqua]Popular Music Videos[/COLOR]',"plugin://plugin.video.youtube/playlist/PLFgquLnL59alCl_2TQvOiD5Vgm1hCaGSI/?page=1",35,art + 'Music.png')
        addDir3('[COLOR aqua]New Music This Week[/COLOR]',"plugin://plugin.video.youtube/playlist/PLFgquLnL59alW3xmYiWRaoz0oM3H17Lth/?page=1",35,art + 'Music.png')
        addDir3('[COLOR aqua]Spotlight On: Leonard Cohen[/COLOR]',"plugin://plugin.video.youtube/playlist/PLFgquLnL59alFaD6qZtCpJgV2CB9L-Boq/?page=1",35,art + 'Music.png')
        addDir3('[COLOR aqua]Latest Music Videos[/COLOR]',"plugin://plugin.video.youtube/playlist/PLFgquLnL59akA2PflFpeQG9L01VFg90wS/?page=1",35,art + 'Music.png')
        addDir3('[COLOR aqua]Top Tracks - Electronic Music[/COLOR]',"plugin://plugin.video.youtube/playlist/PLFPg_IUxqnZNnACUGsfn50DySIOVSkiKI/?page=1",35,art + 'Music.png')
        addDir3('[COLOR aqua]Spotlight On: Visually Stunning[/COLOR]',"plugin://plugin.video.youtube/playlist/PLFgquLnL59ansZbAyA-OqSvImU8yo9j5I/?page=1",35,art + 'Music.png')
        addDir3('[COLOR aqua]Top Tracks - House Music[/COLOR]',"plugin://plugin.video.youtube/playlist/PLhInz4M-OzRUsuBj8wF6383E7zm2dJfqZ/?page=1",35,art + 'Music.png')
        addDir3('[COLOR aqua]Top Tracks - Latin Music [/COLOR]',"plugin://plugin.video.youtube/playlist/PLcfQmtiAG0X-fmM85dPlql5wfYbmFumzQ/?page=1",35,art + 'Music.png')
        addDir3('[COLOR aqua]The Electronic Index[/COLOR]',"plugin://plugin.video.youtube/playlist/PLFgquLnL59akXPIHrEZci0oouw4dArE0D/?page=1",35,art + 'Music.png')
        addDir3('[COLOR aqua]Top Tracks - House Music [/COLOR]',"plugin://plugin.video.youtube/playlist/PLhInz4M-OzRUsuBj8wF6383E7zm2dJfqZ/?page=1",35,art + 'Music.png')
        addDir3('[COLOR aqua]Spotlight On: October Recap[/COLOR]',"plugin://plugin.video.youtube/playlist/PLFgquLnL59amdobdR5OfC5OW3YoGtavfT/?page=1",35,art + 'Music.png')
        addDir3('[COLOR aqua]Spotlight On: Weekend Soundtrack[/COLOR]',"plugin://plugin.video.youtube/playlist/PLFgquLnL59akYTGd40gT26IYoL2kuhQZO/?page=1",35,art + 'Music.png')
        addDir3('[COLOR aqua]The Hip-Hop Index[/COLOR]',"plugin://plugin.video.youtube/playlist/PLFgquLnL59amBBTCULGWSotJu2CkioYkj/?page=1",35,art + 'Music.png')
        addDir3('[COLOR aqua]Top Tracks - Pop Music [/COLOR]',"plugin://plugin.video.youtube/playlist/PLDcnymzs18LWrKzHmzrGH1JzLBqrHi3xQ/?page=1",35,art + 'Music.png')
        addDir3('[COLOR aqua]Top Tracks - Hip Hop Music[/COLOR]',"plugin://plugin.video.youtube/playlist/PLH6pfBXQXHEC2uDmDy5oi3tHW6X8kZ2Jo/?page=1",35,art + 'Music.png')
        addDir3('[COLOR aqua]Top Tracks - Alternative Rock[/COLOR]',"plugin://plugin.video.youtube/playlist/PL47oRh0-pTouthHPv6AbALWPvPJHlKiF7/?page=1",35,art + 'Music.png')
        addDir3('[COLOR aqua]Top Tracks - Reggae[/COLOR]',"plugin://plugin.video.youtube/playlist/PLYAYp5OI4lRLf_oZapf5T5RUZeUcF9eRO/?page=1",35,art + 'Music.png')
        addDir3('[COLOR aqua]Top Tracks - Trap[/COLOR]',"plugin://plugin.video.youtube/playlist/PLL4IwRtlZcbvbCM7OmXGtzNoSR0IyVT02/?page=1",35,art + 'Music.png')
        addDir3('[COLOR aqua]Spotlight On: Global Discoveries [/COLOR]',"plugin://plugin.video.youtube/playlist/PLFgquLnL59an78ZI25rXfkTnpkrLFVXJ8/?page=1",35,art + 'Music.png')
        addDir3('[COLOR aqua]Top Tracks - Country[/COLOR]',"plugin://plugin.video.youtube/playlist/PLvLX2y1VZ-tFJCfRG7hi_OjIAyCriNUT2/?page=1",35,art + 'Music.png')
        addDir3('[COLOR aqua]The Country Index[/COLOR]',"plugin://plugin.video.youtube/playlist/PLFgquLnL59amI45Go39kM7ha2evwjOxzs/?page=1",35,art + 'Music.png')
        addDir3('[COLOR aqua]Top Tracks - Pop Rock[/COLOR]',"plugin://plugin.video.youtube/playlist/PLr8RdoI29cXIlkmTAQDgOuwBhDh3yJDBQ/?page=1",35,art + 'Music.png')
        addDir3('[COLOR aqua]Top Tracks - R&B[/COLOR]',"plugin://plugin.video.youtube/playlist/PLFRSDckdQc1th9sUu8hpV1pIbjjBgRmDw/?page=1",35,art + 'Music.png')
        addDir3('[COLOR aqua]Spotlight On: Dance Off[/COLOR]',"plugin://plugin.video.youtube/playlist/PLFgquLnL59am3gKxgT7Tvw-CMAlT4lQiC/?page=1",35,art + 'Music.png')
        addDir3('[COLOR aqua]Spotlight On: Surreal and Unreal[/COLOR]',"plugin://plugin.video.youtube/playlist/PLFgquLnL59akoZ1GetztyRuu1jtSwOvMi/?page=1",35,art + 'Music.png')
        addDir3('[COLOR aqua]Top Tracks - Asian Music[/COLOR]',"plugin://plugin.video.youtube/playlist/PL0zQrw6ZA60Z6JT4lFH-lAq5AfDnO2-aE/?page=1",35,art + 'Music.png')
        addDir3('[COLOR aqua]Top Tracks - Mexican Music[/COLOR]',"plugin://plugin.video.youtube/playlist/PLXupg6NyTvTxw5-_rzIsBgqJ2tysQFYt5/?page=1",35,art + 'Music.png')
        addDir3('[COLOR aqua]Top Tracks - Soul[/COLOR]',"plugin://plugin.video.youtube/playlist/PLQog_FHUHAFUDDQPOTeAWSHwzFV1Zz5PZ/?page=1",35,art + 'Music.png')
        addDir3('[COLOR aqua]The Indie Index[/COLOR]',"plugin://plugin.video.youtube/playlist/PLFgquLnL59amVPzpNpN5bNLcZCld7JfI8/?page=1",35,art + 'Music.png')
        addDir3('[COLOR aqua]On the Rise[/COLOR]',"plugin://plugin.video.youtube/playlist/PLFgquLnL59ak5gmnz28ZiMd59ryeTPXjT/?page=1",35,art + 'Music.png')
        addDir3('[COLOR aqua]Top Tracks - Rhythm & Blues[/COLOR]',"plugin://plugin.video.youtube/playlist/PLWNXn_iQ2yrKzFcUarHPdC4c_LPm-kjQy/?page=1",35,art + 'Music.png')
        addDir3('[COLOR aqua]Top Tracks - Christian Music[/COLOR]',"plugin://plugin.video.youtube/playlist/PLLMA7Sh3JsOQQFAtj1no-_keicrqjEZDm/?page=1",35,art + 'Music.png')
        addDir3('[COLOR aqua]Top Tracks - Hard Rock[/COLOR]',"plugin://plugin.video.youtube/playlist/PL9NMEBQcQqlzwlwLWRz5DMowimCk88FJk/?page=1",35,art + 'Music.png') 
        addDir3('[COLOR aqua]Top Tracks - Heavy Metal[/COLOR]',"plugin://plugin.video.youtube/playlist/PLfY-m4YMsF-OM1zG80pMguej_Ufm8t0VC/?page=1",35,art + 'Music.png')
        addDir3('[COLOR aqua]Top Tracks - Classical Music[/COLOR]',"plugin://plugin.video.youtube/playlist/PLVXq77mXV53-Np39jM456si2PeTrEm9Mj/?page=1",35,art + 'Music.png')

        addDir3('[COLOR aqua]Just-Released Music[/COLOR]',"plugin://plugin.video.youtube/playlist/PLrEnWoR732-D67iteOI6DPdJH1opjAuJt/?page=1",35,art + 'Music.png')
        addDir3('[COLOR aqua]Billboard Top Songs 2015[/COLOR]',"plugin://plugin.video.youtube/playlist/PL55713C70BA91BD6E/?page=1",35,art + 'Music.png')
        addDir3('[COLOR aqua]Popular Music[/COLOR]',"plugin://plugin.video.youtube/playlist/PLFgquLnL59alCl_2TQvOiD5Vgm1hCaGSI/?page=1",35,art + 'Music.png')
        addDir3('[COLOR aqua]80s & 90s Rock[/COLOR]',"plugin://plugin.video.youtube/playlist/PL3485902CC4FB6C67/?page=1",35,art + 'Music.png')
        addDir3('[COLOR aqua]Greatest Hits Of The 70s[/COLOR]',"plugin://plugin.video.youtube/playlist/PLGBuKfnErZlAkaUUy57-mR97f8SBgMNHh/?page=1",35,art + 'Music.png')
        addDir3('[COLOR aqua]60s Classic Hits[/COLOR]',"plugin://plugin.video.youtube/playlist/PLuK6flVU_Aj5EJ9Pp-C9N7XA0YJr_GrJI/?page=1",35,art + 'Music.png')
        addDir3('[COLOR aqua]50s Classic Hits[/COLOR]',"plugin://plugin.video.youtube/playlist/PLuK6flVU_Aj45QZ_A5ld0-pP3CIkoNQDk/?page=1",35,art + 'Music.png')
        addDir3('[COLOR aqua]Hottest Country Songs 2016[/COLOR]',"plugin://plugin.video.youtube/playlist/PLi7ihgkEws7RB7W89lEjK2qvItmbyLBLl/?page=1",35,art + 'Music.png')
        addDir3('[COLOR aqua]Country Music Mix[/COLOR]',"plugin://plugin.video.youtube/playlist/PLnpWcMv6bu2X0xfAD6Kt-MgIIFOCNb067/?page=1",35,art + 'Music.png')
        addDir3('[COLOR aqua]Hot Country Songs[/COLOR]',"plugin://plugin.video.youtube/playlist/PL2BN1Zd8U_MsyMeK8r9Vdv1lnQGtoJaSa/?page=1",35,art + 'Music.png')
        addDir3('[COLOR aqua]Country Radio Mix 2000 - 2014[/COLOR]',"plugin://plugin.video.youtube/playlist/PLh__qJ1ro4JgQI6aAgk5dduKLZUGr1Tiw/?page=1",35,art + 'Music.png')
        addDir3('[COLOR aqua]90s Country Music[/COLOR]',"plugin://plugin.video.youtube/playlist/PLCEE7B2A4B9C9BCE7/?page=1",35,art + 'Music.png')
        addDir3('[COLOR aqua]80s Country Music[/COLOR]',"plugin://plugin.video.youtube/playlist/PL04199B0AF6C7C9F8/?page=1",35,art + 'Music.png')







def PlayLkids1y():

        addDir3('[COLOR aqua]סמי הכבאי[/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=סמי הכבאי&search_type=playlist",35,art + 'kids.png')

        addDir3('[COLOR aqua]רינת ויויו[/COLOR]',"plugin://plugin.video.youtube/playlist/PLVisQUXwii8qa6lRDe1OmCIup6ylcprfc/?page=1",35,art + 'kids.png')

        addDir3('[COLOR aqua]פסטיגל[/COLOR]',"plugin://plugin.video.youtube/playlist/PLwimDnICcPKPL4MdOLIQrGDMTOAshuQ2l/?page=1",35,art + 'kids.png')

        addDir3('[COLOR aqua]מיקי[/COLOR]',"plugin://plugin.video.youtube/playlist/PLwimDnICcPKP4vFp6zklqeNUSdq08mN1H/?page=1",35,art + 'kids.png')

        addDir3('[COLOR aqua]מר עגבניה[/COLOR]',"plugin://plugin.video.youtube/playlist/PLwimDnICcPKMSeyub1DLM_2jG4aPjqI7n/?page=1",35,art + 'kids.png')

        addDir3('[COLOR aqua]לולי[/COLOR]',"plugin://plugin.video.youtube/playlist/PLwimDnICcPKNQy5TSz2s5XKWsE6kKV5C1/?page=1",35,art + 'kids.png')

        addDir3('[COLOR aqua]סופר סטרייקה[/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=סופר סטרייקה&search_type=playlist",35,art + 'kids.png')

        addDir3('[COLOR aqua]דורימון[/COLOR]',"plugin://plugin.video.youtube/playlist/PL95CWWe9DuaJ6xtv1V8ZxDvoG_cB3z4bc/?page=1",35,art + 'kids.png')

        addDir3('[COLOR aqua]שירי ילדים[/COLOR]',"plugin://plugin.video.youtube/playlist/PLFw7KwIWHNB03yaEG6T08Mg7haNKv673e/?page=1",35,art + 'kids.png')

        addDir3('[COLOR aqua]מיכל הקטנה[/COLOR]',"plugin://plugin.video.youtube/playlist/PLTNonj9ImqaKElCJ-4e8X_3BzXvzEYU_0/?page=1",35,art + 'kids.png')

        addDir3('[COLOR aqua]הדוד חיים[/COLOR]',"plugin://plugin.video.youtube/playlist/PLTNonj9ImqaIuFt2AyqdYFx6bCnKoFsIc/?page=1",35,art + 'kids.png')

        addDir3('[COLOR aqua]פים ופימבה[/COLOR]',"plugin://plugin.video.youtube/playlist/PLTNonj9ImqaI2F7DHlMxZ3VDn8gwpaTKe/?page=1",35,art + 'kids.png')

        addDir3('[COLOR aqua]קופיקו[/COLOR]',"plugin://plugin.video.youtube/playlist/PLQj4MAw08GNjVRSCvC8qbpjq0y6Zsfpho/?page=1",35,art + 'kids.png')

        addDir3('[COLOR aqua]הלו קיטי[/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=הלו קיטי&search_type=playlist",35,art + 'kids.png')

        addDir3('[COLOR aqua]שירים ישראלים לילדים ערוץ בייבי[/COLOR]',"plugin://plugin.video.youtube/playlist/PLErYJg2XgxyXTMAJvmFXoW6Qe66Ztw0Fk/?page=1",35,art + 'kids.png')

        addDir3('[COLOR aqua]אוצר מילים עם נוני[/COLOR]',"plugin://plugin.video.youtube/playlist/PLErYJg2XgxyXmgk6cyROtlJh2g-Fk_T6n/?page=1",35,art + 'kids.png')

        addDir3('[COLOR aqua]מתכוננים לשינה ערוץ בייבי[/COLOR]',"plugin://plugin.video.youtube/playlist/PLErYJg2XgxyVYzsbPxH2dzhlWLs9sWGTa/?page=1",35,art + 'kids.png')

        addDir3('[COLOR aqua]חיות בערוץ לולי[/COLOR]',"plugin://plugin.video.youtube/playlist/PLTleo-h9TFqI2CFuWeFA-Q2Bu3BBHdXqv/?page=1",35,art + 'kids.png')

        addDir3('[COLOR aqua]סיפורי התנכ עם סבא טוביה[/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=סיפורי התנך עם סבא טוביה&search_type=playlist",35,art + 'kids.png')

        addDir3('[COLOR aqua]סיפורים לילדים מרים רות[/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=סיפורים לילדים מרים רות&search_type=playlist",35,art + 'kids.png')

        addDir3('[COLOR aqua]בארץ הקטקטים[/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=בארץ הקטקטים&search_type=playlist",35,art + 'kids.png')

        addDir3('[COLOR aqua]משטרת האגדות[/COLOR]',"plugin://plugin.video.youtube/playlist/PLR7DTcU2p0QiaEmc56lGHMpxW4ladE93X/?page=1",35,art + 'kids.png')

        addDir3('[COLOR aqua]המעופפים הנועזים[/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=המעופפים הנועזים&search_type=playlist",35,art + 'kids.png')

        addDir3('[COLOR aqua]וולברין והאקס מן[/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=ילדים וולברין והאקס מן&search_type=playlist",35,art + 'kids.png')

        addDir3('[COLOR aqua]הצגות ומופעים[/COLOR]',"plugin://plugin.video.youtube/playlist/PLFw7KwIWHNB2xJnDoV8Us1tbWnFyvxkWO/?page=1",35,art + 'kids.png')

        addDir3('[COLOR aqua]הדרדסים[/COLOR]',"plugin://plugin.video.youtube/playlist/PLo3vmw8N0knb9tZuIy7AR9fMPTUzr1oiI/?page=1",35,art + 'kids.png')

        addDir3('[COLOR aqua]קטני[/COLOR]',"plugin://plugin.video.youtube/playlist/PLbHXbhgZi5cL97NlobjLHNtBwIA9VHcmw/?page=1",35,art + 'kids.png')

        addDir3('[COLOR aqua]שרגא בישגדא[/COLOR]',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj5KPYOntZkqg2Nwyqj2M1Lf/?page=1",35,art + 'kids.png')

        addDir3('[COLOR aqua]מיטב השירים פרפר נחמד[/COLOR]',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj45OPEXI-ibfJy8ON0k1ARh/?page=1",35,art + 'kids.png')

        addDir3('[COLOR aqua]קשת וענן[/COLOR]',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj6qcpdP7e44dNj7xHuwd3oo/?page=1",35,art + 'kids.png')

        addDir3('[COLOR aqua]בלי סודות[/COLOR]',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj5Alk2qONbzihcO1FVF1irZ/?page=1",35,art + 'kids.png')

        addDir3('[COLOR aqua]רגע עם דודלי[/COLOR]',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj5gUK-SIhbYyAMUQASzrZAw/?page=1",35,art + 'kids.png')

        addDir3('[COLOR aqua]חגי תשרי[/COLOR]',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj4LOZbA2VzFPUTkheKOlmaE/?page=1",35,art + 'kids.png')

        addDir3('[COLOR aqua]פיטר פן[/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=פיטר פן&search_type=playlist",35,art + 'kids.png')

        addDir3('[COLOR aqua]שאלתיאל קוואק[/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=שאלתיאל קוואק&search_type=playlist",35,art + 'kids.png')

        addDir3('[COLOR aqua]המומינים[/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=המומינים&search_type=playlist",35,art + 'kids.png')

        addDir3('[COLOR aqua]נאנוק[/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=נאנוק&search_type=playlist",35,art + 'kids.png')

        addDir3('[COLOR aqua]פינגווינים[/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=פינגווינים&search_type=playlist",35,art + 'kids.png')

        addDir3('[COLOR aqua]בוב הבנאי[/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=בוב הבנאי&search_type=playlist",35,art + 'kids.png')

        addDir3('[COLOR aqua]נילס הולגרסון[/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=נילס הולגרסון&search_type=playlist",35,art + 'kids.png')

        addDir3('[COLOR aqua]הלב מרקו[/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=הלב מרקו&search_type=playlist",35,art + 'kids.png')

        addDir3('[COLOR aqua]שלגיה ושבעת הגמדים[/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=שלגיה ושבעת הגמדים&search_type=playlist",35,art + 'kids.png')

        addDir3('[COLOR aqua]שלדון[/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=ילדים שלדון&search_type=playlist",35,art + 'kids.png')

        addDir3('[COLOR aqua]מולי וצומי[/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=מולי וצומי&search_type=playlist",35,art + 'kids.png')

        addDir3('[COLOR aqua]מרתה מדברת[/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=מרתה מדברת&search_type=playlist",35,art + 'kids.png')

        addDir3('[COLOR aqua]צארלי ולולה[/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=צארלי ולולה&search_type=playlist",35,art + 'kids.png')

        addDir3('[COLOR aqua]פרפר נחמד[/COLOR]',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj7XTzORdSrWpgCfF1x7ZUeK/?page=1",35,art + 'kids.png')

        addDir3('[COLOR aqua]הורים וגורים[/COLOR]',"plugin://plugin.video.youtube/playlist/PL51YAgTlfPj5sp5nUKFuwuUddCXYjiH8F/?page=1",35,art + 'kids.png')

        addDir3('[COLOR aqua]צור משלנו[/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=צור משלנו&search_type=playlist",35,art + 'kids.png')

        addDir3('[COLOR aqua]ילדים מספרים[/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=ילדים מספרים&search_type=playlist",35,art + 'kids.png')

        addDir3('[COLOR aqua]אבות ובנים[/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=אבות ובנים&search_type=playlist",35,art + 'kids.png')

        addDir3('[COLOR aqua]גלילאו[/COLOR]',"plugin://plugin.video.youtube/playlist/PLFw7KwIWHNB14v2w1rx_drmWtZPldqgtp/?page=1",35,art + 'kids.png')

        addDir3('[COLOR aqua]החפרנים[/COLOR]',"plugin://plugin.video.youtube/playlist/PLFw7KwIWHNB2JjD4-z7-2vZ3Ku6HtYc2U/?page=1",35,art + 'kids.png')

        addDir3('[COLOR aqua]נינגגו[/COLOR]',"plugin://plugin.video.youtube/playlist/PL92EMTBYUH-FoPVTqddFyLgv0-J8Kl6By/?page=1",35,art + 'kids.png')

        addDir3('[COLOR aqua]צימה[/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=צימה/?page=1",35,art + 'kids.png')

        addDir3('[COLOR aqua]מיקי מאוס[/COLOR]',"plugin://plugin.video.youtube/playlist/PLFw7KwIWHNB14Il3yEmYCImeXjUsuG_fR/?page=1",35,art + 'kids.png')

        addDir3('[COLOR aqua]מאסה ומישקה[/COLOR]',"plugin://plugin.video.youtube/playlist/PLBE_VtpC1cB8IsjeMynvNnmMxhrdYvn2E/?page=1",35,art + 'kids.png')

        addDir3('[COLOR aqua]אותיות מצחיקות[/COLOR]',"plugin://plugin.video.youtube/playlist/PL8yBWSFu2PVOlN83H6uWvmH4o1w5871Ws/?page=1",35,art + 'kids.png')

        addDir3('[COLOR aqua]גברת פלפלת[/COLOR]',"plugin://plugin.video.youtube/playlist/PL6BkF-3g8VpYUlrU-Agk3WUAONoOaI09E/?page=1",35,art + 'kids.png')

        addDir3('[COLOR aqua]מר קו[/COLOR]',"plugin://plugin.video.youtube/playlist/PL6BkF-3g8VpbfWb-7p-xPPzqPgkfgEQNK/?page=1",35,art + 'kids.png')

        addDir3('[COLOR aqua]הזרבובים[/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=הזרבובים&search_type=playlist",35,art + 'kids.png')

        addDir3('[COLOR aqua]דרגון בול זי[/COLOR]',"plugin://plugin.video.youtube/playlist/PL92EMTBYUH-HCp123_rEC-Oth1DdDaHNY/?page=1",35,art + 'kids.png')

        addDir3('[COLOR aqua]רוץ דייגו רוץ[/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=רוץ דייגו רוץ&search_type=playlist",35,art + 'kids.png')

        addDir3('[COLOR aqua]סיירי החלל[/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=סיירי החלל&search_type=playlist",35,art + 'kids.png')

        addDir3('[COLOR aqua]רובוט פולי[/COLOR]',"plugin://plugin.video.youtube/playlist/PLsa30wWsZ_kCPrW5BBiFxckb7IBxiOvvs/?page=1",35,art + 'kids.png')

        addDir3('[COLOR aqua]יובל המבולבל[/COLOR]',"plugin://plugin.video.youtube/playlist/PLzAqQoYm2t2xi_8LMKWYVfW0DjchcSzv0/?page=1",35,art + 'kids.png')

        addDir3('[COLOR aqua]זאק וקוואק[/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=זאק וקוואק&search_type=playlist",35,art + 'kids.png')

        addDir3('[COLOR aqua]חבורת החצר[/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=חבורת החצר&search_type=playlist",35,art + 'kids.png')

        addDir3('[COLOR aqua]בומבה[/COLOR]',"plugin://plugin.video.youtube/kodion/search/query/?q=ילדים בומבה&search_type=playlist",35,art + 'kids.png')

        addDir3('[COLOR aqua]ברני וחברים[/COLOR]',"plugin://plugin.video.youtube/playlist/PLFw7KwIWHNB3eIoqm8vLyYpVzxzOtHrK-/?page=1",35,art + 'kids.png')

        addDir3('[COLOR aqua]פלישת הרבידים[/COLOR]',"plugin://plugin.video.youtube/playlist/PLo69t7VQCjOHld0iP6VxBIfEdMWdeaSSu/?page=1",35,art + 'kids.png')

        addDir3('[COLOR aqua]לימוד אנגלית[/COLOR]',"plugin://plugin.video.youtube/playlist/PLqsYSvVJ2b7GhPj-_Xbx7okwcuO8nODHW&search_type=playlist",35,art + 'kids.png')



def PlayLkids2y():


        addDir('[COLOR aqua]דרך (יוטיוב) [/COLOR]','url',9876520020,'https://www.matnasgderot.com/uploads/c-480/1562763700.7671.png')








9999999





def YouTubeIsrael2():










        addDir3('[COLOR aqua] ערוץ ישראלי הרישמי [/COLOR]',"plugin://plugin.video.youtube/channel/UCrspcaIzKI3_RwDo_OyEtyg/playlists/?page=1",35,'https://yt3.ggpht.com/a/AATXAJwHom-ZsNmJGLXTS_LobC-xZ649Y0pkQS8Djg=s100-c-k-c0xffffffff-no-rj-mo')

        addDir3('[COLOR aqua]ערוץ הכיבוד [/COLOR]',"plugin://plugin.video.youtube/channel/UCxiMh-xcmHrCqxeUIIhIijw/playlists/?page=1",35,'https://yt3.ggpht.com/a/AATXAJxUu4bgo1E--c44Abk4S8Hh2lLXEut6CxAkcg=s176-c-k-c0x00ffffff-no-rj-mo')
        addDir3('[COLOR aqua]ערוץ טדי [/COLOR]',"plugin://plugin.video.youtube/channel/UC3hxGnVuGITDPQW6N6AuepA/playlists/?page=1",35,'https://yt3.ggpht.com/a/AATXAJwlZG_4SaMpP4U7N6utoIhn8Lqj6YnJPQKB_w=s176-c-k-c0x00ffffff-no-rj-mo')
        addDir3('[COLOR aqua]ערוץ הופ [/COLOR]',"plugin://plugin.video.youtube/user/hopchannel/",35,'https://yt3.ggpht.com/a/AATXAJzy8RAG8E3PlLPjnoa_fTUiD2k4PoGUv9Desg=s176-c-k-c0x00ffffff-no-rj-mo')
        addDir3('[COLOR aqua]ערוץ קידס [/COLOR]',"plugin://plugin.video.youtube/channel/UC_xBBPCq2pkEPEMCSy2zvkw/playlists/?page=1",35,'https://yt3.ggpht.com/a/AATXAJyUMg-Ziwc_V4bTC0NwF-la8oa31n4fuEIffw=s176-c-k-c0x00ffffff-no-rj-mo')

        addDir3('[COLOR aqua]ערוץ האוכל [/COLOR]',"plugin://plugin.video.youtube/channel/UCN3K5RheRJekWOeVBH_81VQ/playlists/?page=1",35,'https://yt3.ggpht.com/a/AATXAJwoZL_0Xp0KAQz4hvbKY03i5EB4GUrQDpCWaw=s176-c-k-c0x00ffffff-no-rj-mo')
        addDir3('[COLOR aqua]ערוץ כוכבי הילדים [/COLOR]',"plugin://plugin.video.youtube/channel/UCD-qkthtq-lkw3tZThJVeyw/playlists/?page=1",35,'https://yt3.ggpht.com/a/AATXAJwqCO6o62V5YrWzEpXl4PCDL0uJCkbFBwrX0g=s100-c-k-c0xffffffff-no-rj-mo')
        addDir3('[COLOR aqua]ערוץ כאן חדשות - תאגיד השידור [/COLOR]',"plugin://plugin.video.youtube/channel/UC_HwfTAcjBESKZRJq6BTCpg/playlists/?page=1",35,'https://yt3.ggpht.com/a/AATXAJyDk7TTLZYwtwMxP0P4DAgKeTf_Vpx7yT0_yA=s100-c-k-c0xffffffff-no-rj-mo')
        addDir3('[COLOR aqua]ערוץ 20 [/COLOR]',"plugin://plugin.video.youtube/channel/UCKEImtWikw9usC1pl_9m1nQ/playlists/?page=1",35,'https://yt3.ggpht.com/a/AATXAJz-cYE7oQ_fQQsdGozn0mHJlXfmceKZRaDF5g=s100-c-k-c0xffffffff-no-rj-mo')
        addDir3('[COLOR aqua]ערוץ 24 החדש  [/COLOR]',"plugin://plugin.video.youtube/channel/UCmeoV53dPXPQe0gKwtkd37A/playlists/?page=1",35,'https://yt3.ggpht.com/a/AATXAJzuL8nKwECjXiE5KUsyv1cpasoCUMlwu4tHZQ=s100-c-k-c0xffffffff-no-rj-mo')
        addDir3('[COLOR aqua]ערוץ חוק ומשפט [/COLOR]',"plugin://plugin.video.youtube/channel/UC2g9B52uuAIiDJy_eI2klow/playlists/?page=1",35,'https://yt3.ggpht.com/a/AATXAJxw0d_C2gL7M_50pTb3l0LT3EZHuB047Y3sqQ=s100-c-k-c0xffffffff-no-rj-mo')
        addDir3('[COLOR aqua]ערוץ החיים הטובים [/COLOR]',"plugin://plugin.video.youtube/channel/UCMwS6gVUo01idry02RWPAUg/playlists/?page=1",35,'https://yt3.ggpht.com/a/AATXAJxk0V39fMmMNcfGyN8vd1PwyP5JTadZ2I78qQ=s100-c-k-c0xffffffff-no-rj-mo')
        addDir3('[COLOR aqua]ערוץ הטיולים [/COLOR]',"plugin://plugin.video.youtube/channel/UCydYLwPtXqWssYw1-EZoitA/playlists/?page=1",35,'https://yt3.ggpht.com/a/AATXAJyH-opDAXktUbsKfcdDtrkG3pYnOZWOdCOmnA=s48-c-k-c0xffffffff-no-rj-mo')
        addDir3('[COLOR aqua]ערוץ הבריאות [/COLOR]',"plugin://plugin.video.youtube/channel/UCkM4IEaxdETbRls34uPrLIw/playlists/?page=1",35,'https://yt3.ggpht.com/a/AATXAJxMouf3Bf1Y-Hq8H_0uz2gNXbW4oHZyJ7Lb1w=s48-c-k-c0xffffffff-no-rj-mo')
        addDir3('[COLOR aqua]ערוץ כאן רדיו [/COLOR]',"plugin://plugin.video.youtube/channel/UCzr8GKryb0dfc8Y_Sb5B33w/playlists/?page=1",35,'https://yt3.ggpht.com/a/AATXAJxAIKUN-8e7cYwRSp1vVNm3-VDONgBiE-HFdw=s48-c-k-c0xffffffff-no-rj-mo')
        addDir3('[COLOR aqua]ערוץ כאן ארכיון [/COLOR]',"plugin://plugin.video.youtube/channel/UCNeddAJjp9vxE4gcuQlc4WA/playlists/?page=1",35,'https://yt3.ggpht.com/a/AATXAJzxRZ4IptJtzo3UaRzy7LZzwVEkmLDD2y7yrA=s48-c-k-c0xffffffff-no-rj-mo')
        addDir3('[COLOR aqua]ערוץ אי אקס פי [/COLOR]',"plugin://plugin.video.youtube/channel/UCuSfLQNRToAP3hTncar6zqg/playlists/?page=1",35,'https://yt3.ggpht.com/a/AATXAJy68Pk2aUjHr2FEru4fKJwN2p7E81FX94wivA=s100-c-k-c0xffffffff-no-rj-mo')

        addDir3('[COLOR aqua]ערוץ טין ניק [/COLOR]',"plugin://plugin.video.youtube/channel/UCcgf7Bokf_WzQLFDwaBEmSw/playlists/?page=1",35,'https://yt3.ggpht.com/a/AATXAJwUK9l8NiNLRO7GP1h7qodjCDX3PUoDBbZxcA=s100-c-k-c0xffffffff-no-rj-mo')
        addDir3('[COLOR aqua]ערוץ MTV ישראל [/COLOR]',"plugin://plugin.video.youtube/channel/UCJ1AEGt3yFeBBe-fUb0B2vw/playlists/?page=1",35,'https://yt3.ggpht.com/a/AATXAJxNibBU-h8cFdbczgOaANKpK7ePuTUF6iL3mg=s48-c-k-c0xffffffff-no-rj-mo')
        addDir3('[COLOR aqua]ערוץ אחשלירוח [/COLOR]',"plugin://plugin.video.youtube/channel/UC_16iKfb-m8Vel5KPwZsiMw/playlists/?page=1",35,'https://yt3.ggpht.com/a/AATXAJya9yXot_L7inabhuRjgiW2yiMqoFygZAJINA=s100-c-k-c0xffffffff-no-rj-mo')
        addDir3('[COLOR aqua]ערוץ דנה בננה [/COLOR]',"plugin://plugin.video.youtube/channel/UCoyblSpowujYQCK7X4XCErA/playlists/?page=1",35,'https://yt3.ggpht.com/a/AATXAJyBgVc40Vp6OaQ0OHwb09gJy8gM01w9PaSYZQ=s48-c-k-c0xffffffff-no-rj-mo')
        addDir3('[COLOR aqua]ערוץ לירון איש האווירון [/COLOR]',"plugin://plugin.video.youtube/channel/UCHLWMxo-FdAZzA7t-k2_Ulw/playlists/?page=1",35,'https://yt3.ggpht.com/a/AATXAJw42iNCWRovFIOkQjxERsLOU3HFemP3_Gf-=s48-c-k-c0xffffffff-no-rj-mo')
        addDir3('[COLOR aqua]ערוץ קוגומולו [/COLOR]',"plugin://plugin.video.youtube/channel/UC_gXE5AFgQdKSySDEJP4rkA/playlists/?page=1",35,'https://yt3.ggpht.com/a/AATXAJyWmLQfF2_ABccNdnd5ytLJIESYoRd9z6uFXQ=s48-c-k-c0xffffffff-no-rj-mo')
        addDir3('[COLOR aqua]ערוץ אלי אליהו [/COLOR]',"plugin://plugin.video.youtube/channel/UCBHTyzSMKFW0wzG9k0SeQlw/playlists/?page=1",35,'https://yt3.ggpht.com/a/AATXAJwxa_aHP-DoSn_jsY3rGUuiNsOPXUel7uGadw=s100-c-k-c0xffffffff-no-rj-mo')
        addDir3('[COLOR aqua]ערוץ הפיוט [/COLOR]',"plugin://plugin.video.youtube/channel/UCarit_RqfzzejFzVt3mQqSw/playlists/?page=1",35,'https://yt3.ggpht.com/a/AATXAJyIdYf_m917IKlJUrdb0IjzF2I1hLypa2FANw=s100-c-k-c0xffffffff-no-rj-mo')
        addDir3('[COLOR aqua]ערוץ פורמולה [/COLOR]',"plugin://plugin.video.youtube/channel/UCtMuJrQ1cbRneXtdfDYV3jg/playlists/?page=1",35,'https://yt3.ggpht.com/a/AATXAJwG069xBKQ2-0WjJZcvnONCt0jzIhY1f-fyLQ=s100-c-k-c0xffffffff-no-rj-mo')
        addDir3('[COLOR aqua]ערוץ כאן דיגיטל [/COLOR]',"plugin://plugin.video.youtube/channel/UCDJ6HHS5wkNaSREumdJRYhg/playlists/?page=1",35,'https://yt3.ggpht.com/a/AATXAJzolG9PEaG_xZG-Haq53WmLqC_Esq6t9E6LJw=s100-c-k-c0xffffffff-no-rj-mo')
        addDir3('[COLOR aqua]ערוץ מטבח בקלי קלות [/COLOR]',"plugin://plugin.video.youtube/channel/UCYRjRbFiLOyKr89dryIDobw/playlists/?page=1",35,'https://yt3.ggpht.com/a/AATXAJxMqM3IFjYeffkQfdQVOi8I5hdntsAbblvpsQ=s100-c-k-c0xffffffff-no-rj-mo')
        addDir3('[COLOR aqua]ערוץ ynet [/COLOR]',"plugin://plugin.video.youtube/channel/UCpSSzrovhI4fA2PQNItecUA/playlists/?page=1",35,'https://yt3.ggpht.com/a/AATXAJymFNk9f7wUNm0sPPNcaC2scRkBF_AndBT_oA=s100-c-k-c0xffffffff-no-rj-mo')








        addDir3('[COLOR aqua]ערוץ גוניור [/COLOR]',"plugin://plugin.video.youtube/user/ZbangChannel/playlists/",35,'https://yt3.ggpht.com/a/AATXAJywiBNXq2jHMk3rhq_pXw-7XM7Czm7CwCDF9Q=s48-c-k-c0xffffffff-no-rj-mo')
        addDir3('[COLOR aqua]ONE ערוץ [/COLOR]',"plugin://plugin.video.youtube/user/one/",35,'https://yt3.ggpht.com/a/AATXAJxfxohB018RCKob9XTfBLydtqU3XRTW33KDtg=s176-c-k-c0x00ffffff-no-rj-mo')
        addDir3('[COLOR aqua]ערוץ זום [/COLOR]',"plugin://plugin.video.youtube/user/ZOOMTVISRAEL/",35,'https://yt3.ggpht.com/a/AATXAJwW-5XjzKKtZ0VHinO82MJpyPGJIgwwoB2Bpw=s176-c-k-c0x00ffffff-no-rj-mo')
        addDir3('[COLOR aqua]ערוץ לולי [/COLOR]',"plugin://plugin.video.youtube/user/lulitv1/",35,'https://yt3.ggpht.com/a/AATXAJxw8ovKkpFWmy94KqKk8W5fjiBc3RUVl3Xl6g=s176-c-k-c0x00ffffff-no-rj-mo')
        addDir3('[COLOR aqua]ערוץ קופיקו [/COLOR]',"plugin://plugin.video.youtube/user/KofikoChannel/",35,'https://yt3.ggpht.com/a/AATXAJwjN6WiYmkryJNOiOR0D7046gFkVGE6Fxag2g=s100-c-k-c0xffffffff-no-rj-mo')
        addDir3('[COLOR aqua]ערוץ הבידור [/COLOR]',"plugin://plugin.video.youtube/user/HotBidurOnline/",35,'https://yt3.ggpht.com/a/AATXAJyrD6_VNQ8iORe4UG7goH8lPLPWORTejtTmQg=s100-c-k-c0xffffffff-no-rj-mo')
        addDir3('[COLOR aqua]ערוץ ישראל E!  [/COLOR]',"plugin://plugin.video.youtube/user/EonlineIsraelCh/",35,'https://yt3.ggpht.com/a/AATXAJyfriiXQh9spjnhEh-MLDN2cPbjF2JM3TZ1hg=s100-c-k-c0xffffffff-no-rj-mo')
        addDir3('[COLOR aqua]ערוץ כנסת [/COLOR]',"plugin://plugin.video.youtube/user/99knesset/",35,'https://yt3.ggpht.com/a/AATXAJzQHrqv0fWAfcBieUEVT6GIwYu9nShSF0gl2Q=s100-c-k-c0xffffffff-no-rj-mo')
        addDir3('[COLOR aqua]ערוץ 2000 [/COLOR]',"plugin://plugin.video.youtube/user/radio2000Judaism/",35,'https://yt3.ggpht.com/a/AATXAJx1EscZPcWgE7Y6whFlTbEot_YzIoCDBeJhxg=s100-c-k-c0xffffffff-no-rj-mo')
        addDir3('[COLOR aqua]ערוץ ניקלודיאון [/COLOR]',"plugin://plugin.video.youtube/user/nickelodeonIsrael/",35,'https://yt3.ggpht.com/a/AATXAJxYGoieIVzw8kg4xaxoi1GJo1rfB74rAvxz8g=s100-c-k-c0xffffffff-no-rj-mo')
        addDir3('[COLOR aqua]ערוץ פסטיגל [/COLOR]',"plugin://plugin.video.youtube/user/myfestigal/",35,'https://yt3.ggpht.com/a/AATXAJxqnnKOgFWp6BHUX6d0jjdoKKW9buonF_vjdQ=s100-c-k-c0xffffffff-no-rj-mo')
        addDir3('[COLOR aqua]ערוץ כאן חינוכית [/COLOR]',"plugin://plugin.video.youtube/user/23tv/",35,'https://yt3.ggpht.com/a/AATXAJyllp5vvQ8el7FkQ1nUPbMB4_x8m99rnm50Zw=s100-c-k-c0xffffffff-no-rj-mo')
        addDir3('[COLOR aqua]ערוץ כאן לומדים [/COLOR]',"plugin://plugin.video.youtube/user/23bagrut/",35,'https://yt3.ggpht.com/a/AATXAJyXKHzScru98Pvf628ouH8RCsDroDeknt6Ntw=s48-c-k-c0xffffffff-no-rj-mo')
        addDir3('[COLOR aqua]ערוץ כאן שפות [/COLOR]',"plugin://plugin.video.youtube/user/23language/",35,'https://yt3.ggpht.com/a/AATXAJzxI3yY7NHlme2zWHdE_-kqIyEnNuIohGTHAQ=s48-c-k-c0xffffffff-no-rj-mo')
        addDir3('[COLOR aqua]ערוץ הידברות(HD) [/COLOR]',"plugin://plugin.video.youtube/user/hidabrooTeem/",35,'https://yt3.ggpht.com/a/AATXAJx2TVmEWRd5G8rOE3cim0yS6i1UKQsm3oOK6w=s100-c-k-c0xffffffff-no-rj-mo')
        addDir3('[COLOR aqua]ערוץ הידברות [/COLOR]',"plugin://plugin.video.youtube/user/Hidabroot1/",35,'https://yt3.ggpht.com/a/AATXAJx2TVmEWRd5G8rOE3cim0yS6i1UKQsm3oOK6w=s100-c-k-c0xffffffff-no-rj-mo')
        addDir3('[COLOR aqua]ערוץ בייבי [/COLOR]',"plugin://plugin.video.youtube/user/BabyChannelIsrael/",35,'https://yt3.ggpht.com/a/AATXAJwHy9XkIQY8jGlr9p1GKXWk7nEfo-IpUaWPoQ=s100-c-k-c0xffffffff-no-rj-mo')
        addDir3('[COLOR aqua]ערוץ דיסני [/COLOR]',"plugin://plugin.video.youtube/user/DisneyChannelIS/",35,'https://yt3.ggpht.com/a/AATXAJz7Sggyta0L5om55NJkqF8k4_xQ6DLW3Y65RA=s100-c-k-c0xffffffff-no-rj-mo')
        addDir3('[COLOR aqua]ערוץ דיסני גוניור [/COLOR]',"plugin://plugin.video.youtube/user/disneyjuniorisrael/",35,'https://yt3.ggpht.com/a/AATXAJxzgrEsvWKP9pYVyU-hQcxfqcHsLxi3bL6QQw=s48-c-k-c0xffffffff-no-rj-mo')
        addDir3('[COLOR aqua]ערוץ דיסני ישראל [/COLOR]',"plugin://plugin.video.youtube/user/WaltDisneyIL/",35,'https://yt3.ggpht.com/a/AATXAJyM_lT0s5swX6PoRb5fp_38hwsTltx0XxAEfQ=s48-c-k-c0xffffffff-no-rj-mo')
        addDir3('[COLOR aqua]ערוץ גלגלצ [/COLOR]',"plugin://plugin.video.youtube/user/glgltzchannel/",35,'https://yt3.ggpht.com/a/AATXAJwD4GBoJpVS5A9xc6AkqzYkveq4e4cObtxH9Q=s100-c-k-c0xffffffff-no-rj-mo')
        addDir3('[COLOR aqua]ערוץ גלץ רדיו [/COLOR]',"plugin://plugin.video.youtube/user/GLZradio/",35,'https://yt3.ggpht.com/a/AATXAJzhAP-NAj6YfYty4pWn3H0j0nQ2FqdlINDJ_A=s48-c-k-c0xffffffff-no-rj-mo')
        addDir3('[COLOR aqua]ערוץ כאן 11 [/COLOR]',"plugin://plugin.video.youtube/user/MEDIAIBA/",35,'https://yt3.ggpht.com/a/AATXAJy0f5OnDznhjmR4wlPu5YzKsTEcnd8P_SBr0w=s100-c-k-c0xffffffff-no-rj-mo')
        addDir3('[COLOR aqua]ערוץ מיכל הקטנה [/COLOR]',"plugin://plugin.video.youtube/user/rotmana/",35,'https://yt3.ggpht.com/a/AATXAJzda-DhOhNxgV0CLE-vDFHvpp3fUT4zcNe-4w=s100-c-k-c0xffffffff-no-rj-mo')
        addDir3('[COLOR aqua]ערוץ דוד חיים [/COLOR]',"plugin://plugin.video.youtube/user/dodhaim/",35,'https://yt3.ggpht.com/a/AATXAJxRyMEKaw6VSgAy_028hHSgwT86VOnv1T-zLA=s48-c-k-c0xffffffff-no-rj-mo')
        addDir3('[COLOR aqua]ערוץ יובל המבולבל [/COLOR]',"plugin://plugin.video.youtube/user/7yuval/",35,'https://yt3.ggpht.com/a/AATXAJz7XiGOamgxBTyQefNZyCyQo-04uqHRbYWK1A=s48-c-k-c0xffffffff-no-rj-mo')
        addDir3('[COLOR aqua]ערוץ הפרויקט של רביבו [/COLOR]',"plugin://plugin.video.youtube/user/TheRevivoProject/",35,'https://yt3.ggpht.com/a/AATXAJw-ud4C4l7Zy5jvT1fZLvspKnyZ2fbFvKHQPA=s100-c-k-c0xffffffff-no-rj-mo')
        addDir3('[COLOR aqua]ערוץ פיקוד העורף [/COLOR]',"plugin://plugin.video.youtube/user/pakar2008/",35,'https://yt3.ggpht.com/a/AATXAJwzbsR1WG9WTMFI2exDqHzwErNWCpmRMkD1Dg=s100-c-k-c0xffffffff-no-rj-mo')
































def vodil(url):

    ok=True        
    xbmc.executebuiltin('XBMC.Container.Update(%s)' % url )
    return ok
        
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param


params=get_params()
url=None
name=None
mode=None
iconimage=None
page = None
token = None

try: url=urllib.unquote_plus(params["url"])
except: pass
try: name=urllib.unquote_plus(params["name"])
except: pass
try: mode=int(params["mode"])
except:
	try: 
		mode=params["mode"]
	except: pass
try: iconimage=urllib.unquote_plus(params["iconimage"])
except: pass
try: token=urllib.unquote_plus(params["token"])
except: pass
try: page=int(params["page"])
except: page = 1

print ("Mode: "+str(mode))
print ("URL: "+str(url))
print ("Name: "+str(name))
print ("iconimage: "+str(iconimage))
print ("Page: "+str(page))
print ("Token: "+str(token))

		
def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setProperty('fanart_image', fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
		
def addDir3(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setProperty('fanart_image', fanart)
        if mode==35 :
               ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)
               return ok
				
def create_directory(dir_path, dir_name=None):
    if dir_name:
        dir_path = os.path.join(dir_path, dir_name)
    dir_path = dir_path.strip()
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    return dir_path

if mode==None or url==None or len(url)<1:
        print ""
        CATEGORIES()
       
elif mode==1:
        return_youtubevideos(name,url,token,page)

elif mode==5: 
        play_youtube_video(url)

elif mode==6:
        mark_as_watched(url)

elif mode==7:
        removed_watched(url)

elif mode==8:
        add_to_bookmarks(url)

elif mode==9:
        remove_from_bookmarks(url)
		
elif mode==10:
        print ""+url
        lifestyle()
		
elif mode==11:
        print ""+url
        documentary()

elif mode==12:
        print ""+url
        kids()

elif mode==13:
        print ""+url
        Music()
        
elif mode==14:
        print ""+url
        travel()

elif mode==15:
        print ""+url
        Sports()

elif mode==16:
        print ""+url
        liveshows()

elif mode==17:
        print ""+url
        cooking()
			
elif mode==18:
        print ""+url
        junior()
		
elif mode==19:
        print ""+url
        nickjunior()

elif mode==20:
        print ""+url
        nicklodeon()

elif mode==21:
        print ""+url
        logy()

elif mode==22:
        print ""+url
        hop()

elif mode==23:
        print ""+url
        hopy()	

elif mode==24:
        print ""+url
        luly()

elif mode==25:
        print ""+url
        baby()

elif mode==26:
        print ""+url
        hot()

elif mode==27:
        print ""+url
        kidstv()

elif mode==28:
        print ""+url
        ch23()

elif mode==29:
        print ""+url
        zoom()		

elif mode==30:
        print ""+url
        dsjunior()

elif mode==31:
        print ""+url
        NBA()

elif mode==32:
        print ""+url
        basket()

elif mode==33:
        print ""+url
        soccer()		

elif mode==34:
        print ""+url
        box()		

elif mode==37:
        print ""+url
        nostal()				
		
elif mode==35:
	    vodil(url)
	
elif mode==38:
        print ""+url
        movies()


elif mode==99:
        print ""+url
        Mu()

elif mode==98:
        print ""+url
        Su()

elif mode==97:
        print ""+url
        Sl()

elif mode==96:
        print ""+url
        Sx()

elif mode==95:
        print ""+url
        Dg()

elif mode==94:
        print ""+url
        vevo()

elif mode==193:
        print ""+url
        vev()

elif mode==92:
        print ""+url
        Muyu()

elif mode==199:
        print ""+url
        Mul()

elif mode==197:
        print ""+url
        Sll()

elif mode==196:
        print ""+url
        Sxl()

elif mode==195:
        print ""+url
        Dgl()

elif mode==194:
        print ""+url
        Dgll()

elif mode==1941948080:
        print ""+url
        sdarottv()

elif mode==1931:
        print ""+url
        Dglll()

elif mode==1930:
        print ""+url
        Dgllll()

elif mode==1929:
        print ""+url
        Dglllll()

elif mode==192919291009:
        print ""+url
        Bildglllll()

elif mode==1929192910091:
        print ""+url
        Bildglllll1()

elif mode==1929192910092:
        print ""+url
        Bildglllll2()

elif mode==1929192910093:
        print ""+url
        Bildglllll3()

elif mode==1929192910094:
        print ""+url
        Bildglllll4()

elif mode==1929192910095:
        print ""+url
        Bildglllll5()

elif mode==1929192910096:
        print ""+url
        Bildglllll6()

elif mode==19291929177701:
        print ""+url
        Bthecrew1()

elif mode==19291929177702:
        print ""+url
        Bmando2()

elif mode==19291929177703:
        print ""+url
        Bmovixws3()

elif mode==19291929177704:
        print ""+url
        Btelemedia4()

elif mode==19291929177705:
        print ""+url
        BServiceil5()

elif mode==19291929177706:
        print ""+url
        BCHICCO6()

elif mode==19291929177707:
        print ""+url
        BFlash7()

elif mode==192919291777011:
        print ""+url
        Cidanplus1()

elif mode==192919291777012:
        print ""+url
        Csdarottv2()


elif mode==192919291777013:
        print ""+url
        Cthecrew3()

elif mode==192919291777014:
        print ""+url
        Cmando4()



elif mode==192919291777016:
        print ""+url
        Ctelemedia6()



elif mode==192919291777017:
        print ""+url
        CCHICCO7()

elif mode==192919291777018:
        print ""+url
        CFlash8()


elif mode==292919291777011:
        print ""+url
        Didanplus1()

elif mode==292919291777012:
        print ""+url
        Dsdarottv2()


elif mode==292919291777013:
        print ""+url
        Dthecrew3()

elif mode==292919291777014:
        print ""+url
        Dmando4()



elif mode==292919291777015:
        print ""+url
        Dtelemedia5()



elif mode==292919291777016:
        print ""+url
        DCHICCO6()

elif mode==292919291777017:
        print ""+url
        DFlash7()

elif mode==392919291777017:
        print ""+url
        Eidanplus1()

elif mode==392919291777018:
        print ""+url
        EServiceil2()

elif mode==392919291777019:
        print ""+url
        Ethecrew3()


elif mode==492919291777011:
        print ""+url
        FYoutubeMusic1()

elif mode==492919291777012:
        print ""+url
        FServiceil2()

elif mode==492919291777013:
        print ""+url
        Fidanplus3()

elif mode==592919291777011:
        print ""+url
        GSportHD1()

elif mode==592919291777012:
        print ""+url
        Gthecrew2()

elif mode==592919291777013:
        print ""+url
        GServiceil3()

elif mode==592919291777014:
        print ""+url
        Gidanplus4()





elif mode==1928:
        print ""+url
        Dgllllll()

elif mode==1927:
        print ""+url
        Dglllllll()

elif mode==2000:
        print ""+url
        rockcollection()

elif mode==2001:
        print ""+url
        topinmusic()

elif mode==2002:
        print ""+url
        topinmusic2()

elif mode==2003:
        print ""+url
        topinmusic3()

elif mode==1925:
        print ""+url
        kttgt()

elif mode==2100:
        print ""+url
        rockcollectionl()

elif mode==2101:
        print ""+url
        topinmusicl()

elif mode==2102:
        print ""+url
        topinmusic2l()

elif mode==2103:
        print ""+url
        topinmusic3l()

elif mode==5930:
        print ""+url
        Daa()

elif mode==5940:
        print ""+url
        Daaa()
		

elif mode==7899:
        print ""+url
        THEATER()

elif mode==5931:
        print ""+url
        THEATERB()

elif mode==5932:
        print ""+url
        THEATERB2()

elif mode==5933:
        print ""+url
        THEATERB2a()

elif mode==5934:
        print ""+url
        THEATERB2b()

elif mode==5935:
        print ""+url
        THEATERB3a()

elif mode==5936:
        print ""+url
        THEATERB3b()

elif mode==5937:
        print ""+url
        KungFu1()

elif mode==5938:
        print ""+url
        KungFu2()

elif mode==9009:
        print ""+url
        zozozo()

elif mode==9010:
        print ""+url
        zomba()

elif mode==9011:
        print ""+url
        pilates()

elif mode==9012:
        print ""+url
        aerobic()

elif mode==9013:
        print ""+url
        yoga()

elif mode==9014:
        print ""+url
        makeup()

elif mode==9015:
        print ""+url
        nutrition()

elif mode==9016:
        print ""+url
        health()

elif mode==9017:
        print ""+url
        sports()

elif mode==9018:
        print ""+url
        bidor()

elif mode==10000:
        print ""+url
        dat()

elif mode==10001:
        print ""+url
        dat1()

elif mode==10002:
        print ""+url
        dok1()

elif mode==10003:
        print ""+url
        dok2()

elif mode==10004:
        print ""+url
        dok3()

elif mode==10005:
        print ""+url
        trlrsrt()

elif mode==10006:
        print ""+url
        POLARIS()

elif mode==10007:
        print ""+url
        POLARIS1()

elif mode==10008:
        print ""+url
        POLARIS2()

elif mode==10009:
        print ""+url
        SPORTEXTREME()

elif mode==10010:
        print ""+url
        SPORTEXTREME1()

elif mode==10011:
        print ""+url
        SPORTEXTREME2()

elif mode==10012:
        print ""+url
        binaural()


elif mode==20000:
        print ""+url
        nostalgia()
        

elif mode==20001:
        print ""+url
        nostalgia1()

elif mode==20002:
        print ""+url
        kids99()

elif mode==20003:
        print ""+url
        Broadcast99()
        	
elif mode==20004:
        print ""+url
        lomdim99()
	
elif mode==20005:
        print ""+url
        special99()	

elif mode==20006:
        print ""+url
        music99()

elif mode==20007:
        print ""+url
        kidsnew99()

elif mode==20008:
        print ""+url
        LILI1()


elif mode==20009:
        print ""+url
        Documentarysport()

elif mode==20010:
        print ""+url
        Documentarysport1()

elif mode==20011:
        print ""+url
        Documentarysport2()

elif mode==20012:
        print ""+url
        Documentarysport3()

elif mode==20013:
        print ""+url
        Documentarysport4()

elif mode==20014:
        print ""+url
        Documentarysport5()

elif mode==20015:
        print ""+url
        shadow()

elif mode==7777777:
        print ""+url
        srbc()

elif mode==7777776:
        print ""+url
        srbc2()

elif mode==20016:
        print ""+url
        ezmaintenanceplus()

elif mode==20017:
        print ""+url
        PlayLists1()

elif mode==20018:
        print ""+url
        PlayLists2()



elif mode==20020:
        print ""+url
        PlayLkids1()

elif mode==20021:
        print ""+url
        PlayLkids2()













elif mode==9876510:
        print ""+url
        lifestyley()
		
elif mode==9876511:
        print ""+url
        documentaryy()

elif mode==9876512:
        print ""+url
        kidsy()

elif mode==9876513:
        print ""+url
        Musicy()
        
elif mode==9876514:
        print ""+url
        travely()

elif mode==9876515:
        print ""+url
        Sportsy()

elif mode==9876516:
        print ""+url
        liveshowsy()

elif mode==9876517:
        print ""+url
        cookingy()
			


elif mode==9876528:
        print ""+url
        ch23y()





elif mode==9876531:
        print ""+url
        NBAy()

elif mode==9876532:
        print ""+url
        baskety()

elif mode==9876533:
        print ""+url
        soccery()		

elif mode==9876534:
        print ""+url
        boxy()		

				
		
elif mode==9876535:
	    vodil(url)
	
elif mode==9876538:
        print ""+url
        moviesy()


elif mode==9876599:
        print ""+url
        Muy()

elif mode==9876598:
        print ""+url
        Suy()

elif mode==9876597:
        print ""+url
        Sly()

elif mode==9876596:
        print ""+url
        Sxy()

elif mode==9876595:
        print ""+url
        Dgy()

elif mode==9876594:
        print ""+url
        vevoy()

elif mode==98765193:
        print ""+url
        vevy()

elif mode==9876592:
        print ""+url
        Muyuy()



elif mode==98765199:
        print ""+url
        Muly()

elif mode==98765197:
        print ""+url
        Slly()

elif mode==98765196:
        print ""+url
        Sxly()

elif mode==98765195:
        print ""+url
        Dgly()

elif mode==98765194:
        print ""+url
        Dglly()

elif mode==987651931:
        print ""+url
        Dgllly()

elif mode==987651930:
        print ""+url
        Dglllly()

elif mode==987651929:
        print ""+url
        Dgllllly()

elif mode==987651928:
        print ""+url
        Dglllllly()

elif mode==987651927:
        print ""+url
        Dgllllllly()

elif mode==987652000:
        print ""+url
        rockcollectiony()

elif mode==987652001:
        print ""+url
        topinmusicy()

elif mode==987652002:
        print ""+url
        topinmusic2y()

elif mode==987652003:
        print ""+url
        topinmusic3y()

elif mode==987651925:
        print ""+url
        kttgty()

elif mode==987652100:
        print ""+url
        rockcollectionly()

elif mode==987652101:
        print ""+url
        topinmusicly()

elif mode==987652102:
        print ""+url
        topinmusic2ly()

elif mode==987652103:
        print ""+url
        topinmusic3ly()

elif mode==987655930:
        print ""+url
        Daay()


		

elif mode==987657899:
        print ""+url
        THEATERy()

elif mode==987655931:
        print ""+url
        THEATERBy()



elif mode==987655933:
        print ""+url
        THEATERB2ay()



elif mode==987655935:
        print ""+url
        THEATERB3ay()



elif mode==987655937:
        print ""+url
        KungFu1y()



elif mode==987659009:
        print ""+url
        zozozoy()

elif mode==987659010:
        print ""+url
        zombay()

elif mode==987659011:
        print ""+url
        pilatesy()

elif mode==987659012:
        print ""+url
        aerobicy()

elif mode==987659013:
        print ""+url
        yogay()

elif mode==987659014:
        print ""+url
        makeupy()

elif mode==987659015:
        print ""+url
        nutritiony()

elif mode==987659016:
        print ""+url
        healthy()

elif mode==987659017:
        print ""+url
        sportsy()

elif mode==987659018:
        print ""+url
        bidory()

elif mode==9876510000:
        print ""+url
        daty()

elif mode==9876510001:
        print ""+url
        dat1y()

elif mode==9876510002:
        print ""+url
        dok1y()



elif mode==9876510004:
        print ""+url
        dok3y()

elif mode==9876510005:
        print ""+url
        trlrsrty()

elif mode==9876510006:
        print ""+url
        POLARISy()



elif mode==9876510008:
        print ""+url
        POLARIS2y()

elif mode==9876510009:
        print ""+url
        SPORTEXTREMEy()



elif mode==9876510011:
        print ""+url
        SPORTEXTREME2y()

elif mode==9876510012:
        print ""+url
        binauraly()


elif mode==9876520000:
        print ""+url
        nostalgiay()
        

elif mode==9876520001:
        print ""+url
        nostalgia1y()

elif mode==9876520002:
        print ""+url
        kids99y()

elif mode==9876520003:
        print ""+url
        Broadcast99y()
        	
elif mode==9876520004:
        print ""+url
        lomdim99y()
	
elif mode==9876520005:
        print ""+url
        special99y()	

elif mode==9876520006:
        print ""+url
        music99y()

elif mode==9876520007:
        print ""+url
        kidsnew99y()

elif mode==9876520008:
        print ""+url
        LILI1y()


elif mode==9876520009:
        print ""+url
        Documentarysporty()



elif mode==9876520011:
        print ""+url
        Documentarysport2y()

elif mode==9876520012:
        print ""+url
        Documentarysport3y()

elif mode==9876520013:
        print ""+url
        Documentarysport4y()

elif mode==9876520014:
        print ""+url
        Documentarysport5y()

elif mode==9876520015:
        print ""+url
        shadowy()

elif mode==987657777777:
        print ""+url
        srbcy()

elif mode==9876520016:
        print ""+url
        ezmaintenanceplusy()

elif mode==9876520017:
        print ""+url
        PlayLists1y()

elif mode==9876520018:
        print ""+url
        PlayLists2y()



elif mode==9876520020:
        print ""+url
        PlayLkids1y()

elif mode==20021:
        print ""+url
        PlayLkids2y()


elif mode==20022:
        print ""+url
        juniory()
		
elif mode==20023:
        print ""+url
        nickjuniory()

elif mode==20024:
        print ""+url
        nicklodeony()

elif mode==20025:
        print ""+url
        logyy()

elif mode==20026:
        print ""+url
        hopy()

elif mode==20027:
        print ""+url
        hopyy()	

elif mode==20028:
        print ""+url
        lulyy()

elif mode==20029:
        print ""+url
        babyy()

elif mode==20030:
        print ""+url
        hoty()

elif mode==20031:
        print ""+url
        kidstvy()


elif mode==20032:
        print ""+url
        zoomy()		

elif mode==20033:
        print ""+url
        dsjuniory()

elif mode==20034:
        print ""+url
        nostaly()


elif mode==987652002122:
        print ""+url
        PlayLkids233y()

elif mode==987652002122456:
        print ""+url
        PlayLkids238787y()



elif mode==20035:
        print ""+url
        YouTubeIsrael1()

elif mode==20036:
        print ""+url
        YouTubeIsrael2()



elif mode==20038:
        print ""+url
        YouKODI2()


elif mode==8134256789:
        print ""+url
        index()

elif mode==18134256789:
        print ""+url
        index1()

elif mode==28134256789:
        print ""+url
        index2()

elif mode==38134256789:
        print ""+url
        index3()










xbmcplugin.endOfDirectory(int(sys.argv[1]))
