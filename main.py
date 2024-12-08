from flet import *

def main(page:Page):
        page.bgcolor = "f0f8ff"
        #profile links
        def visit_twitter():
                WebView("www.twitter.com/@eyahnz")
                page.update()

        t1 =Text("Preyamble of The Company",size=18,color="blue400")
        t3 = Text("CEO of the Company  ?",size=18,color="blue400")
        t5 =Text("Goal & Objects of botoSoft",size=18,color="blue400")
        t7 =Text("Location",size=18,color="blue400")
        t8 = Text("""Dately has its official headquaters in Jinja Uganda(ug) Street jinja-kampala high way POBOX 44 Bugembe and your official mail is info@dately.com .Note that your data is physically stored on amazon aws s3 server which we pay monthly for hosting and data management and retrieval.""",color=colors.with_opacity(0.5,"black"),size=13)
        t6 = Text("""To protect our users data safely without any compromisatiom and interchange for personal gains.The assure you that if you use the service your data is a key.To protect our users acounts safely without sharing your info and data will always stay encrypted.This will enable you do your online activity here without worries on your personal data suchs message chats.""",color=colors.with_opacity(0.5,"black"),size=13)
        t4 =Text("""Dately is officialy under Eyahn TheDone (young software enginner) aka Mwesigwa Ian Lubogo. He coded this app when he accidently was practising coding in python at home.This app was purely coded in python as the front end and black end """,color=colors.with_opacity(0.5,"black"),size=13)
        t2 =Text("""Dately is an official legit dating site that has no charges on how their customer date,It was started in 2024 in the month of April we it was officially released to the general public.It focuses and finds people their patterns and make love. Dately is under botoSoft Companies limited .""",color=colors.with_opacity(0.5,"black"),size=13)
         #about us page
        def Aboutus():
                page.clean()
                page.add(
                        SafeArea(
                                Container(
                                        content=Column([
                                                Row([IconButton(icon=cupertino_icons.BACK,icon_color=cupertino_colors.SYSTEM_BLUE,on_click=lambda _:settings())
                                        ,Text("     About Us   ",size=18,color=cupertino_colors.ACTIVE_BLUE)]),
                        Divider(color=colors.BLACK12,height=1),

                        #content in about us 
                        Row([
                              t1  
                        ]),

                        t2,


                        Row([
                                t3
                        ]),

                        t4



                        #more
                        ,Row([
                                t5
                        ]),

                       t6
                                        
                                        
                                        
                        
                        #more
                        ,Row([
                                t7
                        ]),

                       t8          
                              ],alignment=CrossAxisAlignment.CENTER)
                                )
                        )
                )
                page.update()       
        #functions  in settings

        def switch_theme_l(e):
                print()
                theme_switch.track_outline_color ="green"
                page.theme_mode = ThemeMode.LIGHT
                page.update()

        
        def switch_theme(e):
                
                if e.control.value ==True:
                        theme_switch.track_outline_color ="green"
                        page.theme_mode = ThemeMode.DARK
                        logal_text.color =colors.BLUE_700
                        t1.color ="blue400"
                        t2.color ="blue400"
                        t3.color ="blue400"
                        t4.color ="blue400"
                        t5.color ="blue400"
                        t6.color ="blue400"
                        t7.color ="blue400"
                        t8.color ="blue400"

                else:
                        theme_switch.track_outline_color ="black"
                        page.theme_mode = ThemeMode.LIGHT    
                        logal_text.color =colors.BLACK45 
                        t1.color ="blue400" 
                        t2.color ="blue400" 
                        t3.color ="blue400"
                        t4.color ="blue400" 
                page.update()


                print(e.control)
        #search page
        def search_tab():
                page.clean()
                page.appbar.visible=False
                #page.bottom_appbar.visible =False
                page.add(
                        SafeArea(
                                Column([
                                        Container(
                                                content=Row([
                                                IconButton(icon=cupertino_icons.BACK,icon_color=colors.BLUE_700,on_click=lambda _:chats()),
                                                Container(
                                                        content=TextField(width=150,height=40,border=InputBorder.NONE,show_cursor=True,cursor_color="blue700"),
                                                        padding=padding.only(bottom=20)
                                                ),
                                                IconButton(icon=cupertino_icons.SEARCH,icon_color=cupertino_colors.ACTIVE_BLUE,visible=True)
                                        ],alignment=MainAxisAlignment.CENTER),
                                        bgcolor=colors.with_opacity(0.5,"blue50"),
                                        height=60,
                                        border_radius=BorderRadius(top_left=20,top_right=20,bottom_left=20,bottom_right=20)
                                        )
                                ])
                        )
                )
                page.update()


        #chats list tile
        # 
        # 
        #         
        #bottom app bar
        
        #widgets chats
        #
        chats_tab = SafeArea(
                Column([
                #page.appbar = AppBar()
                Container(
                        content=Row([
                                #content in search row
                                Text("search now !",size=16,color=colors.with_opacity(0.5,"blue"))

                        ]),bgcolor=colors.with_opacity(0.3,"blue50"),width=page.width,height=45,border_radius=BorderRadius(top_left=30,top_right=30,bottom_left=30,bottom_right=30),
                        on_click=lambda _:search_tab(),
                        padding=padding.only(left=80)
                ),

                #list tile of the charts
                #chats_listTile

        ]))
       
        #widgets settings
        theme_switch = Switch(active_color="green",on_change=switch_theme)
        theme_switch_light =  Switch(active_color="green",on_change=switch_theme_l)

        #logal text
        logal_text =Text("Dately",color=colors.BLACK45,size=20)

        settings_tab = SafeArea(
                Column([
                        Row([IconButton(icon=cupertino_icons.BACK,icon_color=cupertino_colors.SYSTEM_BLUE,on_click=lambda _:chats())
                        ,Text("     Settings   ",size=18,color=cupertino_colors.ACTIVE_BLUE)]),
                        Divider(color=colors.BLACK12,height=1),
                        #main content
                        Container(
                                width=page.width,
                                height= 60,
                                bgcolor=colors.with_opacity(0.5,"blue50"),
                                border_radius=BorderRadius(top_left=10,top_right=10,bottom_left=10,bottom_right=10),

                                content=Row([
                                        Text("Dark Mode",size=17,color=colors.BLUE_200),
                                       theme_switch
                                ],alignment=MainAxisAlignment.SPACE_BETWEEN),padding=padding.all(6)
                        ),
                        Divider(height=1,color=colors.BLACK12),


                        Container(
                                width=page.width,
                                height= 60,
                                bgcolor=colors.with_opacity(0.5,"blue50"),
                                border_radius=BorderRadius(top_left=10,top_right=10,bottom_left=10,bottom_right=10),

                                content=Row([
                                        Text("Restricted Mode",size=17,color=colors.BLUE_200),
                                       theme_switch_light
                                ],alignment=MainAxisAlignment.SPACE_BETWEEN),padding=padding.all(6)
                        ),
                        Divider(height=1,color=colors.BLACK12),


                        Container(
                                width=page.width,
                                height= 60,
                                bgcolor=colors.with_opacity(0.5,"blue50"),
                                border_radius=BorderRadius(top_left=10,top_right=10,bottom_left=10,bottom_right=10),

                                content=Row([
                                        IconButton(icon=cupertino_icons.PERSON_ALT),
                                        Text("Follow Us",size=17,color=colors.BLUE_200),

                                
                                ],alignment=MainAxisAlignment.SPACE_BETWEEN),padding=padding.all(6)
                        ),

                        


                        # other items
                        Container(
                                width=page.width,
                                height= 50,
                                #border=Border(left=BorderSide(color="blue",width=20)),
                                bgcolor=colors.with_opacity(0.5,"blue50"),
                                border_radius=BorderRadius(top_left=10,top_right=10,bottom_left=10,bottom_right=10),

                                content=Row([
                                        Image(src="assets/facebook.png",width=30,height=30),
                                        TextButton("@Eyahn ",style=ButtonStyle(text_style=TextStyle(decoration_color="black12",color="black12")))

                                ]
                        ),padding=padding.only(left=7),
                        on_click=lambda _:WebView("www.facebook.com/@eyahhnz")),

                                             # other items
                        Container(
                                width=page.width,
                                height= 50,
                                #border=Border(left=BorderSide(color="black",width=20)),
                                bgcolor=colors.with_opacity(0.5,"blue50"),
                                border_radius=BorderRadius(top_left=10,top_right=10,bottom_left=10,bottom_right=10),

                                content=Row([
                                        Image(src="assets/tik-tok.png",width=30,height=30),
                                        TextButton("@eyahnz",style=ButtonStyle(text_style=TextStyle(decoration_color="black12")))

                                ]
                        ),padding=padding.only(left=7),
                        on_click=lambda _:WebView("www.tiktik.com/@eyahnz")),


                                       # other items
                        Container(
                                width=page.width,
                                height= 50,
                                #border=Border(left=BorderSide(color="red800",width=20)),
                                bgcolor=colors.with_opacity(0.5,"blue50"),
                                border_radius=BorderRadius(top_left=10,top_right=10,bottom_left=10,bottom_right=10),

                                content=Row([
                                        Image(src="assets/twitter.png",width=30,height=30),
                                        TextButton("@eyahn",style=ButtonStyle(text_style=TextStyle(decoration_color="black12")))

                                ]
                        ),padding=padding.only(left=7),
                        on_click=lambda _:visit_twitter),

                         #more profiles
                        Container(
                                width=page.width,
                                height= 50,
                                #border=Border(left=BorderSide(color="black",width=20)),
                                bgcolor=colors.with_opacity(0.5,"blue50"),
                                border_radius=BorderRadius(top_left=10,top_right=10,bottom_left=10,bottom_right=10),

                                content=Row([
                                        Image(src="assets/tik-tok.png",width=30,height=30),
                                        TextButton("@eyahnz",style=ButtonStyle(text_style=TextStyle(decoration_color="black12")))

                                ]
                        ),padding=padding.only(left=7),
                        on_click=lambda _:WebView("www.tiktik.com/@eyahnz")),



                        #main content
                        Container(
                                width=page.width,
                                height= 60,
                                bgcolor=colors.with_opacity(0.5,"blue50"),
                                border_radius=BorderRadius(top_left=10,top_right=10,bottom_left=10,bottom_right=10),

                                content=Row([
                                        Text("About Us",size=17,color=colors.BLUE_200),
                                       
                                ],alignment=MainAxisAlignment.SPACE_BETWEEN),padding=padding.all(6),
                                on_click=lambda _:Aboutus()
                        ),



                        





                ],spacing=10)
        )




        #ai only ====================================================================
              #ai search
        search_ai = IconButton(icon=cupertino_icons.SEARCH_CIRCLE,icon_color="blue300")   



        def ai_gpt():
                page.clean()
                page.appbar.visible =False
                # appbar in ai page
                page.appbar =AppBar(
                        
                        leading= IconButton(icon=cupertino_icons.BACK,icon_color="blue",on_click=lambda _:chats()),
                        title=Text("Smart A.I",size=17,color="blue200"),

                )
                page.floating_action_button.visible =False
                page.bottom_appbar = BottomAppBar(
                        content=Row([
                                IconButton(icon =cupertino_icons.PLUS,icon_color="blue300"),TextField("",width=180,border_color=colors.with_opacity(0.5,"blue"),
                                cursor_color="blue200"),search_ai
                        ],alignment=MainAxisAlignment.CENTER)
                        
                )
                
                page.add(
                        SafeArea(
                                Container(content=Column([
                                        Row([
                                                
                                                
                                        ])

                                        
                                ]))
                        )
                )
                page.update()
        #settings
              # ccomponets
        

        def settings():
                page.clean()
                page.scroll ="auto"
                page.add(settings_tab)
                page.appbar.visible =False
                page.floating_action_button.visible=False
                page.update()
        #chats
        def chats():
                page.clean()
                page.appbar =AppBar(
                  
                        title=logal_text,
                        actions=[
                                IconButton(icon=icons.MENU,icon_color =colors.BLUE_100,on_click=lambda _:settings())
                        ],visible=True
                )


                #action floating button
                page.floating_action_button =FloatingActionButton(
                        text="A.I",visible=True,on_click=lambda _:ai_gpt()
                )


                #All widhets here

                page.add(
                        
                chats_tab,
                bottom_appbar)
                page.update()
        #bottom sheeets
        def bottomsheet():
                page.clean()
                 
                page.update()   
       
        bottom_appbar = BottomAppBar(
        content=Row([
                IconButton(icon=cupertino_icons.CHAT_BUBBLE,icon_color="blue",on_click=lambda _:chats()),
                IconButton(icon=cupertino_icons.PERSON),
                IconButton(icon=cupertino_icons.SETTINGS_SOLID,on_click=lambda _:bottomsheet())               
        ],alignment=MainAxisAlignment.CENTER,
        spacing=50)
        )
        chats()
        #page.add(bottom_appbar)
app(target=main)                      
