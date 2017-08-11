#-*- coding: utf-8 -*-




import wx
# w.Frame 을 상속받은 클래스 정의하기

class MyFrame(wx.Frame):
    
    def __init__(self,parent,title):
        #부모 생성자에 필요한 값 넘겨 주기
        super(MyFrame, self).__init__(parent,title=title,size=(300,250))
       
        
        #프레임에 TextCtrl 이라는 UI 추가하기
        wx.TextCtrl(self, style=wx.TE_MULTILINE)
        
        #하단 상태바 보이게 하기
        self.CreateStatusBar()
        
        #화면의 가운데에 보이게 하기
        self.Center()
        self.Show()
        

if __name__ == '__main__':
    app=wx.App()
    #MyFrame 객체 생성
    MyFrame(None, title=u"연습")
    app.MainLoop()