from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivy.core.window import Window
import requests
from kivy.lang import Builder
from kivymd.uix.list import MDList, OneLineListItem
from plyer import tts

Window.size=(300,500)
textfield_string='''
MDTextField:
    hint_text: "Enter Movie name"
    helper_text_mode: "on_focus"
    icon_right: "android"
    icon_right_color: app.theme_cls.primary_color
    pos_hint:{'center_x': 0.5, 'center_y': 0.8}
    size_hint_x:None
    width:300

'''

class DemoApp(MDApp):
    def build(self):
        self.theme_cls.theme_style="Dark"
        self.theme_cls.primary_palette="Yellow"
        self.scrren=Screen()
        self.movie_name=Builder.load_string(textfield_string)
        button=MDRectangleFlatButton(text="send",pos_hint={'center_x':0.5,'center_y':0.7},on_release=self.get_movies)
        self.mdlist=MDList()
        self.scrren.add_widget(self.movie_name)
        self.scrren.add_widget(button)


        return self.scrren
    def get_movies(self,obj):
        self.scrren.remove_widget(self.mdlist)
        self.mdlist.clear_widgets()
        name=self.movie_name.text
        url='http://73ae-35-245-115-230.ngrok.io/recommend_movie'+'?movie_name='+name
        payload=requests.get(url)
        message=payload.json()
        #tts.speak("my recomendation is.")
        print(message)
        for msg in message['recommend_movies']:
            #tts.speak(msg)
            self.mdlist.add_widget(OneLineListItem(text=msg))
        self.scrren.add_widget(self.mdlist)

            

DemoApp().run()



