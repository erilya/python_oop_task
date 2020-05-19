import os

from MainWindowUI import Ui_MainWindow as MainWindowUI
from Game import Game

from PyQt5.QtGui import QMouseEvent, QPainter, QStandardItemModel, QColor, QBrush, QPen
from PyQt5.QtWidgets import QMainWindow, QItemDelegate, QStyleOptionViewItem
from PyQt5.QtCore import QModelIndex, QRectF, Qt, QTimer, QEventLoop


class MainWindow(QMainWindow, MainWindowUI):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self.__cell_colors = [QColor(255,0,0),QColor(0,255,0),QColor(0,0,255),QColor(255,255,0),QColor(138,43,226)]
        self.__frozen = True
        self.__animation_vw = None

        self._game = Game(8, len(self.__cell_colors), 3)
        self.game_resize(self._game)


        class MyDelegate(QItemDelegate):
            def __init__(self, parent=None, *args):
                QItemDelegate.__init__(self, parent, *args)

            def paint(self, painter: QPainter, option: QStyleOptionViewItem, idx: QModelIndex):
                painter.save()
                self.parent().on_item_paint(idx, painter, option)
                painter.restore()

        self.gameFieldTableView.setItemDelegate(MyDelegate(self))
        self.gameFieldTableView.setShowGrid(False)

        # такие ухищрения, т.к. не предусмотрено сигналов для правой кнопки мыши
        def new_mouse_press_event(e: QMouseEvent) -> None:
            idx = self.gameFieldTableView.indexAt(e.pos())
            self.on_item_clicked(idx, e)
        self.gameFieldTableView.mousePressEvent = new_mouse_press_event

        self.newGamePushButton.clicked.connect(self.on_new_game)

        self.new_game()


    def game_resize(self, game: Game) -> None:
        model = QStandardItemModel(game.size, game.size)
        self.gameFieldTableView.setModel(model)
        self.update_view()

    def update_view(self):
        self.gameFieldTableView.viewport().update()
        score = self._game.score
        if self.__animation_vw is not None:
            score = self.__animation_vw["score"]
        self.minesLcdNumber.display(score)


    def new_game(self):
        self.__frozen = True
        self.__animation_vw = None
        self._game.new_game()
        self.game_resize(self._game)
        self.update_view()
        self.__frozen = False


    def on_new_game(self):
        self.new_game()

    def on_item_paint(self, e: QModelIndex, painter: QPainter, option: QStyleOptionViewItem) -> None:

        item = self._game[e.row(), e.column()]
        if self.__animation_vw is not None:
            item = self.__animation_vw["cells"][e.row()][e.column()]

        color = QColor(128,128,128)
        if item is not None:
            color = self.__cell_colors[item]

        painter.fillRect(QRectF(option.rect),QBrush(color))
        painter.drawRect(QRectF(option.rect))

    def on_item_clicked(self, e: QModelIndex, me: QMouseEvent=None) -> None:
        if self.__frozen:
            return
        if me.button() == Qt.LeftButton:
            self.__frozen = True
            result_vw = self._game.step(min(e.row(),self._game.size-2), min(e.column(),self._game.size-2))

            for self.__animation_vw in result_vw:
                self.update_view()
                loop = QEventLoop()
                QTimer.singleShot(200, loop.quit)
                loop.exec_()
            self.__frozen = False
            self.__animation_vw = None


