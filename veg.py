# from kivy.config import Config
# Config.set('graphics','resizable',True)
from kivy.core.window import Window
Window.size = (350, 760)
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.behaviors import ButtonBehavior, button
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.properties import StringProperty
from kivymd.uix.label import MDLabel
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.garden.iconfonts import register
from os.path import dirname,join
from kivy.metrics import dp
from kivy.properties import (
    BooleanProperty,
    ColorProperty,
    DictProperty,
    NumericProperty,
    ObjectProperty,
    OptionProperty,
    StringProperty,
)
from kivymd.uix.button import MDFloatingActionButton, MDFlatButton
from kivy.properties import NumericProperty
from kivymd.uix.textfield import MDTextField
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.behaviors import RectangularRippleBehavior
from kivy.uix.screenmanager import FadeTransition, ScreenManager
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex
from kivymd.color_definitions import colors
register('MatIcons',join(dirname(__file__),'assets/fonts/Material-Design-Iconic-Font.ttf'),join(dirname(__file__),'assets/fonts/zmd.fontd'))
# register('MatIcons',join(dirname(__file__),'assets/fonts/fontawesome.ttf'),join(dirname(__file__),'assets/fonts/fontawesome.fontd'))

kv = '''
#: import FadeTransition kivy.uix.screenmanager.FadeTransition
#: import gch kivy.utils.get_color_from_hex
#: import rgba kivy.utils.rgba
#: import icon kivy.garden.iconfonts.icon
            
<MainWindow>:
    ScreenManager:
        id: screen_manager
        transition: FadeTransition()
        Screen:
            name:'Login'    
            MDBoxLayout:
                orientation:'vertical'
                id: Bod
                FitImage:
                    source:'pizza.png'
                    size:self.size
                    pos:self.pos
            MDFloatLayout:
                screen_manager:screen_manager
                MDBoxLayout:
                    orientation:"horizontal"
                    size_hint:(None,None)
                    pos_hint:{'center_x':.4,'center_y':.9}
                    MDLabel:
                        id:verified
                        text:"Vegified."
                        color:gch("#000000")
                        size_hint:(None,None)
                        width:'170dp'
                        font_size:'30sp'
                        font_name: "assets/fonts/Poppins-ExtraBold.ttf"
                    Image:
                        source:'leaf.png'
                        size_hint:(None,None)
                        width:'30dp'
                        pos_hint:{'center_y':.6}
                MDLabel:
                    id:verified
                    text:'        All your favourite dishes,'
                    color:gch("#000000")
                    size_hint:(None,None)
                    width:'300dp'
                    pos_hint:{'center_x':.5,'center_y':.83}
                    font_size:'20sp'
                    font_name: "assets/fonts/Poppins-Regular.ttf"
                MDLabel:
                    id:verified
                    text:'                  but vegan.'
                    color:gch("#000000")
                    size_hint:(None,None)
                    width:'300dp'
                    pos_hint:{'center_x':.5,'center_y':.80}
                    font_size:'20sp'
                    font_name: "assets/fonts/Poppins-Regular.ttf"

                CustomButton:
                    id: signin_button
                    y: "110dp"
                    pos_hint:{'center_x':.5}
                    size_hint: None, None
                    md_bg_color:gch("#64dd17")
                    radius:[30,0,30,0]
                    size:
                        root.width  - dp(120) + root.increment_width, \
                        dp(56) + root.increment_height
                    on_touch_down:
                        if self.collide_point(*args[1].pos) \
                        and len(signin_button.children) == 1: root.start_animation()

                    CustomLabel:
                        id: signin_label
                        text: "Log IN"
                        text_color: 1, 1, 1, 1
                        pos_hint: {"center_x": .5, "center_y": .5}
                        adaptive_size: True

                CustomButton:
                    id: signup_button
                    y: "35dp"
                    pos_hint:{'center_x':.5}
                    size_hint: None, None
                    md_bg_color:gch("#ffffff")
                    radius:[30,0,30,0]
                    size:
                        root.width  - dp(120) , \
                        dp(56) 
                    on_touch_down:
                        if self.collide_point(*args[1].pos) \
                        and len(signup_button.children) == 1: root.start_animation()

                    CustomLabel:
                        id: signup_label
                        text: "SIGN IN"
                        text_color: 0, 0, 0, 1
                        pos_hint: {"center_x": .5, "center_y": .5}
                        adaptive_size: True

        Screen:
            name:'Home'
            MDBoxLayout:
                md_bg_color:gch("#ffffff")
                screen_manager:screen_manager
                orientation:"vertical"
                spacing:dp(20)
                MDBoxLayout:
                    orientation:'horizontal'
                    size_hint_y:None
                    height:'50dp'
                    screen_manager:screen_manager
                    padding:20,0,20,0

                    MDLabel:
                        text: 'Browse Recipes'
                        color:gch("#000000")
                        size_hint_y:None
                        height:'30dp'
                        font_size:'25sp'
                        font_name: "assets/fonts/Poppins-ExtraBold.ttf"
                    MDIconButton:
                        id:exit
                        icon: 'exit-to-app'
                        user_font_size: "20sp"
                        theme_text_color: "Custom"
                        text_color: gch("#64dd17")
                        pos_hint: {"center_x": .9, "center_y": .3}
                        on_release: root.go_back()
                    
                ScrollView:
                    do_scroll_y: False
                    bar_widget:1
                    size_hint_y:None
                    height:'80dp'
                    GridLayout:
                        id: grid
                        rows: 1
                        size_hint_y: None
                        size_hint_x: None
                        width: self.minimum_width
                        height: "40dp"
                        row_default_height: 1
                        
                        Card:
                            id:card
                            MDIconButton:
                                icon: 'noodles'
                                pos_hint: {"center_x": .5, "center_y": .65}
                                user_font_size: "40sp"
                                theme_text_color: "Custom"
                                text_color: gch("#BDBDBD")
                            MDLabel:
                                text:'PASTA'
                                color:gch("#BDBDBD")
                                size_hint:(None,None)
                                pos_hint:{'center_x':.8,'center_y':.2}
                                font_size:'15sp'
                                font_name: "assets/fonts/Poppins-Regular.ttf" 
                        Separator1:
                            height:card.height
                        Card:
                            MDIconButton:
                                icon: 'pizza'
                                pos_hint: {"center_x": .5, "center_y": .65}
                                user_font_size: "40sp"
                                theme_text_color: "Custom"
                                text_color: gch("#64dd17")
                            MDLabel:
                                text:'ITALIAN'
                                color:gch("#000000")
                                size_hint:(None,None)
                                pos_hint:{'center_x':.8,'center_y':.2}
                                font_size:'15sp'
                                font_name: "assets/fonts/Poppins-Regular.ttf"
                        Separator1:
                            height:card.height
                        Card:
                            MDIconButton:
                                icon: 'hamburger'
                                pos_hint: {"center_x": .5, "center_y": .65}
                                user_font_size: "40sp"
                                theme_text_color: "Custom"
                                text_color: gch("#BDBDBD")
                            MDLabel:
                                text:'BURGER'
                                color:gch("#000000")
                                size_hint:(None,None)
                                pos_hint:{'center_x':.8,'center_y':.2}
                                font_size:'15sp'
                                font_name: "assets/fonts/Poppins-Regular.ttf"
                        Separator1:
                            height:card.height
                        Card:
                            MDIconButton:
                                icon: 'rice'
                                pos_hint: {"center_x": .5, "center_y": .65}
                                user_font_size: "40sp"
                                theme_text_color: "Custom"
                                text_color: gch("#BDBDBD")
                            MDLabel:
                                text:'RICE'
                                color:gch("#000000")
                                size_hint:(None,None)
                                pos_hint:{'center_x':.9,'center_y':.2}
                                font_size:'15sp'
                                font_name: "assets/fonts/Poppins-Regular.ttf"
                        Separator1:
                            height:card.height
                
                ScrollView:
                    do_scroll_y:True
                    do_scroll_x:True
                    bar_widget:5
                    GridLayout:
                        id: todo_list
                        cols: 1
                        height: self.minimum_height
                        row_default_height: 5
                        size_hint_y:None
                        spacing:dp(10)
                        padding:20,0,20,0
                        screen_manager:screen_manager
                        ItemCard:
                            id:Recipe
                            screen:'Recipe'
                            on_release:root.go_Recipe()
                            MDBoxLayout:
                                orientation:'horizontal'
                                MDBoxLayout:
                                    size_hint:(None,None)
                                    width:'120dp'
                                    FitImage:
                                        source:'carb.png'
                                        size_hint:(None,None)
                                        width:'120dp'
                                        height:'150dp'
                                MDBoxLayout:
                                    orientation:'vertical'
                                    MDLabel:
                                        text:"Vegan Carbonara"
                                        size_hint:(None,None)
                                        width:'250dp'
                                        height:'40dp'
                                        pos_hint:{'x':.08}
                                        font_size:'15sp'
                                        font_name: "assets/fonts/Poppins-Bold.ttf"
                                    Detail:
                                        MDIconButton:
                                            id:fork
                                            icon: 'silverware-fork-knife'
                                            user_font_size: "25sp"
                                            theme_text_color: "Custom"
                                            text_color: gch("#000000")
                                            size_hint:(None,None)
                                            height:'30dp'
                                            pos_hint:{'center_y':.5}
                                        MDLabel:
                                            text:'Prep 10 mins'
                                            color:gch("#000000")
                                            size_hint:(None,None)
                                            height:'30dp'
                                            pos_hint:{'center_y':.5}
                                            font_size:'15sp'
                                            font_name: "assets/fonts/Poppins-Regular.ttf"
                                    Detail:
                                        MDIconButton:
                                            id:fork
                                            icon: 'clock-time-nine-outline'
                                            user_font_size: "25sp"
                                            theme_text_color: "Custom"
                                            text_color: gch("#000000")
                                            size_hint:(None,None)
                                            height:'30dp'
                                            pos_hint:{'center_y':.5}
                                        MDLabel:
                                            text:'Cook 30 mins'
                                            color:gch("#000000")
                                            size_hint:(None,None)
                                            height:'30dp'
                                            pos_hint:{'center_y':.5}
                                            font_size:'15sp'
                                            font_name: "assets/fonts/Poppins-Regular.ttf"
                                    Rating: 
                                        pos_hint:{'x':.05}
                                        FlatButton:
                                            text:"%s"%icon("zmdi-star",28)
                                            color:gch("#64dd17")
                                            markup:True
                                            background_normal:""
                                            font_size:'8sp'
                                            pos_hint: {"center_x": .1}
                                        FlatButton:
                                            text:"%s"%icon("zmdi-star",28)
                                            color:gch("#64dd17")
                                            markup:True
                                            background_normal:""
                                            font_size:'8sp'
                                            pos_hint: {"center_x": .1}
                                        FlatButton:
                                            text:"%s"%icon("zmdi-star",28)
                                            color:gch("#64dd17")
                                            markup:True
                                            background_normal:""
                                            font_size:'8sp'
                                            pos_hint: {"center_x": .1}
                                    MDLabel:
                                        text:" "
                                        size_hint:(None,None)
                                        width:'250dp'
                                        height:'20dp'
                                        pos_hint:{'x':.08}
                                        font_size:'15sp'
                                        font_name: "assets/fonts/Poppins-Bold.ttf"
                                    
                        ItemCard:
                            MDBoxLayout:
                                orientation:'horizontal'
                                MDBoxLayout:
                                    size_hint:(None,None)
                                    width:'120dp'
                                    FitImage:
                                        source:'meatballs.png'
                                        size_hint:(None,None)
                                        width:'120dp'
                                        height:'150dp'
                                MDBoxLayout:
                                    orientation:'vertical'
                                    MDLabel:
                                        text:"Vegan MeatBalls"
                                        size_hint:(None,None)
                                        width:'250dp'
                                        height:'40dp'
                                        pos_hint:{'x':.08}
                                        font_size:'15sp'
                                        font_name: "assets/fonts/Poppins-Bold.ttf"
                                    Detail:
                                        MDIconButton:
                                            id:fork
                                            icon: 'silverware-fork-knife'
                                            user_font_size: "25sp"
                                            theme_text_color: "Custom"
                                            text_color: gch("#000000")
                                            size_hint:(None,None)
                                            height:'30dp'
                                            pos_hint:{'center_y':.5}
                                        MDLabel:
                                            text:'Prep 10 mins'
                                            color:gch("#000000")
                                            size_hint:(None,None)
                                            height:'30dp'
                                            pos_hint:{'center_y':.5}
                                            font_size:'15sp'
                                            font_name: "assets/fonts/Poppins-Regular.ttf"
                                    Detail:
                                        MDIconButton:
                                            id:fork
                                            icon: 'clock-time-nine-outline'
                                            user_font_size: "25sp"
                                            theme_text_color: "Custom"
                                            text_color: gch("#000000")
                                            size_hint:(None,None)
                                            height:'30dp'
                                            pos_hint:{'center_y':.5}
                                        MDLabel:
                                            text:'Cook 30 mins'
                                            color:gch("#000000")
                                            size_hint:(None,None)
                                            height:'30dp'
                                            pos_hint:{'center_y':.5}
                                            font_size:'15sp'
                                            font_name: "assets/fonts/Poppins-Regular.ttf"
                                    Rating: 
                                        pos_hint:{'x':.05}
                                        FlatButton:
                                            text:"%s"%icon("zmdi-star",28)
                                            color:gch("#64dd17")
                                            markup:True
                                            background_normal:""
                                            font_size:'8sp'
                                            pos_hint: {"center_x": .1}
                                        FlatButton:
                                            text:"%s"%icon("zmdi-star",28)
                                            color:gch("#64dd17")
                                            markup:True
                                            background_normal:""
                                            font_size:'8sp'
                                            pos_hint: {"center_x": .1}
                                        FlatButton:
                                            text:"%s"%icon("zmdi-star",28)
                                            color:gch("#64dd17")
                                            markup:True
                                            background_normal:""
                                            font_size:'8sp'
                                            pos_hint: {"center_x": .1}
                                        FlatButton:
                                            text:"%s"%icon("zmdi-star-half",28)
                                            color:gch("#64dd17")
                                            markup:True
                                            background_normal:""
                                            font_size:'8sp'
                                            pos_hint: {"center_x": .1}
                                    MDLabel:
                                        text:" "
                                        size_hint:(None,None)
                                        width:'250dp'
                                        height:'20dp'
                                        pos_hint:{'x':.08}
                                        font_size:'15sp'
                                        font_name: "assets/fonts/Poppins-Bold.ttf"
                                    
                        ItemCard:
                            MDBoxLayout:
                                orientation:'horizontal'
                                MDBoxLayout:
                                    size_hint:(None,None)
                                    width:'120dp'
                                    FitImage:
                                        source:'spinach pizza.png'
                                        size_hint:(None,None)
                                        width:'120dp'
                                        height:'150dp'
                                MDBoxLayout:
                                    orientation:'vertical'
                                    MDLabel:
                                        text:"Vegan Spinach Pizza"
                                        size_hint:(None,None)
                                        width:'250dp'
                                        height:'40dp'
                                        pos_hint:{'x':.08}
                                        font_size:'15sp'
                                        font_name: "assets/fonts/Poppins-Bold.ttf"
                                    Detail:
                                        MDIconButton:
                                            id:fork
                                            icon: 'silverware-fork-knife'
                                            user_font_size: "25sp"
                                            theme_text_color: "Custom"
                                            text_color: gch("#000000")
                                            size_hint:(None,None)
                                            height:'30dp'
                                            pos_hint:{'center_y':.5}
                                        MDLabel:
                                            text:'Prep 10 mins'
                                            color:gch("#000000")
                                            size_hint:(None,None)
                                            height:'30dp'
                                            pos_hint:{'center_y':.5}
                                            font_size:'15sp'
                                            font_name: "assets/fonts/Poppins-Regular.ttf"
                                    Detail:
                                        MDIconButton:
                                            id:fork
                                            icon: 'clock-time-nine-outline'
                                            user_font_size: "25sp"
                                            theme_text_color: "Custom"
                                            text_color: gch("#000000")
                                            size_hint:(None,None)
                                            height:'30dp'
                                            pos_hint:{'center_y':.5}
                                        MDLabel:
                                            text:'Cook 30 mins'
                                            color:gch("#000000")
                                            size_hint:(None,None)
                                            height:'30dp'
                                            pos_hint:{'center_y':.5}
                                            font_size:'15sp'
                                            font_name: "assets/fonts/Poppins-Regular.ttf"
                                    Rating: 
                                        pos_hint:{'x':.05}
                                        FlatButton:
                                            text:"%s"%icon("zmdi-star",28)
                                            color:gch("#64dd17")
                                            markup:True
                                            background_normal:""
                                            font_size:'8sp'
                                            pos_hint: {"center_x": .1}
                                        FlatButton:
                                            text:"%s"%icon("zmdi-star-half",28)
                                            color:gch("#64dd17")
                                            markup:True
                                            background_normal:""
                                            font_size:'8sp'
                                            pos_hint: {"center_x": .1}
                                    MDLabel:
                                        text:" "
                                        size_hint:(None,None)
                                        width:'250dp'
                                        height:'20dp'
                                        pos_hint:{'x':.08}
                                        font_size:'15sp'
                                        font_name: "assets/fonts/Poppins-Bold.ttf"
                                    

                    
            BottomNavBar:
                screen_manager:screen_manager


        Screen:
            name:'Recipe'    
            MDBoxLayout:
                md_bg_color:gch("#ffffff")
                screen_manager:screen_manager
                orientation:"vertical"
                spacing:dp(20)
                MDBoxLayout:
                    orientation:'horizontal'
                    size_hint_y:None
                    height:'50dp'
                    screen_manager:screen_manager
                    MDIconButton:
                        id:exit
                        icon: 'arrow-left-bold'
                        user_font_size: "50sp"
                        theme_text_color: "Custom"
                        text_color: gch("#64dd17")
                        pos_hint: {"center_x": .01, "center_y": .3}
                        on_release: root.go_Home()

                    MDLabel:
                        text: 'Cook Time'
                        color:gch("#000000")
                        size_hint_y:None
                        height:'30dp'
                        font_size:'25sp'
                        pos_hint: {"center_x": .2, "center_y": .3}
                        font_name: "assets/fonts/Poppins-ExtraBold.ttf"
                ScrollView:
                    do_scroll_y:True
                    do_scroll_x:True
                    bar_widget:5
                    GridLayout:
                        id: todo_list
                        cols: 1
                        height: self.minimum_height
                        row_default_height: 5
                        size_hint_y:None
                        spacing:dp(10)
                        screen_manager:screen_manager
                        RecipeCard:
                            FitImage:
                                source:"carb.png"
                        MDLabel:
                            text: 'Method'
                            color:gch("#000000")
                            size_hint_y:None
                            height:'50dp'
                            font_size:'25sp'
                            pos_hint: {"center_x": .2}
                            font_name: "assets/fonts/Poppins-ExtraBold.ttf"
                        MDLabel:
                            text: 'Preheat the oven to 180°C/350°F/Gas mark 4. To make the croûtons, and brushboth sides of each slice with the oil.'
                            color:gch("#000000")
                            size_hint_y:None
                            height:'50dp'
                            font_size:'15sp'
                            pos_hint: {"center_x": .2}
                            font_name: "assets/fonts/Poppins-Regular.ttf"
                        
                        MDLabel:
                            text: 'Ingredients'
                            color:gch("#000000")
                            size_hint_y:None
                            height:'50dp'
                            font_size:'25sp'
                            pos_hint: {"center_x": .2}
                            font_name: "assets/fonts/Poppins-ExtraBold.ttf"
                        ScrollView:
                            do_scroll_y: False
                            bar_widget:1
                            size_hint_y:None
                            height:'200dp'
                            GridLayout:
                                id: grid
                                rows: 1
                                size_hint_y: None
                                size_hint_x: None
                                width: self.minimum_width
                                height: self.minimum_height
                                spacing:dp(20)
                                row_default_height: 1
                                Recipee:
                                    source:'onio.jpg'
                                    name:'Onion'
                                    quantity:'2 Chopped'
                                Recipee:
                                    source:'spinach.jpg'
                                    name:'Spinach'
                                    quantity:'3 leaves'
                                Recipee:
                                    source:'chilli.jpg'
                                    name:'Chille'
                                    quantity:'1 teaspoon'
                                Recipee:
                                    source:'tomato.jpg'
                                    name:'Tomato'
                                    quantity:'2 Chopped'
                                Recipee:
                                Recipee:
                                Recipee:


<Recipee@MDBoxLayout>:
    id:Recipee
    orientation:'vertical'
    size_hint:None,None
    height:self.minimum_height
    width:self.minimum_width
    source:''
    name:''
    quantity:''
    MDCard:
        id:rec
        elevation:12
        radius:[0,30,0,30]
        size_hint_y:None
        size_hint_x:None
        height:'100dp'
        width:'85dp'
        md_bg_color: gch("#FFFFFF")
        FitImage:
            source:Recipee.source
            size_hint_y:None
            size_hint_x:None
            pos_hint: {"top": 1}
            radius:[0,30,0,30]
    MDLabel:
        text:Recipee.name
        size_hint:None,None
        height:'20dp'
        width:'80dp'
        pos_hint:{'center_x':.6}
    MDLabel:
        text:Recipee.quantity
        size_hint:None,None
        height:'20dp'
        width:'80dp'
        font_size:'12sp'
        pos_hint:{'center_x':.6}


<FlatButton@Button>:
	background_normal: ''
	background_color: [1,1,1,0]
    size_hint_x:None
    width:'30dp'

<Detail@MDBoxLayout>:
    height:"30dp"
    size_hint_y:None
    md_bg_color: gch("#FFFFFF")

<Rating@MDBoxLayout>:
    height:"30dp"
    size_hint_y:None
    md_bg_color: gch("#FFFFFF")
        
<LoginButton@MDBoxLayout>:
    id: btntext
    size_hint_y:None
    size_hint_x:None
    height:"50dp"
    width:'200dp'
    radius:[30,0,30,0]
    text:''
    VegButton:
        id:in
        text:btntext.text
        color:gch("#ffffff")
        screen: 'Home'
        font_name: "assets/fonts/Poppins-SemiBold.ttf"
        font_size: "16sp"

<SignUpButton@MDBoxLayout>:
    id: btntext
    size_hint_y:None
    size_hint_x:None
    height:"50dp"
    width:'200dp'
    radius:[30,0,30,0]
    text:''
    VegButton:
        id:in
        text:btntext.text
        screen: 'Home'
        font_name: "assets/fonts/Poppins-SemiBold.ttf"
        font_size: "16sp"

<Card@UmCard>:
    md_bg_color: 1, 1, 1 ,1
    radius:[8]
    size_hint_y:None
    size_hint_x:None
    height:'60dp'
    width:'85dp'

<Separator1@MDLabel>:
    md_bg_color: gch("#BDBDBD")
    size_hint_y:None
    size_hint_x:None
    width:'3dp'

<ItemCard@MDCard>:
    elevation:12
    radius:[8]
    size_hint_y:None
    height:'150dp'
    md_bg_color: gch("#FFFFFF")

<RecipeCard@MDCard>:
    elevation:12
    radius:[8]
    size_hint_y:None
    height:'250dp'
    md_bg_color: gch("#FFFFFF")    



<BottomNavBar@MDBoxLayout>:
    md_bg_color: gch("#ffffff")
    orientation: 'horizontal'
    height: dp(65)
    size_hint_y: None
    padding: 10,0,0,10
    spacing: '40dp'
    MDIconButton:
        id:fork
        icon: 'magnify'
        user_font_size: "30sp"
        theme_text_color: "Custom"
        text_color: gch("#64dd17")
        size_hint:(None,None)
        height:'30dp'
        pos_hint:{'center_y':.5}
    MDIconButton:
        id:fork
        icon: 'cards-heart'
        user_font_size: "30sp"
        theme_text_color: "Custom"
        text_color: gch("#424242")
        size_hint:(None,None)
        height:'30dp'
        pos_hint:{'center_y':.5}
    MDIconButton:
        id:fork
        icon: 'account'
        user_font_size: "30sp"
        theme_text_color: "Custom"
        text_color: gch("#424242")
        size_hint:(None,None)
        height:'30dp'
        pos_hint:{'center_y':.5}
    MDIconButton:
        id:fork
        icon: 'share-variant'
        user_font_size: "30sp"
        theme_text_color: "Custom"
        text_color: gch("#424242")
        size_hint:(None,None)
        height:'30dp'
        pos_hint:{'center_y':.5}

        
<CustomLabel@MDLabel>
    theme_text_color: "Custom"
    text_color: app.theme_cls.primary_color


<CustomButton>


    
'''
class VegButton(ButtonBehavior, MDLabel):
    # def on_press(self):
    #     self.parent.parent.screen_manager.current = self.screen
    pass

        
