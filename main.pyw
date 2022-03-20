# -*- coding: utf-8 -*-
import sys
import ctypes
import random

from PySide6.QtCore import (
    QCoreApplication,
    QMetaObject,
    QRect,
    Slot,
    Qt
)
from PySide6.QtGui import (
    QResizeEvent,
    QIcon,
    QFont
)
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QLayoutItem,
    QLCDNumber,
    QGroupBox,
    QWidget,
    QLabel,
)

import resources


class Window(QWidget):
    classes = (
        "Barbarian",
        "Bard",
        "Cleric",
        "Druid",
        "Fighter",
        "Monk",
        "Paladin",
        "Ranger",
        "Rouge",
        "Sorcerer",
        "Warlock",
        "Wizard"
    )
    
    races = (
        "Human",
        "Aasimar",
        "Warforged",
        "Yuan-ti-Pureblood",
        "Dwarf",
        "Triton",
        "Goliath",
        "Tabaxi",
        "Dragonborn",
        "Half-Elf",
        "LizardFolk",
        "Gnome",
        "Genasi",
        "Aarakocra",
        "ELF",
        "Tiefling",
        "Bugbear",
        "Kenku",
        "Githyanki",
        "Tortle",
        "Loxodon",
        "Centaur",
        "Kalashtar",
        "Changeling",
        "Shifter"
    )
    
    def __init__(self):
        super().__init__()
        
        self.resize(575, 300)
        self.setWindowTitle(self.tr(u"Your Next D&D Character!"))
        self.setWindowIcon(QIcon("://winico.png"))

        # Create layouts:
        self.mainLayout = QVBoxLayout(self)
        self.mainLayout.setObjectName(u"verticalLayout")
        
        self.charLayout = QHBoxLayout()
        self.charLayout.setObjectName(u"charLayout")

        self.statsLayout = QHBoxLayout()
        self.statsLayout.setObjectName(u"statsLayout")

        self.mainLayout.addLayout(self.charLayout)
        self.mainLayout.addLayout(self.statsLayout)
        
        # Now create the GroupBoxes:
        # -- character group boxes --
        self.raceGroupBox = QGroupBox(self.tr(u"Race"), self)
        self.raceGroupBox.setObjectName(u"raceGroupBox")
        self.charLayout.addWidget(self.raceGroupBox)

        self.classGroupBox = QGroupBox(self.tr(u"Class"), self)
        self.classGroupBox.setObjectName(u"classGroupBox")
        self.charLayout.addWidget(self.classGroupBox)
        
        # -- stats group boxes --
        self.strGroupBox = QGroupBox(self.tr(u"Strength"), self)
        self.strGroupBox.setObjectName(u"strGroupBox")
        self.statsLayout.addWidget(self.strGroupBox)

        self.dexGroupBox = QGroupBox(self.tr(u"Dexterity"), self)
        self.dexGroupBox.setObjectName(u"dexGroupBox")
        self.statsLayout.addWidget(self.dexGroupBox)

        self.conGroupBox = QGroupBox(self.tr(u"Constitution"), self)
        self.conGroupBox.setObjectName(u"conGroupBox")
        self.statsLayout.addWidget(self.conGroupBox)

        self.intGroupBox = QGroupBox(self.tr(u"Intelligence"), self)
        self.intGroupBox.setObjectName(u"intGroupBox")
        self.statsLayout.addWidget(self.intGroupBox)

        self.wisGroupBox = QGroupBox(self.tr(u"Wisdom"), self)
        self.wisGroupBox.setObjectName(u"wisGroupBox")
        self.statsLayout.addWidget(self.wisGroupBox)

        self.chaGroupBox = QGroupBox(self.tr(u"Charisma"), self)
        self.chaGroupBox.setObjectName(u"chaGroupBox")
        self.statsLayout.addWidget(self.chaGroupBox)
        
        self.charGroupBoxes = {
            self.raceGroupBox,
            self.classGroupBox
        }
        
        self.statsGroupBoxes = {
            self.strGroupBox,
            self.dexGroupBox,
            self.conGroupBox,
            self.intGroupBox,
            self.wisGroupBox,
            self.chaGroupBox
        }
        
        for groupbox in self.statsGroupBoxes | self.charGroupBoxes:
            groupbox.setLayout(QHBoxLayout())  # Arbitrary layout
            
        for groupbox in self.charGroupBoxes:
            groupbox.layout().addWidget(label := QLabel(groupbox))
            
            label.setTextInteractionFlags(Qt.TextBrowserInteraction)
            label.setFont(QFont("Segoe UI", 28))
            groupbox.label = label
        
        for groupbox in self.statsGroupBoxes:
            groupbox.setAlignment(Qt.AlignCenter)
            groupbox.layout().addWidget(lcd := QLCDNumber(2, groupbox))
            groupbox.number = lcd
            
        # Create button and add it to main layout
        self.genPushButton = QPushButton(self.tr(u"Generate Your Next D&&D Character!"), self)
        self.genPushButton.setObjectName(u"genPushButton")
        self.genPushButton.clicked.connect(self.generate)
        self.mainLayout.addWidget(self.genPushButton)

        self.show()  # show window
    # __init__
    
    @Slot()
    def generate(self):
        for w in self.statsGroupBoxes:
            w.number.display(random.randint(1, 20))
            
        self.raceGroupBox.label.setText(random.choice(self.races))
        self.classGroupBox.label.setText(random.choice(self.classes))
    # generate


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    aumid = u'Alice.DndCharacterGenerator'

    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(aumid)
    sys.exit(app.exec())
