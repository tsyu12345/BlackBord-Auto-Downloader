from __future__ import annotations
from abc import ABC
from abc import abstractmethod
from enum import Enum

from selenium import webdriver


class ILoginParam:
    
    def __init__(self, address:str, password:str) -> None:
        """_summary_
        BlackBoardへのログインパラメータ
        Args:
            address (str): ログインメールアドレス
            password (str): ログインパスワード
        """
        self.address = address
        self.password = password
        
        
class ILoginresult(Enum):
    """_summary_
    ログイン結果
    """
    SUCCESS = 1
    FAILED = 0
    


    
class AbsLogin(ABC):
    """_summary_
    BlackBoardへのログイン処理
    """
    def __init__(self, login_param:ILoginParam) -> None:
        """_summary_
        Args:
            login_param (ILoginParam): ログインパラメータ
        """
        self.login_param = login_param
        #self.driver:webdriver.Chrome = webdriver.Chrome()
        
        
    @abstractmethod
    def login(self) -> ILoginresult:
        """_summary_
        ログイン処理
        Returns:
            ILoginresult: ログイン結果
        """
        pass
    
    
class AbsFileDownloader(ABC):
    
    def __init__(self, destination_path:str) -> None:
        self.destination_path = destination_path
