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
from kivymd_extensions.akivymd.uix.rating import AKRating
register('MatIcons',join(dirname(__file__),'assets/fonts/Material-Design-Iconic-Font.ttf'),join(dirname(__file__),'assets/fonts/zmd.fontd'))
# register('MatIcons',join(dirname(__file__),'assets/fonts/fontawesome.ttf'),join(dirname(__file__),'assets/fonts/fontawesome.fontd'))


import fontawesome
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
    textt = "The technique is similar to risotto. After softening the noodles in boiling water, you finish cooking them in a saute pan with the sauce, adding ladles of the pasta water until they are done. “That’s flour, egg, flavor you’re adding,” Clevenger says. Vigorous stirring creates an emulsion that allows the sauce to coat each strand. As with risotto, the tricky part is stopping before the noodles overcook."
    text_splt = textt.split()
    ex_text = None
    signin_pos = None
    signup_pos = None
    logtype = None
    btnlog = None

    def go_back(self):
        self.ids.exit.parent.screen_manager.current = 'Login'
    def go_Home(self):
        self.ids.signin_button.parent.screen_manager.current = 'Home'
    
    def go_Recipe(self):
        self.ids.Recipe.parent.screen_manager.current = 'Recipe'
        
        fontIcon = "[font=assets/fonts/fontawesome.ttf]" +  "  " + eval(self.ids.reccipe.icon) +"[/font]"
        
        i = 19
        print(self.text_splt[i])
        self.check_agn(i,self.text_splt)
        
        self.ids.reccipe.text = self.ex_text + '[ref=world][color=64dd17]'+"read more"+fontIcon+'[/color][/ref]'
        self.ids.reccipe.markup = True
    
    def check_agn(self,i,text_splt):
        fnal_textt = text_splt[i]
        if text_splt.count(fnal_textt) > 1:
            i-=1
            self.check_agn(i,self.text_splt)
            
        else:
            # fnal_textt = text_splt[i]
            self.ex_text = self.textt.split(text_splt[i])[0]

    open_field_box = 0
    increment_width = NumericProperty(0)
    increment_height = NumericProperty(0)

    def on_size(self, *args):
        if self.open_field_box:
            self.btnlog.width = self.width - dp(50)


    def start_animation(self):
        
        if self.logtype == "SignIn":
            hnum = 180
            self.btnlog = self.ids.signin_button
            self.btnlog.clear_widgets()
            # Animation(opacity=0, d=0.4).start(self.ids.signin_label)
        else:
            hnum = 370
            self.btnlog = self.ids.signup_button
            self.btnlog.clear_widgets()
            # Animation(opacity=0, d=0.4).start(self.ids.signup_label)


        # anim_transform_button = Animation(
        #     increment_width=self.width - dp(40) - self.btnlog.width,
        #     increment_height=dp(hnum),
        #     d=1.2,
        #     t="out_quart",
        # )
        # anim_transform_button.bind(on_progress=self.anim_transform_button_progress)
        # anim_transform_button.start(self)
        n = Animation(
            height=dp(hnum),
            width=dp(280),
            y=dp(200),
            
            d=1.2,
            t="out_quart",
        )
        n.bind(on_progress=self.anim_transform_button_progress)
        n.start(self.btnlog)

    def anim_transform_button_progress(self, animation, instance, value):
        def set_focus(*args):
            self.self.btnlog.children[-2].focus = True

        if value > 0.5 and not self.open_field_box:
            self.open_field_box = True
            height = 14
            duration = 0.8
            pos_x = 82

            signup = ["First Name", "Last Name", "Email", "Password","Confirm Password"]
            signin = ["Email", "Password"]
            if self.logtype == "SignIn":
                login = signin
            else:
                login = signup

            for name_field in login:
                height += 54
                duration += 0.2
                pos_x -= 10
                field = MDTextField(
                    x=dp(pos_x),
                    hint_text=name_field,
                    size_hint_x=None,
                    y=self.btnlog.height - dp(height),
                    width=self.btnlog.width - dp(72),
                    opacity=0,
                )
                
                # btnlog.md_bg_color=[1,1,1,1]
                anim_transform_button = Animation(md_bg_color=get_color_from_hex("#ffffff"))
                anim_transform_button.start(self.btnlog)
                field.color_mode = 'accent'
                
                self.btnlog.add_widget(field)
                
                animation = Animation(x=dp(36), opacity=1, t="out_quart", d=duration)
                # if duration > 1.5:
                #     animation.bind(on_complete=set_focus)
                animation.start(field)
            if self.logtype == "SignIn":
                btnData = ['Cancel','Login']
            else:
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
                self.btnlog.add_widget(field2)
                n=.72
    def Login(self, *args):
        self.Cancel()
        self.ids.signin_button.parent.screen_manager.current = 'Home'
    
    def Cancel(self, *args):
        self.open_field_box = False
        if self.logtype == "SignIn":
            cy = 110
            txt = "Sign In"
            bgclr = "#64dd17"
            ftclr = "ffffff"
        else:
            cy = 35
            txt = "Sign Up"
            bgclr = "#ffffff"
            ftclr = "000000"

        # anim_transform_button = Animation(
        #     increment_width=self.width - dp(40) - self.btnlog.width,
        #     increment_height=dp(0),
        #     d=1.2,
        #     t="out_quart",
        # )
        self.btnlog.clear_widgets()
        # anim_transform_button.start(self)
        # Animation(
        #     y=dp(cy),
            
        #     d=1.2,
        #     t="out_quart",
        # ).start(self.btnlog)
        n = Animation(
            height=dp(55),
            width=dp(230),
            y=dp(cy),
            
            d=1.2,
            t="out_quart",
        )
        n.start(self.btnlog)

        anim_transform_button = Animation(md_bg_color=get_color_from_hex(bgclr))
        anim_transform_button.start(self.btnlog)
        llbl = MDLabel(
                text= txt,
                pos_hint= {"center_x": .6, "center_y": .5},
                adaptive_size= True,
        )
        llbl.color = get_color_from_hex(ftclr)
        import weakref
        self.btnlog.ids['signin_label'] = weakref.ref(llbl)
        self.btnlog.add_widget(llbl)
    
    def LogFirst(self,*args):
        self.logtype = "SignIn"
        if self.signin_pos == None:
            self.signin_pos = True
            self.start_animation()
        else:
            if len(self.ids.signin_button.children) == 1:
                self.LogAgain()
    
    def SignUpFirst(self,*args):
        self.logtype = "SignUp"
        if self.signup_pos == None:
            self.signup_pos = True
            self.start_animation()
        else:
            if len(self.ids.signup_button.children) == 1:
                self.SignUpAgain()


    def LogAgain(self,*args):
        print(len(self.ids.signin_button.children))
        self.ids.signin_button.clear_widgets()
        self.start_animation()
    
    def SignUpAgain(self,*args):
        print(len(self.ids.signup_button.children))
        self.ids.signup_button.clear_widgets()
        self.start_animation()
        
        




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
        Builder.load_file("veg.kv")
        self.wm = WindowManager(transition=FadeTransition())
        screens = [
            MainWindow(name='Login')
        ]

        for screen in screens:
            self.wm.add_widget(screen)
        
        return self.wm

    
# on_touch_down:
#     if self.collide_point(*args[1].pos) \
#     and len(signup_button.children) == 1: root.SignUpFirst()
   
if __name__=='__main__':
    MainApp().run()