class CustomButton(
    MDRelativeLayout,
    RectangularRippleBehavior,
    ButtonBehavior,
):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.md_bg_color = [1, 1, 1, 1]
        self.ripple_color = [0.7, 0.7, 0.7, 1]
        self.radius = [20,0,20,0]
        

class WindowManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.transition = FadeTransition()

class LoginScreen(Screen):
    pass

class Home(Screen):
    def go_back(self):
        self.manager.current = 'Login'

class Recipe(Screen):
    def go_back(self):
        self.manager.current = 'Home'

class MainWindow(Screen):
    def go_back(self):
        self.ids.exit.parent.screen_manager.current = 'Login'
    def go_Home(self):
        self.ids.signin_button.parent.screen_manager.current = 'Home'
    
    def go_Recipe(self):
        self.ids.Recipe.parent.screen_manager.current = 'Recipe'

    open_field_box = 0
    increment_width = NumericProperty(0)
    increment_height = NumericProperty(0)

    def on_size(self, *args):
        if self.open_field_box:
            self.ids.signin_button.width = self.width - dp(50)


    def start_animation(self):
        Animation(opacity=0, d=0.4).start(self.ids.signin_label)
        anim_transform_button = Animation(
            increment_width=self.width - dp(40) - self.ids.signin_button.width,
            increment_height=dp(270),
            d=1.2,
            t="out_quart",
        )
        anim_transform_button.bind(on_progress=self.anim_transform_button_progress)
        anim_transform_button.start(self)
        Animation(
            y=self.height - dp(600),
            
            d=1.2,
            t="out_quart",
        ).start(self.ids.signin_button)

    def anim_transform_button_progress(self, animation, instance, value):
        def set_focus(*args):
            self.ids.signin_button.children[-2].focus = True

        if value > 0.5 and not self.open_field_box:
            self.open_field_box = True
            height = 14
            duration = 0.8
            pos_x = 82

            for name_field in ["First Name", "Last Name", "Email", "Password"]:
                height += 54
                duration += 0.2
                pos_x -= 10
                field = MDTextField(
                    x=dp(pos_x),
                    hint_text=name_field,
                    size_hint_x=None,
                    y=self.ids.signin_button.height - dp(height),
                    width=self.ids.signin_button.width - dp(72),
                    opacity=0,
                )
                
                self.ids.signin_button.md_bg_color=[1,1,1,1]
                field.color_mode = 'accent'
                
                self.ids.signin_button.add_widget(field)
                
                animation = Animation(x=dp(36), opacity=1, t="out_quart", d=duration)
                if duration > 1.5:
                    animation.bind(on_complete=set_focus)
                animation.start(field)
            btnData = ['Cancel','Register']

            n=.28
            for i in range(2):
                btnid = ['cancel','login']
                Cmd = [self.Cancel,self.Login]
                for d in range(2):
                    field2 = VegButton(
                        
                            text=btnData[i],
                            size_hint_y=None,
                            height=dp(20),
                            size_hint_x=None,
                            width=dp(100),
                            pos_hint={'center_x':n,'center_y':.13},
                        )
                field2.id = btnid[d]
                field2.bind(on_press=Cmd[i])
                self.ids.signin_button.add_widget(field2)
                n=.72
    def Login(self, *args):
        self.ids.signin_button.parent.screen_manager.current = 'Home'
    
    def Cancel(self, *args):
        self.ids.signin_button.parent.screen_manager.current = 'Login'



class UmCard(FakeRectangularElevationBehavior,MDFloatLayout):
    title = StringProperty()
    description = StringProperty()



class MainApp(MDApp):

    def back_button_handler(self, window, key, *args):
        if key == 27:
            if self.manager.current == 'Home':
                self.manager.get_screen("Home").go_back()
                return True
            elif self.manager.current == 'Login':
                return False

    def build(self):
        Builder.load_string(kv)
        self.wm = WindowManager(transition=FadeTransition())
        screens = [
            MainWindow(name='Login')
        ]

        for screen in screens:
            self.wm.add_widget(screen)
        
        return self.wm

    
    
   
if __name__=='__main__':
    MainApp().run()