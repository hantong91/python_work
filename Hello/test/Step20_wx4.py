#-*- coding: utf-8 -*-

import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title,\
                                      size=(300, 500))
        #생성자에서 UI 초기화 하는 함수들 호출하는 구조로 만든다. 
        self.InitUI()
        self.Center()
        self.Show()
    # UI 초기화 하는 함수 정의 
    def InitUI(self):
        #Panel 객체
        panel=wx.Panel(self)
        
        #일반 버튼
        btn1=wx.Button(panel, label="눌러보셈", pos=(5, 5))
        #토글 버튼
        btn2=wx.ToggleButton(panel, label="토글버튼", pos=(100, 5))
        btn3=wx.Button(panel, label="종료", pos=(195, 5))
        
        # 각각의 버튼에 고유한 아이디 부여하기
        btn1.id=1
        btn2.id=2
        btn3.id=3
        
        # 세개의 버튼에 동일한 함수를 등록한다. 
        btn1.Bind(wx.EVT_BUTTON, self.BtnClicked)
        btn2.Bind(wx.EVT_TOGGLEBUTTON, self.BtnClicked)
        btn3.Bind(wx.EVT_BUTTON, self.BtnClicked)
        
        # 정적인 텍스트 출력 (label)
        wx.StaticText(panel, label="아이디", pos=(5,40))   # StaticText 수정할 수 없는 문자
        wx.StaticText(panel, label="비밀번호", pos=(5, 70))
        # 텍스트 컨트롤 (문자열 입력창)
        self.inputId=wx.TextCtrl(panel, pos=(100, 40))
        self.inputPwd=wx.TextCtrl(panel, pos=(100, 70))
        #로그인 버튼
        loginBtn = wx.Button(panel, label="로그인", pos=(100, 100))
        #로그인 버튼을 눌렀을때 호출되는 함수 등록
        loginBtn.Bind(wx.EVT_BUTTON, self.LoginBtnClicked)
        
    def LoginBtnClicked(self, event):
        # 입력한 아이디와 비밀번호를 읽어온다.
        id = self.inputId.GetValue()
        pwd = self.inputPwd.GetValue()
        msg = None
        if id == "gura" and pwd == "1234":
            msg="gura 회원님 반갑습니다."
        else:
            msg="아이디 혹은 비밀번호가 틀려요"
        dlg=wx.MessageDialog(self, msg, "알림", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
        
    # 3개의 버튼중 하나를 눌렀을때 호출되는 함수 
    def BtnClicked(self, event):
        # 눌러진 버튼의 참조값 얻어오기
        btn = event.GetEventObject()
        # 눌러진 버튼의 아이디 값 얻어오기
        if btn.id == 1:
            print "btn1 !"
        elif btn.id == 2:
            print "btn2 !"
        elif btn.id == 3:
            print "btn3 !"
        

if __name__ == "__main__":
    app=wx.App()
    MyFrame(None, title="버튼")
    app.MainLoop()
    