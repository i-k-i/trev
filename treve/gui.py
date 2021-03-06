import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QGridLayout
from PyQt5 import QtCore
from PyQt5.QtGui import QCursor
# from PyQt5 import QtGui
from treve.ll import LinguaLeo
from treve import config
from treve.yat import auto_translate_ya
from treve.systools import get_sel

app = QApplication(sys.argv)

class Window(QWidget):
    def __init__(self, data=None, llo=None):
        super(Window, self).__init__()
        self.make_window(self.prepare_data(data))
        self.llo=llo

    def prepare_data(self, data):
        if not data:
            data = {
                'src': 'source',
                'yat': 'yandex translated',
                'll': 'lingualeo translated',
                'source': 'source_lang',
                'target': 'target_lang'
                }
        else:
            # for data.items()
            data['src']=data['src'].strip()
        return data

    def make_window(self, data):
        self.installEventFilter(self)
        # make window not decorated and on the top
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint| QtCore.Qt.FramelessWindowHint)
        self.cursor = QCursor()
        self.move(self.cursor.pos())
        #labels
        self.src_lable = QLabel(data['src'])
        self.yat_label = QLabel('Yndx say:')
        self.yat_trans = QLabel(data['yat']['text'][0])
        self.ll_label = QLabel('Leo say:')
        self.ll_trans = QLabel(data['ll'])
        #buttons
        self.yat_button = QPushButton('Add to dict', self)
        self.ll_button = QPushButton('Add to dict', self)
        self.yat_button.setEnabled(False)
        self.ll_button.setEnabled(False)
        if data['src']:
            if data['yat']['text'][0]:
                self.yat_button.setEnabled(True)
                self.yat_button.clicked.connect(lambda: self.add_to_lldict(data['src'], data['yat']['text'][0], data))
            if data['ll']:
                self.ll_button.setEnabled(True)
                self.yat_button.clicked.connect(lambda: self.add_to_lldict(data['src'], data['ll'], data))
        layout = QGridLayout(self)
        layout.addWidget(self.src_lable, 0, 0, 1,-1)
        layout.addWidget(self.yat_label, 1, 0)
        layout.addWidget(self.yat_button, 1, 2)
        layout.addWidget(self.yat_trans, 1, 1)
        layout.addWidget(self.ll_label, 2, 0)
        layout.addWidget(self.ll_trans, 2, 1)
        layout.addWidget(self.ll_button, 2, 2)
        #
    def exit(self):
        sys.exit(app.exec_())

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.exit()

    def add_to_lldict(self, word, tword, data):
        add_resp = self.llo.add_word(word, tword, data['source'], data['target'])
        self.exit()

    def eventFilter(self, object, event):
        if event.type()== QtCore.QEvent.WindowDeactivate:
            self.exit()
        return False

def parce_yat_lang(yat_result):
    source, target = yat_result['lang'].split('-')
    return source, target

def main():
    selected_text = get_sel()
    if not selected_text:
        sys.exit(app.exec_())
    yat_result = auto_translate_ya(selected_text)
    llo = LinguaLeo(config.ll_login, config.ll_passwd)
    llo.login()
    source, target = parce_yat_lang(yat_result)
    ll_trans_resp = llo.translate(selected_text, source=source, target=target)
    if ll_trans_resp:
        ll_trans = ll_trans_resp.json()['translation']
    else:
        ll_trans = None
    data = {
        'src': selected_text,
        'yat': yat_result,
        'll': ll_trans,
        'source': source,
        'target':target,
    }
    # import ipdb; ipdb.set_trace()
    w = Window(data=data, llo=llo)
    w.show()
    # import ipdb; ipdb.set_trace()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
