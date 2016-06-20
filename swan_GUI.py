# -*- coding: utf-8 -*-

import sys
import os
from PyQt4.QtGui import *
from PyQt4.QtCore import *


class Swan(QDialog):
    def __init__(self, parent=None):
        super(Swan, self).__init__(parent)

        self.createTitle()
        self.createTabWidget()
        self.createRun()

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.groupBox)
        mainLayout.addWidget(self.tabWidget)
        mainLayout.addWidget(self.groupBox2)

        self.setLayout(mainLayout)
        self.setWindowTitle(u'模拟系统')
        self.resize(900, 600)

    def createTitle(self):
        """标题"""
        self.groupBox = QGroupBox()
        self.groupBox.setStyleSheet('QGroupBox{border: 1px solid blue}')

        name = QLabel(u'基于SWAN模型的数值模拟系统 v1.0', self)
        # name = QLabel(u'数值模拟系统 v1.0', self)
        name.setAlignment(Qt.AlignCenter)
        company = QLabel(u'上海河口海岸科学研究中心', self)
        # company = QLabel(u'公司：', self)
        company.setAlignment(Qt.AlignCenter)
        author = QLabel(u'开发者：贾晓 黄华聪', self)
        author.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        font = QFont()
        font.setBold(True)
        font.setPointSize(15)
        name.setFont(font)

        grid = QGridLayout()
        grid.addWidget(name, 0, 0, 2, 3)
        grid.addWidget(company, 2, 2)
        grid.addWidget(author, 3, 2)

        self.groupBox.setLayout(grid)

    def createTabWidget(self):
        """
        Tab选项卡，注意与TableWidget的区别
        """
        self.tabWidget = QTabWidget()

        tab1 = QWidget()
        tab2 = QWidget()
        tab3 = QWidget()
        tab4 = QWidget()
        tab5 = QWidget()
        tab6 = QWidget()
        tab7 = QWidget()
        tab8 = QWidget()

        self.basicSet()
        tab1vbox = QVBoxLayout()
        tab1vbox.addWidget(self.tab1groupbox)
        tab1.setLayout(tab1vbox)

        self.gridSet()
        tab2vbox = QVBoxLayout()
        tab2vbox.addWidget(self.tab2groupbox)
        tab2.setLayout(tab2vbox)

        self.inputParameters()
        tab3_hbox = QHBoxLayout()
        tab3_hbox.addWidget(self.tab3_listwidget)
        tab3_hbox.addWidget(self.tab3_stack)
        tab3.setLayout(tab3_hbox)
        self.connect(self.tab3_listwidget, SIGNAL("currentRowChanged(int)"), self.tab3_stack,
                     SLOT("setCurrentIndex(int)"))

        self.boundarySet()
        tab4_hbox = QHBoxLayout()
        tab4_hbox.addWidget(self.tab4_groupbox1)
        tab4_hbox.addWidget(self.tab4_groupbox2)
        tab4.setLayout(tab4_hbox)

        self.source_sink_termSet()
        tab5_hbox = QHBoxLayout()
        tab5_hbox.addWidget(self.tab5_groupbox)
        tab5.setLayout(tab5_hbox)

        self.calculateSet()
        tab6_hbox = QHBoxLayout()
        tab6_hbox.addWidget(self.tab6_groupbox)
        tab6.setLayout(tab6_hbox)

        self.outputSet()
        tab7_hbox = QHBoxLayout()
        tab7_hbox.addWidget(self.tab7_listwidget)
        tab7_hbox.addWidget(self.tab7_stack)
        tab7.setLayout(tab7_hbox)
        self.connect(self.tab7_listwidget, SIGNAL("currentRowChanged(int)"), self.tab7_stack,
                     SLOT("setCurrentIndex(int)"))
        # tab7_vbox = QVBoxLayout()
        # tab7_vbox.addWidget(self.tab7_groupbox1)
        # tab7_vbox.addWidget(self.tab7_groupbox2)
        # tab7.setLayout(tab7_vbox)

        self.calculate_input_file()
        tab8_vbox = QVBoxLayout()
        tab8_vbox.addWidget(self.tab8_groupbox)
        tab8.setLayout(tab8_vbox)

        self.tabWidget.addTab(tab1, u"&基本设置")
        self.tabWidget.addTab(tab2, u"计算网格及设置")
        self.tabWidget.addTab(tab3, u"输入参量")
        self.tabWidget.addTab(tab4, u"边界设置")
        self.tabWidget.addTab(tab5, "源汇项设置")
        self.tabWidget.addTab(tab6, "计算设置")
        self.tabWidget.addTab(tab7, "输出设置")
        self.tabWidget.addTab(tab8, "计算输入文件")

    def createRun(self):
        self.groupBox2 = QGroupBox()
        self.pushButton = QPushButton("生成input文件")
        self.connect(self.pushButton, SIGNAL("clicked()"), self.writeFile)
        self.hboxlayout = QHBoxLayout()
        self.hboxlayout.addWidget(self.pushButton)
        self.groupBox2.setLayout(self.hboxlayout)
        self.input_lines = []

    def basicSet(self):
        self.tab1groupbox = QGroupBox()

        frame1 = QFrame()
        frame2 = QFrame()
        groupbox1 = QGroupBox(u'二维波浪场计算')

        label1 = QLabel(u'项目名称:')
        self.tab1_linedit1 = QLineEdit()
        label2 = QLabel(u'组次:')
        self.tab1_linedit2 = QLineEdit()
        hblayout1 = QHBoxLayout()
        hblayout1.addWidget(label1)
        hblayout1.addWidget(self.tab1_linedit1)
        hblayout1.addStretch(1)
        hblayout1.addWidget(label2)
        hblayout1.addWidget(self.tab1_linedit2)
        frame1.setLayout(hblayout1)

        label3 = QLabel(u'固定增水:')
        self.tab1_linedit3 = QLineEdit()
        label4 = QLabel(u'm')
        label5 = QLabel(u'nor:')
        self.tab1_linedit4 = QLineEdit()
        label6 = QLabel(u'°')
        self.tab1_checkbox = QCheckBox(u'&拖曳力饱和')
        self.tab1_checkbox.setChecked(True)
        label7 = QLabel(u'输出基准变量:')
        self.tab1_combobox1 = QComboBox()
        self.tab1_combobox1.addItems([u'波参数', u'能量参数'])
        hblayout2 = QHBoxLayout()
        hblayout2.addWidget(label3)
        hblayout2.addWidget(self.tab1_linedit3)
        hblayout2.addWidget(label4)
        hblayout2.addStretch(1)
        hblayout2.addWidget(label5)
        hblayout2.addWidget(self.tab1_linedit4)
        hblayout2.addWidget(label6)
        hblayout3 = QHBoxLayout()
        hblayout3.addWidget(self.tab1_checkbox)
        hblayout3.addStretch(1)
        hblayout3.addWidget(label7)
        hblayout3.addWidget(self.tab1_combobox1)
        hblayout3.addStretch(1)
        vboxlayout1 = QVBoxLayout()
        vboxlayout1.setAlignment(Qt.AlignLeft)
        vboxlayout1.addLayout(hblayout2)
        vboxlayout1.addLayout(hblayout3)
        frame2.setLayout(vboxlayout1)

        label8 = QLabel(u'模式:')
        self.tab1_combobox2 = QComboBox()
        self.tab1_combobox2.addItems([u'恒定', u'非恒定'])
        label9 = QLabel(u'坐标系:')
        self.tab1_combobox3 = QComboBox()
        self.tab1_combobox3.addItems([u'笛卡尔', u'球(墨卡托)', u'球(准笛卡尔)'])
        grid1 = QGridLayout()
        # grid1.setAlignment(Qt.AlignLeft)
        grid1.setColumnStretch(2, 1)
        grid1.addWidget(label8, 0, 0)
        grid1.addWidget(self.tab1_combobox2, 0, 1)
        grid1.addWidget(label9, 1, 0)
        grid1.addWidget(self.tab1_combobox3, 1, 1)
        groupbox1.setLayout(grid1)

        vboxlayout = QVBoxLayout()
        vboxlayout.addWidget(frame1)
        vboxlayout.addWidget(frame2)
        vboxlayout.addWidget(groupbox1)

        self.tab1groupbox.setLayout(vboxlayout)

    def gridSet(self):
        self.tab2groupbox = QGroupBox()

        label10 = QLabel(u'计算机网格剖分:')
        self.tab2_radiobutton1 = QRadioButton(u'矩形')
        self.tab2_radiobutton2 = QRadioButton(u'非结构')
        self.tab2_radiobutton2.setChecked(True)

        self.groupbox_rec = QGroupBox()
        tab2_label1 = QLabel("起始点坐标:")
        tab2_label_x1 = QLabel("X1:")
        self.tab2_linedit_x1 = QLineEdit()
        tab2_label_y1 = QLabel("Y1:")
        self.tab2_linedit_y1 = QLineEdit()
        tab2_label2 = QLabel("终点坐标:")
        tab2_label_x2 = QLabel("X2:")
        self.tab2_linedit_x2 = QLineEdit()
        tab2_label_y2 = QLabel("Y2:")
        self.tab2_linedit_y2 = QLineEdit()
        tab2_label3 = QLabel("步长:")
        tab2_label_dx = QLabel("DX:")
        self.tab2_linedit_dx = QLineEdit()
        tab2_label_dy = QLabel("DY:")
        self.tab2_linedit_dy = QLineEdit()
        tab2_grid1 = QGridLayout()
        tab2_grid1.addWidget(tab2_label1, 0, 0)
        tab2_grid1.addWidget(tab2_label_x1, 0, 1)
        tab2_grid1.addWidget(self.tab2_linedit_x1, 0, 2)
        tab2_grid1.addWidget(tab2_label_y1, 0, 3)
        tab2_grid1.addWidget(self.tab2_linedit_y1, 0, 4)
        tab2_grid1.addWidget(tab2_label2, 1, 0)
        tab2_grid1.addWidget(tab2_label_x2, 1, 1)
        tab2_grid1.addWidget(self.tab2_linedit_x2, 1, 2)
        tab2_grid1.addWidget(tab2_label_y2, 1, 3)
        tab2_grid1.addWidget(self.tab2_linedit_y2, 1, 4)
        tab2_grid1.addWidget(tab2_label3, 2, 0)
        tab2_grid1.addWidget(tab2_label_dx, 2, 1)
        tab2_grid1.addWidget(self.tab2_linedit_dx, 2, 2)
        tab2_grid1.addWidget(tab2_label_dy, 2, 3)
        tab2_grid1.addWidget(self.tab2_linedit_dy, 2, 4)
        self.groupbox_rec.setLayout(tab2_grid1)
        self.groupbox_rec.setVisible(False)
        self.connect(self.tab2_radiobutton1, SIGNAL("clicked()"), self.groupbox_rec.show)
        self.connect(self.tab2_radiobutton2, SIGNAL("clicked()"), self.groupbox_rec.hide)

        grid3 = QGridLayout()
        grid3.addWidget(label10, 0, 0)
        grid3.addWidget(self.tab2_radiobutton1, 0, 1)
        grid3.addWidget(self.groupbox_rec, 0, 2)
        grid3.addWidget(self.tab2_radiobutton2, 1, 1)
        self.tab2groupbox.setLayout(grid3)

    def inputParameters(self):
        self.tab3_listwidget = QListWidget()
        self.tab3_listwidget.insertItem(0, u"非定常变量")
        self.tab3_listwidget.insertItem(1, u"定常输入")

        self.tab3_stack = QStackedWidget()

        tab3_groupbox1 = QGroupBox(u'选择要输入的要素')
        self.tab3_boxes = [QCheckBox(u'地形'), QCheckBox(u'时变'), QComboBox(), QLineEdit(),
                           QCheckBox(u'水位'), QCheckBox(u'时变'), QComboBox(), QLineEdit(),
                           QCheckBox(u'风'), QCheckBox(u'时变'), QComboBox(), QLineEdit(),
                           QCheckBox(u'流'), QCheckBox(u'时变'), QComboBox(), QLineEdit(),
                           QCheckBox(u'摩阻系数'), QCheckBox(u'时变'), QComboBox(), QLineEdit(),
                           QCheckBox(u'植被'), QCheckBox(u'时变'), QComboBox(), QLineEdit()]
        tab3_grid1 = QGridLayout()

        def state_changed():
            for i, box in enumerate(self.tab3_boxes):
                if i % 4 == 0:
                    if box.isChecked():
                        self.tab3_boxes[i + 1].setDisabled(False)
                        self.tab3_boxes[i + 2].setDisabled(False)
                        self.tab3_boxes[i + 3].setDisabled(False)
                    else:
                        self.tab3_boxes[i + 1].setDisabled(True)
                        self.tab3_boxes[i + 2].setDisabled(True)
                        self.tab3_boxes[i + 3].setDisabled(True)

        for i, box in enumerate(self.tab3_boxes):
            if i % 4 == 2:
                box.addItems(["单个文件名", "系列文件名"])
            if i % 4 != 0:
                box.setDisabled(True)
            else:
                box.stateChanged.connect(state_changed)
                # box.toggled.connect(self.tab3_boxes[i + 1].setDisabled)
            tab3_grid1.addWidget(box, i / 4, i % 4)

        tab3_groupbox1.setLayout(tab3_grid1)

        tab3_groupbox2 = QGroupBox(u'时序设置')
        tab3_label1 = QLabel(u'起始时间:')
        tab3_label2 = QLabel(u'终止时间:')
        tab3_label3 = QLabel(u'时间步长:')
        self.tab3_linedit1 = QLineEdit()
        self.tab3_combobox = QComboBox()
        self.tab3_combobox.addItems(['MIn', 'Sec', 'HR'])
        self.tab3_datetime1 = QDateTimeEdit()
        self.tab3_datetime2 = QDateTimeEdit()
        self.tab3_datetime1.setDateTime(QDateTime.currentDateTime())
        self.tab3_datetime2.setDateTime(QDateTime.currentDateTime())

        tab3_grid2 = QGridLayout()
        tab3_grid2.addWidget(tab3_label1, 0, 0)
        tab3_grid2.addWidget(self.tab3_datetime1, 0, 1)
        tab3_grid2.addWidget(tab3_label2, 1, 0)
        tab3_grid2.addWidget(self.tab3_datetime2, 1, 1)
        tab3_grid2.addWidget(tab3_label3, 2, 0)
        tab3_grid2.addWidget(self.tab3_linedit1, 2, 1)
        tab3_grid2.addWidget(self.tab3_combobox, 2, 2)
        tab3_groupbox2.setLayout(tab3_grid2)

        tab3_vbox1 = QVBoxLayout()
        tab3_vbox1.addWidget(tab3_groupbox1)
        tab3_vbox1.addWidget(tab3_groupbox2)
        tab3_group1 = QGroupBox()
        tab3_group1.setLayout(tab3_vbox1)

        tab3_groupbox3 = QGroupBox(u'定常风')
        tab3_label4 = QLabel(u'风速:')
        tab3_label5 = QLabel(u'm/s')
        tab3_label6 = QLabel(u'风向:')
        tab3_label7 = QLabel(u'°')
        self.tab3_linedit2 = QLineEdit()
        self.tab3_linedit3 = QLineEdit()
        tab3_grid3 = QGridLayout()
        tab3_grid3.addWidget(tab3_label4, 0, 0)
        tab3_grid3.addWidget(self.tab3_linedit2, 0, 1)
        tab3_grid3.addWidget(tab3_label5, 0, 2)
        tab3_grid3.addWidget(tab3_label6, 1, 0)
        tab3_grid3.addWidget(self.tab3_linedit3, 1, 1)
        tab3_grid3.addWidget(tab3_label7, 1, 2)
        tab3_groupbox3.setLayout(tab3_grid3)

        tab3_groupbox4 = QGroupBox(u'摩阻系数')
        tab3_label9 = QLabel(u'JONswap:')
        self.tab3_radiobutton1 = QRadioButton(u'恒定')
        self.tab3_radiobutton1.setChecked(True)
        self.tab3_linedit4 = QLineEdit(u'0.0007')
        self.tab3_radiobutton2 = QRadioButton(u'变化')
        self.tab3_radiobutton2.toggled.connect(self.tab3_linedit4.setDisabled)
        tab3_grid4 = QGridLayout()
        tab3_grid4.addWidget(tab3_label9, 0, 0)
        tab3_grid4.addWidget(self.tab3_radiobutton1, 0, 1)
        tab3_grid4.addWidget(self.tab3_linedit4, 0, 2)
        tab3_grid4.addWidget(self.tab3_radiobutton2, 1, 1)
        tab3_groupbox4.setLayout(tab3_grid4)

        tab3_group2 = QGroupBox()
        tab3_vbox2 = QVBoxLayout()
        tab3_vbox2.addWidget(tab3_groupbox3)
        tab3_vbox2.addWidget(tab3_groupbox4)
        tab3_group2.setLayout(tab3_vbox2)

        self.tab3_stack.addWidget(tab3_group1)
        self.tab3_stack.addWidget(tab3_group2)

    def boundarySet(self):
        self.tab4_groupbox1 = QGroupBox()
        self.tab4_groupbox2 = QGroupBox("边界参数")

        tab4_label1 = QLabel("边界谱型:")
        self.tab4_combox1 = QComboBox()
        self.tab4_combox1.addItems(["规则波(BIN)", "Jonswap谱", "PM", "GAUSs"])
        tab4_label2 = QLabel("代表周期:")
        self.tab4_combox2 = QComboBox()
        self.tab4_combox2.addItems(["平均", "谱峰"])
        tab4_gridlayout1 = QGridLayout()
        tab4_gridlayout1.addWidget(tab4_label1, 0, 0)
        tab4_gridlayout1.addWidget(self.tab4_combox1, 0, 1)
        tab4_gridlayout1.addWidget(tab4_label2, 1, 0)
        tab4_gridlayout1.addWidget(self.tab4_combox2, 1, 1)
        self.tab4_groupbox1.setLayout(tab4_gridlayout1)

        tab4_gridlayout2 = QGridLayout()
        self.tab4_radiobutton1 = QRadioButton("规则边界")
        self.tab4_radiobutton2 = QRadioButton("无结构网格")
        self.tab4_radiobutton1.setChecked(True)
        self.tab4_combox2 = QComboBox()
        self.tab4_combox2.addItems(["N", "NW", "W", "SW", "S", "SE", "E", "NE"])
        self.tab4_radiobutton2.toggled.connect(self.tab4_combox2.setDisabled)
        tab4_label0 = QLabel("k:")
        self.tab4_linedit0 = QLineEdit()
        self.tab4_linedit0.setDisabled(True)
        self.tab4_radiobutton1.toggled.connect(self.tab4_linedit0.setDisabled)
        # 定常波参数
        tab4_groupbox4 = QGroupBox("定常波参数")
        tab4_label3 = QLabel("有效波高:")
        self.tab4_linedit1 = QLineEdit()
        tab4_label4 = QLabel("周期:")
        self.tab4_linedit2 = QLineEdit()
        tab4_label5 = QLabel("波向:")
        self.tab4_linedit3 = QLineEdit()
        tab4_label6 = QLabel("方向谱扩散角:")
        self.tab4_spinbox1 = QSpinBox()
        self.tab4_spinbox1.setRange(2, 8)
        tab4_gridlayout3 = QGridLayout()
        tab4_gridlayout3.addWidget(tab4_label3, 0, 0)
        tab4_gridlayout3.addWidget(self.tab4_linedit1, 0, 1)
        tab4_gridlayout3.addWidget(tab4_label4, 0, 2)
        tab4_gridlayout3.addWidget(self.tab4_linedit2, 0, 3)
        tab4_gridlayout3.addWidget(tab4_label5, 1, 0)
        tab4_gridlayout3.addWidget(self.tab4_linedit3, 1, 1)
        tab4_gridlayout3.addWidget(tab4_label6, 1, 2)
        tab4_gridlayout3.addWidget(self.tab4_spinbox1, 1, 3)
        tab4_groupbox4.setLayout(tab4_gridlayout3)
        tab4_gridlayout2.addWidget(self.tab4_radiobutton1, 0, 0)
        tab4_gridlayout2.addWidget(self.tab4_combox2, 0, 1)
        tab4_gridlayout2.setColumnStretch(1, 1)
        tab4_gridlayout2.addWidget(self.tab4_radiobutton2, 0, 2)
        tab4_gridlayout2.addWidget(tab4_label0, 0, 3)
        tab4_gridlayout2.addWidget(self.tab4_linedit0, 0, 4)
        tab4_gridlayout2.addWidget(tab4_groupbox4, 1, 0, 1, 5)
        self.tab4_groupbox2.setLayout(tab4_gridlayout2)

    def source_sink_termSet(self):
        self.tab5_groupbox = QGroupBox()
        tab5_gridlayout1 = QGridLayout()
        tab5_label1 = QLabel("风能输入模式:")
        self.tab5_combox1 = QComboBox()
        self.tab5_combox1.addItems(["KOMen", "JANSsen", "WESTHuysen"])
        tab5_label2 = QLabel("线性增长系数:")
        self.tab5_linedit1 = QLineEdit("0.0015")
        tab5_label3 = QLabel("白帽破碎模式:")
        self.tab5_combox2 = QComboBox()
        self.tab5_combox2.addItems(["KOMen", "JANSsen", "LHIG", "BJ", "KBJ", "AB"])
        self.tab5_checkbox1 = QCheckBox("四波作用")
        self.tab5_checkbox2 = QCheckBox("制约参数")
        self.tab5_checkbox3 = QCheckBox("三波作用")
        self.tab5_checkbox4 = QCheckBox("绕射")
        tab5_label4 = QLabel("极限破波模式")
        self.tab5_combox3 = QComboBox()
        self.tab5_combox3.addItems(["CON", "VAR", "RUE", "TG"])
        self.tab5_checkbox5 = QCheckBox("底摩阻")
        self.tab5_combox4 = QComboBox()
        self.tab5_combox4.addItems(["JONswap", "COLLins", "MADsen"])
        self.tab5_checkbox6 = QCheckBox("波浪增水")

        tab5_groupbox1 = QGroupBox("水生植物影响")
        tab5_label5 = QLabel("高度:")
        self.tab5_linedit2 = QLineEdit()
        tab5_label6 = QLabel("diamtr:")
        self.tab5_linedit3 = QLineEdit()
        tab5_label7 = QLabel("nstems:")
        self.tab5_linedit4 = QLineEdit()
        tab5_label8 = QLabel("拖曳力:")
        self.tab5_linedit5 = QLineEdit()
        tab5_gridlayout2 = QGridLayout()
        tab5_gridlayout2.addWidget(tab5_label5, 0, 0)
        tab5_gridlayout2.addWidget(self.tab5_linedit2, 0, 1)
        tab5_gridlayout2.addWidget(tab5_label6, 0, 2)
        tab5_gridlayout2.addWidget(self.tab5_linedit3, 0, 3)
        tab5_gridlayout2.addWidget(tab5_label8, 1, 0)
        tab5_gridlayout2.addWidget(self.tab5_linedit5, 1, 1)
        tab5_gridlayout2.addWidget(tab5_label7, 1, 2)
        tab5_gridlayout2.addWidget(self.tab5_linedit4, 1, 3)
        tab5_groupbox1.setLayout(tab5_gridlayout2)

        tab5_groupbox2 = QGroupBox("水工建筑物")
        tab5_label9 = QLabel("建筑物数目")
        self.tab5_label10 = QLabel()
        self.tab5_label10.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.obs_num = 0
        self.tab5_label10.setText(str(self.obs_num))
        self.tab5_pushbutton1 = QPushButton("添加")
        self.connect(self.tab5_pushbutton1, SIGNAL("clicked()"), self.addObstacle)
        self.tab5_pushbutton2 = QPushButton("删除")
        self.connect(self.tab5_pushbutton2, SIGNAL("clicked()"), self.deleteObstacle)
        if self.obs_num == 0:
            self.tab5_pushbutton2.setDisabled(True)

        self.obsParams = {}
        first_obs = [QLabel("透浪:"),
                     QLineEdit(),
                     QLabel("反射:"),
                     QLineEdit(),
                     QLabel("X1:"),
                     QLineEdit(),
                     QLabel("Y1:"),
                     QLineEdit(),
                     QLabel("X2:"),
                     QLineEdit(),
                     QLabel("Y2:"),
                     QLineEdit()]
        self.obsParams[str(self.obs_num) + "obs"] = first_obs

        self.tab5_gridlayout3 = QGridLayout()
        self.tab5_gridlayout3.addWidget(tab5_label9, 0, 0)
        self.tab5_gridlayout3.addWidget(self.tab5_label10, 0, 1)
        self.tab5_gridlayout3.addWidget(self.tab5_pushbutton1, 0, 2)
        self.tab5_gridlayout3.addWidget(self.tab5_pushbutton2, 0, 3)

        tab5_groupbox2.setLayout(self.tab5_gridlayout3)

        tab5_gridlayout1.addWidget(tab5_label1, 0, 0)
        tab5_gridlayout1.addWidget(self.tab5_combox1, 0, 1)
        tab5_gridlayout1.addWidget(tab5_label2, 0, 2)
        tab5_gridlayout1.addWidget(self.tab5_linedit1, 0, 3)
        tab5_gridlayout1.addWidget(tab5_label3, 0, 4)
        tab5_gridlayout1.addWidget(self.tab5_combox2, 0, 5)
        tab5_gridlayout1.addWidget(self.tab5_checkbox1, 1, 0)
        tab5_gridlayout1.addWidget(self.tab5_checkbox2, 1, 1)
        tab5_gridlayout1.addWidget(self.tab5_checkbox3, 1, 2)
        tab5_gridlayout1.addWidget(self.tab5_checkbox4, 1, 3)
        tab5_gridlayout1.addWidget(tab5_label4, 2, 0)
        tab5_gridlayout1.addWidget(self.tab5_combox3, 2, 1)
        tab5_gridlayout1.addWidget(self.tab5_checkbox5, 2, 2)
        tab5_gridlayout1.addWidget(self.tab5_combox4, 2, 3)
        tab5_gridlayout1.addWidget(self.tab5_checkbox6, 3, 0)
        tab5_gridlayout1.addWidget(tab5_groupbox1, 4, 0, 1, 6)
        tab5_gridlayout1.addWidget(tab5_groupbox2, 5, 0, 1, 6)

        self.tab5_groupbox.setLayout(tab5_gridlayout1)

    def addObstacle(self):
        self.obs_num += 1
        self.tab5_label10.setText(str(self.obs_num))
        key_name = str(self.obs_num) + "obs"
        self.obsParams[key_name] = [QLabel("透浪:"),
                                    QLineEdit(),
                                    QLabel("反射:"),
                                    QLineEdit(),
                                    QLabel("X1:"),
                                    QLineEdit(),
                                    QLabel("Y1:"),
                                    QLineEdit(),
                                    QLabel("X2:"),
                                    QLineEdit(),
                                    QLabel("Y2:"),
                                    QLineEdit()]
        for i, param_widget in enumerate(self.obsParams[key_name]):
            self.tab5_gridlayout3.addWidget(param_widget, self.obs_num, i)
        if self.obs_num > 0:
            self.tab5_pushbutton2.setDisabled(False)

    def deleteObstacle(self):
        key_name = str(self.obs_num) + "obs"
        for param_widget in self.obsParams[key_name]:
            param_widget.deleteLater()
        self.obs_num -= 1
        self.tab5_label10.setText(str(self.obs_num))
        if self.obs_num <= 0:
            self.tab5_pushbutton2.setDisabled(True)

    def calculateSet(self):
        self.tab6_groupbox = QGroupBox()

        tab6_gridlayout1 = QGridLayout()

        tab6_label1 = QLabel("起算条件:")
        self.tab6_combox1 = QComboBox()
        self.tab6_combox1.addItems(["Default", "Zero", "PAR"])

        self.tab6_radiobutton1 = QRadioButton("BSBT")
        self.tab6_radiobutton2 = QRadioButton("GSE")
        self.tab6_radiobutton2.setChecked(True)
        tab6_label2 = QLabel("波龄:")
        self.tab6_linedit1 = QLineEdit()
        self.tab6_combox2 = QComboBox()
        self.tab6_combox2.addItems(["SEC", "MIN", "HR"])
        self.tab6_radiobutton1.toggled.connect(self.tab6_linedit1.setDisabled)
        self.tab6_radiobutton1.toggled.connect(self.tab6_combox2.setDisabled)

        tab6_label3 = QLabel("计算精度:")
        self.tab6_combox3 = QComboBox()
        self.tab6_combox3.addItems(["ACCUR", "STOPC"])

        self.tab6_radiobutton3 = QRadioButton("恒定")
        self.tab6_radiobutton4 = QRadioButton("非恒定")
        self.tab6_radiobutton4.setChecked(True)
        tab6_label4 = QLabel(u'起始时间:')
        tab6_label5 = QLabel(u'终止时间:')
        tab6_label6 = QLabel(u'时间步长:')
        self.tab6_linedit2 = QLineEdit()
        self.tab6_combox4 = QComboBox()
        self.tab6_combox4.addItems(['MIN', 'SEC', 'HR'])
        self.tab6_datetime1 = QDateTimeEdit()
        self.tab6_datetime2 = QDateTimeEdit()
        self.tab6_datetime1.setDateTime(QDateTime.currentDateTime())
        self.tab6_datetime2.setDateTime(QDateTime.currentDateTime())

        tab6_groupbox1 = QGroupBox("数值模式:")
        tab6_gridlayout2 = QGridLayout()
        tab6_gridlayout2.addWidget(self.tab6_radiobutton1, 0, 0)
        tab6_gridlayout2.addWidget(self.tab6_radiobutton2, 1, 0)
        tab6_gridlayout2.addWidget(tab6_label3, 1, 2)
        tab6_gridlayout2.addWidget(tab6_label2, 1, 3)
        tab6_gridlayout2.addWidget(self.tab6_linedit1, 1, 4)
        tab6_gridlayout2.addWidget(self.tab6_combox2, 1, 5)
        tab6_groupbox1.setLayout(tab6_gridlayout2)

        self.tab6_groupbox2 = QGroupBox()
        tab6_gridlayout3 = QGridLayout()
        tab6_gridlayout3.addWidget(tab6_label4, 0, 0)
        tab6_gridlayout3.addWidget(self.tab6_datetime1, 0, 1)
        tab6_gridlayout3.addWidget(tab6_label5, 1, 0)
        tab6_gridlayout3.addWidget(self.tab6_datetime2, 1, 1)
        tab6_gridlayout3.addWidget(tab6_label6, 2, 0)
        tab6_gridlayout3.addWidget(self.tab6_linedit2, 2, 1)
        tab6_gridlayout3.addWidget(self.tab6_combox4, 2, 2)
        self.tab6_groupbox2.setLayout(tab6_gridlayout3)
        self.tab6_radiobutton3.toggled.connect(self.tab6_groupbox2.setDisabled)

        tab6_groupbox3 = QGroupBox("计算时域及步长:")
        tab6_gridlayout4 = QGridLayout()
        tab6_gridlayout4.addWidget(self.tab6_radiobutton3, 0, 0)
        tab6_gridlayout4.addWidget(self.tab6_radiobutton4, 1, 0)
        tab6_gridlayout4.addWidget(self.tab6_groupbox2, 1, 1, 3, 3)
        tab6_groupbox3.setLayout(tab6_gridlayout4)

        tab6_gridlayout1.addWidget(tab6_label1, 0, 0)
        tab6_gridlayout1.addWidget(self.tab6_combox1, 0, 1)
        tab6_gridlayout1.addWidget(tab6_groupbox1, 1, 0, 2, 3)
        tab6_gridlayout1.addWidget(tab6_label3, 3, 0)
        tab6_gridlayout1.addWidget(self.tab6_combox3, 3, 1)
        tab6_gridlayout1.addWidget(tab6_groupbox3, 4, 0, 3, 4)
        self.tab6_groupbox.setLayout(tab6_gridlayout1)

    def outputSet(self):
        self.tab7_listwidget = QListWidget()
        self.tab7_listwidget.insertItem(0, u"输出点")
        self.tab7_listwidget.insertItem(1, u"输出点变量设置")
        self.tab7_listwidget.insertItem(2, u"输出域")
        self.tab7_listwidget.insertItem(3, u"输出域变量设置")
        self.tab7_listwidget.insertItem(4, u"嵌套输出")
        self.tab7_listwidget.insertItem(5, "输出时间设置")
        self.tab7_stack = QStackedWidget()

        tab7_group1 = QGroupBox("输出点")
        tab7_group2 = QGroupBox("输出点变量设置")
        tab7_group3 = QGroupBox("输出域")
        tab7_group4 = QGroupBox("输出域变量设置")
        tab7_group5 = QGroupBox("嵌套输出")
        tab7_group6 = QGroupBox("输出时间设置")

        # -------------------output points----------------------
        self.tab7_checkbox1 = QCheckBox("读入点位文件")
        self.tab7_pushbutton1 = QPushButton("+")
        self.tab7_pushbutton1.clicked.connect(self.addPointsFiles)
        self.tab7_checkbox2 = QCheckBox("输入点位坐标")
        self.tab7_pushbutton2 = QPushButton("+")
        self.tab7_pushbutton2.clicked.connect(self.addPointsCoordinates)

        self.points_files_num = 1
        self.points1 = {}
        self.points1[str(self.points_files_num)] = [QLabel("点位名:"), QLineEdit(),
                                                    QLabel("点位文件名:"), QLineEdit(),
                                                    QLabel("结果文件名:"), QLineEdit()]
        self.tab7_grid_p1 = QGridLayout()
        for i, widget in enumerate(self.points1[str(self.points_files_num)]):
            self.tab7_grid_p1.addWidget(widget, self.points_files_num - 1, i)
        tab7_groupbox1 = QGroupBox()
        tab7_groupbox1.setLayout(self.tab7_grid_p1)

        self.points_coords_num = 1
        self.points2 = {}
        self.points2[str(self.points_coords_num)] = [QLabel("点位名:"), QLineEdit(),
                                                     QLabel("X:"), QLineEdit(),
                                                     QLabel("Y:"), QLineEdit(),
                                                     QLabel("结果文件名:"), QLineEdit()]
        self.tab7_grid_p2 = QGridLayout()
        for i, widget in enumerate(self.points2[str(self.points_coords_num)]):
            self.tab7_grid_p2.addWidget(widget, self.points_coords_num - 1, i)
        tab7_groupbox2 = QGroupBox()
        tab7_groupbox2.setLayout(self.tab7_grid_p2)

        tab7_grid1 = QGridLayout()
        tab7_grid1.addWidget(self.tab7_checkbox1, 0, 0)
        tab7_grid1.addWidget(self.tab7_pushbutton1, 0, 1)
        tab7_grid1.addWidget(tab7_groupbox1, 1, 0, 1, 2)
        tab7_grid1.addWidget(self.tab7_checkbox2, 2, 0)
        tab7_grid1.addWidget(self.tab7_pushbutton2, 2, 1)
        tab7_grid1.addWidget(tab7_groupbox2, 3, 0, 1, 2)
        tab7_group1.setLayout(tab7_grid1)

        # -------------------output points variables set----------------------
        tab7_grid2 = QGridLayout()
        output_vars = ["HSIGN", "HSWELL", "DIR", "PDIR", "TDIR", "TM01", "RTM01", "RTP", "TM02", "FSPR", "DSPR", "VEL",
                       "FRCOEF", "WIND", "DISSIP", "QB", "TRANSP", "FORCE", "UBOT", "URMS", "WLEN", "STEEPNESS",
                       "DHSIGN", "DRTM01", "LEAK", "TSEC", "XP", "YP", "DIST", "SETUP", "TMM10", "RTMM10", "DEPTH",
                       "TMBOT", "QP", "BFI", "NPLANT", " WATLEV ", "BOTLEV", "TPS", "DISBOT", " DISSURF ", " DISWCAP",
                       "GENE", "GENW", "REDI", "REDQ", "REDT", "PROPA", "PROPX", "PROPT", "PROPS", "RADS", " LWAVP"]
        self.output_points_vars = []
        for i in range(len(output_vars)):
            self.output_points_vars.append(QCheckBox(output_vars[i]))
            # quotient = num // 6
            # remainder = i % 6
            tab7_grid2.addWidget(self.output_points_vars[i], i // 6, i % 6)
        tab7_group2.setLayout(tab7_grid2)

        # -------------------output frame----------------------
        self.tab7_checkbox3 = QCheckBox("矩形域")
        tab7_label2 = QLabel("区域名：")
        self.tab7_linedit2 = QLineEdit()
        tab7_label_m1 = QLabel("左下角坐标:")
        tab7_label_mx1 = QLabel("X1:")
        self.tab7_linedit_mx1 = QLineEdit()
        tab7_label_my1 = QLabel("Y1:")
        self.tab7_linedit_my1 = QLineEdit()
        tab7_label_m2 = QLabel("右上角坐标:")
        tab7_label_mx2 = QLabel("X2:")
        self.tab7_linedit_mx2 = QLineEdit()
        tab7_label_my2 = QLabel("Y2:")
        self.tab7_linedit_my2 = QLineEdit()
        tab7_label_m3 = QLabel("步长:")
        tab7_label_mdx = QLabel("DX:")
        self.tab7_linedit_mdx = QLineEdit()
        tab7_label_mdy = QLabel("DY:")
        self.tab7_linedit_mdy = QLineEdit()
        tab7_grid_f1 = QGridLayout()
        tab7_grid_f1.addWidget(tab7_label_m1, 0, 0)
        tab7_grid_f1.addWidget(tab7_label_mx1, 0, 1)
        tab7_grid_f1.addWidget(self.tab7_linedit_mx1, 0, 2)
        tab7_grid_f1.addWidget(tab7_label_my1, 0, 3)
        tab7_grid_f1.addWidget(self.tab7_linedit_my1, 0, 4)
        tab7_grid_f1.addWidget(tab7_label_m2, 1, 0)
        tab7_grid_f1.addWidget(tab7_label_mx2, 1, 1)
        tab7_grid_f1.addWidget(self.tab7_linedit_mx2, 1, 2)
        tab7_grid_f1.addWidget(tab7_label_my2, 1, 3)
        tab7_grid_f1.addWidget(self.tab7_linedit_my2, 1, 4)
        tab7_grid_f1.addWidget(tab7_label_m3, 2, 0)
        tab7_grid_f1.addWidget(tab7_label_mdx, 2, 1)
        tab7_grid_f1.addWidget(self.tab7_linedit_mdx, 2, 2)
        tab7_grid_f1.addWidget(tab7_label_mdy, 2, 3)
        tab7_grid_f1.addWidget(self.tab7_linedit_mdy, 2, 4)
        tab7_groupbox3 = QGroupBox()
        tab7_groupbox3.setLayout(tab7_grid_f1)

        tab7_label3 = QLabel("输出域结果文件名：")
        self.tab7_linedit3 = QLineEdit()
        tab7_grid3 = QGridLayout()
        tab7_grid3.addWidget(self.tab7_checkbox3, 0, 0)
        tab7_grid3.addWidget(tab7_label2, 1, 0)
        tab7_grid3.addWidget(self.tab7_linedit2, 1, 1)
        tab7_grid3.addWidget(tab7_groupbox3, 2, 0, 1, 3)
        tab7_grid3.addWidget(tab7_label3, 3, 0)
        tab7_grid3.addWidget(self.tab7_linedit3, 3, 1)
        tab7_group3.setLayout(tab7_grid3)

        # -------------------output frame variables set----------------------
        tab7_grid4 = QGridLayout()
        self.output_frame_vars = []
        for i in range(len(output_vars)):
            self.output_frame_vars.append(QCheckBox(output_vars[i]))
            # quotient = num // 6
            # remainder = i % 6
            tab7_grid4.addWidget(self.output_frame_vars[i], i // 6, i % 6)
        tab7_group4.setLayout(tab7_grid4)

        # -------------------output nest----------------------
        self.tab7_checkbox4 = QCheckBox("嵌套输出")
        tab7_label4 = QLabel("嵌套网格名：")
        self.tab7_linedit4 = QLineEdit()
        tab7_label_bx1 = QLabel("X1:")
        tab7_linedit_bx1 = QLineEdit()
        tab7_label_by1 = QLabel("Y1:")
        tab7_linedit_by1 = QLineEdit()
        tab7_label_bx2 = QLabel("X2:")
        tab7_linedit_bx2 = QLineEdit()
        tab7_label_by2 = QLabel("Y2:")
        tab7_linedit_by2 = QLineEdit()
        tab7_label_bdx = QLabel("DX:")
        tab7_linedit_bdx = QLineEdit()
        tab7_label_bdy = QLabel("DY:")
        tab7_linedit_bdy = QLineEdit()
        tab7_grid_g1 = QGridLayout()
        tab7_grid_g1.addWidget(tab7_label_bx1, 0, 0)
        tab7_grid_g1.addWidget(tab7_linedit_bx1, 0, 1)
        tab7_grid_g1.addWidget(tab7_label_by1, 0, 2)
        tab7_grid_g1.addWidget(tab7_linedit_by1, 0, 3)
        tab7_grid_g1.addWidget(tab7_label_bx2, 1, 0)
        tab7_grid_g1.addWidget(tab7_linedit_bx2, 1, 1)
        tab7_grid_g1.addWidget(tab7_label_by2, 1, 2)
        tab7_grid_g1.addWidget(tab7_linedit_by2, 1, 3)
        tab7_grid_g1.addWidget(tab7_label_bdx, 2, 0)
        tab7_grid_g1.addWidget(tab7_linedit_bdx, 2, 1)
        tab7_grid_g1.addWidget(tab7_label_bdy, 2, 2)
        tab7_grid_g1.addWidget(tab7_linedit_bdy, 2, 3)
        tab7_groupbox4 = QGroupBox()
        tab7_groupbox4.setLayout(tab7_grid_g1)

        tab7_label5 = QLabel("嵌套输出结果文件名：")
        self.tab7_linedit5 = QLineEdit()
        tab7_grid5 = QGridLayout()
        tab7_grid5.addWidget(self.tab7_checkbox4, 0, 0)
        tab7_grid5.addWidget(tab7_label4, 1, 0)
        tab7_grid5.addWidget(self.tab7_linedit4, 1, 1)
        tab7_grid5.addWidget(tab7_groupbox4, 2, 0, 1, 3)
        tab7_grid5.addWidget(tab7_label5, 3, 0)
        tab7_grid5.addWidget(self.tab7_linedit5, 3, 1)
        tab7_group5.setLayout(tab7_grid5)

        # -------------------output time set----------------------
        tab7_label_t1 = QLabel(u'起始时间:')
        tab7_label_dt = QLabel(u'时间步长:')
        self.tab7_linedit_bt = QLineEdit()
        self.tab7_combox_b1 = QComboBox()
        self.tab7_combox_b1.addItems(['MIN', 'SEC', 'HR'])
        self.tab7_datetime1 = QDateTimeEdit()
        self.tab7_datetime1.setDateTime(QDateTime.currentDateTime())
        tab7_grid6 = QGridLayout()
        tab7_grid6.addWidget(tab7_label_t1, 0, 0)
        tab7_grid6.addWidget(self.tab7_datetime1, 0, 1)
        tab7_grid6.addWidget(tab7_label_dt, 2, 0)
        tab7_grid6.addWidget(self.tab7_linedit_bt, 2, 1)
        tab7_grid6.addWidget(self.tab7_combox_b1, 2, 2)
        tab7_group6 = QGroupBox()
        tab7_group6.setLayout(tab7_grid6)

        self.tab7_stack.addWidget(tab7_group1)
        self.tab7_stack.addWidget(tab7_group2)
        self.tab7_stack.addWidget(tab7_group3)
        self.tab7_stack.addWidget(tab7_group4)
        self.tab7_stack.addWidget(tab7_group5)
        self.tab7_stack.addWidget(tab7_group6)

    def addPointsFiles(self):
        self.points_files_num += 1
        self.points1[str(self.points_files_num)] = [QLabel("点位名:"), QLineEdit(),
                                                    QLabel("点位文件名:"), QLineEdit(),
                                                    QLabel("结果文件名:"), QLineEdit()]
        for i, widget in enumerate(self.points1[str(self.points_files_num)]):
            self.tab7_grid_p1.addWidget(widget, self.points_files_num - 1, i)

    def addPointsCoordinates(self):
        self.points_coords_num += 1
        self.points2[str(self.points_coords_num)] = [QLabel("点位名:"), QLineEdit(),
                                                     QLabel("X:"), QLineEdit(),
                                                     QLabel("Y:"), QLineEdit(),
                                                     QLabel("结果文件名:"), QLineEdit()]
        for i, widget in enumerate(self.points2[str(self.points_coords_num)]):
            self.tab7_grid_p2.addWidget(widget, self.points_coords_num - 1, i)

    def calculate_input_file(self):
        self.tab8_groupbox = QGroupBox()

        tab8_label1 = QLabel("geo文件名:")
        self.tab8_linedit1 = QLineEdit()

        tab8_label_x1 = QLabel("横坐标范围:")
        self.tab8_linedit_x1 = QLineEdit()
        tab8_label_x2 = QLabel("--")
        self.tab8_linedit_x2 = QLineEdit()
        tab8_label_dx = QLabel("网格尺度:")
        self.tab8_linedit_dx = QLineEdit()
        tab8_label_y1 = QLabel("纵坐标范围:")
        self.tab8_linedit_y1 = QLineEdit()
        tab8_label_y2 = QLabel("--")
        self.tab8_linedit_y2 = QLineEdit()
        tab8_label_dy = QLabel("网格尺度:")
        self.tab8_linedit_dy = QLineEdit()
        tab8_grid1 = QGridLayout()
        tab8_grid1.addWidget(tab8_label_x1, 0, 0)
        tab8_grid1.addWidget(self.tab8_linedit_x1, 0, 1)
        tab8_grid1.addWidget(tab8_label_x2, 0, 2)
        tab8_grid1.addWidget(self.tab8_linedit_x2, 0, 3)
        tab8_grid1.addWidget(tab8_label_dx, 0, 4)
        tab8_grid1.addWidget(self.tab8_linedit_dx, 0, 5)
        tab8_grid1.addWidget(tab8_label_y1, 1, 0)
        tab8_grid1.addWidget(self.tab8_linedit_y1, 1, 1)
        tab8_grid1.addWidget(tab8_label_y2, 1, 2)
        tab8_grid1.addWidget(self.tab8_linedit_y2, 1, 3)
        tab8_grid1.addWidget(tab8_label_dy, 1, 4)
        tab8_grid1.addWidget(self.tab8_linedit_dy, 1, 5)
        tab8_groupbox1 = QGroupBox()
        tab8_groupbox1.setLayout(tab8_grid1)

        tab8_label2 = QLabel("输出文件名：")
        self.tab8_linedit2 = QLineEdit()
        self.conditions = [QLabel("人工岸线数目:"), QLineEdit(), QLabel("文件名:"), QLineEdit(),
                           QLabel("人工港池数目:"), QLineEdit(), QLabel("文件名:"), QLineEdit(),
                           QLabel("边界斜坡宽度:"), QLineEdit(), QLabel("坡度:"), QLineEdit(),
                           QLabel("人工航道数目:"), QLineEdit(), QLabel("文件名:"), QLineEdit(),
                           QLabel("航道边坡宽度:"), QLineEdit(), QLabel("坡度:"), QLineEdit()]

        self.tab8_button1 = QPushButton("生成condition文件")
        self.tab8_button1.clicked.connect(self.conditionFile)
        self.tab8_button2 = QPushButton("运行caldep")
        self.tab8_button2.clicked.connect(self.caldep)

        tab8_grid2 = QGridLayout()
        tab8_grid2.addWidget(tab8_label1, 0, 0)
        tab8_grid2.addWidget(self.tab8_linedit1, 0, 1)
        tab8_grid2.addWidget(tab8_groupbox1, 1, 0, 2, 4)
        tab8_grid2.addWidget(tab8_label2, 3, 0)
        tab8_grid2.addWidget(self.tab8_linedit2, 3, 1)
        for i, con_widget in enumerate(self.conditions):
            tab8_line = i / 4 + 4
            tab8_grid2.addWidget(con_widget, i / 4 + 4, i % 4)
        tab8_grid2.addWidget(self.tab8_button1, tab8_line + 1, 0, 1, 2)
        tab8_grid2.addWidget(self.tab8_button2, tab8_line + 1, 2, 1, 2)
        self.tab8_groupbox.setLayout(tab8_grid2)

    def writeFile(self):
        self.projectline()
        self.setLine()
        self.modeLine()
        self.coordinatesLine()
        self.cgridLine()
        self.inpgridLine()
        self.readinpLine()
        self.windLine()
        self.boundLine()
        self.gen3Line()
        self.functionsStrength()
        self.propLine()
        self.numericLine()
        self.outputLines()
        self.computeLine()
        self.input_lines.append("STOP \n")

    # ************************-----PROJECT-----****************************
    def projectLine(self):
        name = self.tab1_linedit1.text()
        nr = self.tab1_linedit2.text()
        project_line = " ".join(["PROJect", "\'" + name + "\'", "\'" + nr + "\'", "\n"])
        print(project_line)
        self.input_lines.append(project_line)

    # ************************-----SET-----****************************
    def setLine(self):
        level = self.tab1_linedit3.text()
        nor = self.tab1_linedit4.text()
        depmin = '0.05'
        maxmes = '200'
        maxerr = '1'
        grav = '9.81'
        rho = '1025'
        if self.tab1_checkbox.isChecked():
            cdcap = '2.5e-3'
        else:
            cdcap = '99999'
        if self.tab1_combobox1.currentIndex():
            inrhog = '1'
        else:
            inrhog = '0'
        # hsrerr = '0.10'
        convention = 'CARTesian'
        pwtail = '4'
        froudmax = '0.8'
        printf = '4'
        prtest = '4'
        set_line = " ".join(['SET', level, nor, depmin, maxmes, maxerr, grav, rho,
                             cdcap, inrhog, convention, pwtail, froudmax, printf, prtest, "\n"])
        # print(set_line)
        self.input_lines.append(set_line)

    # ************************-----MODE-----****************************
    def modeLine(self):
        if self.tab1_combobox2.currentIndex():
            mode = 'NONSTATionary'
        else:
            mode = 'STATionary'
        dimension = 'TWODimensional'
        mode_line = " ".join(["MODE", mode, dimension, "\n"])
        print(mode_line)
        self.input_lines.append(mode_line)

    # ************************-----COORDINATES-----****************************
    def coordinatesLine(self):
        coordinate_index = self.tab1_combobox3.currentIndex()
        if coordinate_index is 0:
            coordinate = 'CARTesian'
        elif coordinate_index is 1:
            coordinate = 'SPHErical CCM'
        else:
            coordinate = 'SPHErical QC'
        coordinate_line = " ".join(["COORDINATES", coordinate, "\n"])
        print(coordinate_line)
        self.input_lines.append(coordinate_line)

    # ************************-----CGRID-----****************************
    def cgridLine(self):
        if self.tab2_radiobutton2.isChecked():
            shape = 'UNSTRUCtured CIRcle'
        if self.tab2_radiobutton1.isChecked():
            shape = 'REGular'
            xpc = self.tab2_linedit_x1.text()
            ypc = self.tab2_linedit_y1.text()
            alpc = '0.0'
            cx2 = int(self.tab2_linedit_x2)
            cy2 = int(self.tab2_linedit_y2)
            cdx = int(self.tab2_linedit_dx)
            cdy = int(self.tab2_linedit_dy)
            xlenc = str(cx2 - int(xpc))
            ylenc = str(cy2 - int(ypc))
            mxc = str((cx2 - int(xpc)) / cdx)
            myc = str((cy2 - int(ypc)) / cdy)
            shape = " ".join(["REGular", xpc, ypc, alpc, xlenc, ylenc, mxc, myc, "CIRcle"])
        mdc = '36'
        flow = '0.04'
        fhigh = '2'
        cgrid_line = " ".join(["CGRID", shape, mdc, flow, fhigh, "\n"])
        self.input_lines.append(cgrid_line)

        # ************************-----READgrid-----****************************
        readgrid_line = " ".join(["READgrid", "UNSTRUCtured", "ADCirc", "\n"])
        self.input_lines.append(readgrid_line)

    # ************************-----INPgrid-----****************************
    def inpgridLine(self):
        tbeginp = self.tab3_datetime1.dateTime().toString("yyyyMMdd.hhmmss")
        deltinp = self.tab3_linedit1.text()
        tendinp = self.tab3_datetime2.dateTime().toString("yyyyMMdd.hhmmss")
        time_unit0 = self.tab3_combobox.currentText()
        self.factors = ["BOTtom", "WLEVel", "CURrent", "FRiction", "WInd", "NPLAnts"]
        for i, box in enumerate(self.tab3_boxes):
            if i % 4 == 0:
                if box.isChecked():
                    factor = self.factors[int(i / 4)]
                    if self.tab3_boxes[i + 1].isChecked():
                        inpgrid_line = " ".join(
                            ["INPgrid", factor, "UNSTRUC NONSTAT", tbeginp, deltinp, time_unit0, tendinp, "\n"])
                    else:
                        inpgrid_line = " ".join(["INPgrid", factor, "UNSTRUC\n"])
                    self.input_lines.append(inpgrid_line)

    # ************************-----READinp-----****************************
    def readinpLine(self):
        for j, box in enumerate(self.tab3_boxes):
            if j % 4 == 0:
                if box.isChecked():
                    factor = self.factors[int(j / 4)]
                    fname = "\'" + self.tab3_boxes[j + 3].text() + "\'"
                    if self.tab3_boxes[j + 2].currentIndex():
                        readinp_line = " ".join(["READinp", factor, "SERIes", fname, "\n"])
                    else:
                        readinp_line = " ".join(["READinp", factor, fname, "\n"])
                    self.input_lines.append(readinp_line)

    # ************************-----WIND-----****************************
    def windLine(self):
        vel = self.tab3_linedit2.text()
        dir_ = self.tab3_linedit3.text()
        wind_line = " ".join(["WIND", vel, dir_, "\n"])
        self.input_lines.append(wind_line)

    # ************************-----BOUNd SHAPespec-----****************************
    def boundLine(self):
        if self.tab4_combox1.currentIndex() is 0:
            spectrum = 'BIN'
        elif self.tab4_combox1.currentText() is 1:
            spectrum = 'IONswap 3.3'
        elif self.tab4_combox1.currentIndex() is 2:
            spectrum = 'PM'
        else:
            spectrum = 'GAUSs 0'
        if self.tab4_combox2.currentIndex():
            wave_period = 'PEAK'
        else:
            wave_period = 'MEAN'
        bound_shapespec_line = " ".join(["BOUND SHAPespec", spectrum, wave_period, "DSPR POWER", "\n"])
        self.input_lines.append(bound_shapespec_line)

        # ************************-----BOUNdspec-----****************************
        hs = self.tab4_linedit1.text()
        per = self.tab4_linedit2.text()
        dir = self.tab4_linedit3.text()
        dd = self.tab4_spinbox1.text()
        if self.tab4_radiobutton1.isChecked():
            side = self.tab4_combox1.currentText()
            if hs and per and dir and dd:
                boundspec_line = " ".join(["BOUNspec SIDE", side, "CONstant PAR", hs, per, dir, dd, "\n"])
            else:
                boundspec_line = " ".join(["!BOUNspec", "\n"])
        else:
            side = self.tab4_linedit0.text()
            boundspec_line = " ".join(["BOUNspec SIDE", side, "\n"])
        self.input_lines.append(boundspec_line)

        # ************************-----INITial-----****************************
        if self.tab6_combox1.currentIndex() is 0:
            initial = 'DAEFault'
        elif self.tab6_combox1.currentIndex() is 1:
            initial = 'ZERO'
        else:
            initial = " ".join(["PAR", hs, per, dir, dd])
        initial_line = " ".join(["INITial", initial, "\n"])
        self.input_lines.append(initial_line)

    # ************************-----GEN3-----****************************
    def gen3Line(self):
        cds1 = '4.5'
        delta = '0.5'
        cds2 = '2.36e-5'
        stpm = '3.02e-3'
        a = self.tab5_linedit1.text()
        if self.tab5_combox1.currentIndex() is 0:
            wind_input_mode = " ".join(["KOMen", cds2, stpm])
        elif self.tab5_combox1.currentIndex() is 1:
            wind_input_mode = " ".join(["JANSsen", cds1, delta])
        else:
            wind_input_mode = " ".join(["JANSsen", cds1, delta])
        gen3_line = " ".join(["GEN3", wind_input_mode, "AGROW", a, "\n"])
        self.input_lines.append(gen3_line)

    def functionsStrength(self):
        # ************************-----WCAP-----****************************
        wcap_line = " ".join(["WCAP", self.tab5_combox2.currentText(), "\n"])
        self.input_lines.append(wcap_line)

        # ************************-----QUADrupl-----****************************
        if self.tab5_checkbox1.isChecked():
            quadrupl_line = 'QUADrupl \n'
        else:
            quadrupl_line = '!QUADrupl \n'
        self.input_lines.append(quadrupl_line)

        # ************************-----BREaking-----****************************
        breaking_line = " ".join(["BREaking", self.tab5_combox3.currentText(), "\n"])
        self.input_lines.append(breaking_line)

        # ************************-----FRICtion-----****************************
        if self.tab5_checkbox5.isChecked():
            if self.tab5_combox4.currentText() is "JONswap":
                if self.tab3_radiobutton1.isChecked():
                    cfjon = self.tab3_linedit4.text()
                    friction_line = " ".join(["FRICtion JONswap", "CONstant", cfjon, "\n"])
                elif self.tab3_radiobutton2.isChecked():
                    friction_line = " ".join(["FRICtion JONswap VARiable\n"])
                else:
                    friction_line = ""
            elif self.tab5_combox4.currentText() is "COLLins":
                friction_line = " ".join(["FRICtion COLLins 0.015 \n"])
            else:
                friction_line = " ".join(["FRICtion MADsen 0.05 \n"])
        else:
            friction_line = " ".join(["!FRICtion \n"])
        self.input_lines.append(friction_line)

        # ************************-----TRIad-----****************************
        if self.tab5_checkbox3.isChecked():
            triad_line = 'TRIad \n'
        else:
            triad_line = '!TRIad \n'
        self.input_lines.append(triad_line)

        # ************************-----VEGEtation-----****************************
        height = self.tab5_linedit2.text()
        diamtr = self.tab5_linedit3.text()
        nstems = self.tab5_linedit4.text()
        drag = self.tab5_linedit5.text()
        if height and diamtr and nstems and drag:
            vegetation_line = " ".join(["VEGEtation", height, diamtr, nstems, drag])
        else:
            vegetation_line = "!VEGEtation \n"
        self.input_lines.append(vegetation_line)

        # ************************-----LIMiter-----****************************
        if self.tab5_checkbox2.isChecked():
            limiter_line = 'LIMiter \n'
        else:
            limiter_line = '!LIMiter \n'
        self.input_lines.append(limiter_line)

        # ************************-----OBSTacle-----****************************
        if self.obs_num == 0:
            obstacle_line = "!OBSTacle"
            self.input_lines.append(obstacle_line)
        else:
            for i in range(self.obs_num):
                _key_name = str(i + 1) + "obs"
                trcoef = self.obsParams[_key_name][1].text()
                reflc = self.obsParams[_key_name][3].text()
                obs_x1 = self.obsParams[_key_name][5].text()
                obs_y1 = self.obsParams[_key_name][7].text()
                obs_x2 = self.obsParams[_key_name][9].text()
                obs_y2 = self.obsParams[_key_name][11].text()
                if reflc:
                    obstacle_line = " ".join(["OBSTacle TRANSm", trcoef, "REFL", reflc, "RSPEC LINE",
                                              obs_x1, obs_y1, obs_x2, obs_y2, "\n"])
                else:
                    obstacle_line = " ".join(["OBSTacle TRANSm", trcoef, "LINE",
                                              obs_x1, obs_y1, obs_x2, obs_y2, "\n"])
                self.input_lines.append(obstacle_line)

        # ************************-----SETUP-----****************************
        if self.tab5_checkbox6.isChecked():
            setup_line = "SETUP"
            self.input_lines.append(setup_line)

        # ************************-----DIFFRACtion-----****************************
        if self.tab5_checkbox4.isChecked():
            diffraction_line = " ".join(["DIFFRACtion 1 0 0 1\n"])
        else:
            diffraction_line = " ".join(["!DIFFRACtion\n"])
        self.input_lines.append(diffraction_line)

    # ************************-----PROP-----****************************
    def propLine(self):
        if self.tab6_radiobutton1.isChecked():
            prop_line = "PROP BSBT\n"
        elif self.tab6_radiobutton2.isChecked():
            waveage = self.tab6_linedit1.text()
            time_unit1 = self.tab6_combox2.currentText()
            prop_line = " ".join(["PROP GSE", waveage, time_unit1, "\n"])
        else:
            prop_line = "!PROP"
        self.input_lines.append(prop_line)

    # ************************-----NUMeric-----****************************
    def numericLine(self):
        if self.tab6_combox3.currentIndex():
            numeric_line = "NUMeric STOPC\n"
        else:
            numeric_line = "NUMeric ACCUR\n"
        self.input_lines.append(numeric_line)

    # ************************-----FRAME-----****************************
    def outputLines(self):
        if self.tab7_checkbox3.isChecked():
            xpfr = self.tab7_linedit_mx1.text()
            ypfr = self.tab7_linedit_my1.text()
            fx2 = int(self.tab7_linedit_mx2.text())
            fy2 = int(self.tab7_linedit_my2.text())
            fdx = int(self.tab7_linedit_mdx.text())
            fdy = int(self.tab7_linedit_mdy.text())
            alpfr = '0'
            xlenfr = str(fx2 - int(xpfr))
            ylenfr = str(fy2 - int(ypfr))
            mxfr = str((fx2 - int(xpfr)) / fdx)
            myfr = str((fy2 - int(ypfr)) / fdy)
            f_sname = "\'" + self.tab7_linedit2.text() + "\'"
            frame_line = " ".join(["FRAME", f_sname, xpfr, ypfr, alpfr, xlenfr, ylenfr, mxfr, myfr, "\n"])
            self.input_lines.append(frame_line)

        # ************************-----POINTS-----****************************
        if self.tab7_checkbox1.isChecked():
            for i in range(self.points_files_num):
                if self.points1[str(i + 1)][3].text():
                    p1_sname = "\'" + self.points1[str(i + 1)][1].text() + "\'"
                    p1_fname = "\'" + self.points1[str(i + 1)][3].text() + "\'"
                    points_line = " ".join(["POINTS", p1_sname, "FILE", p1_fname, "\n"])
                    self.input_lines.append(points_line)
        if self.tab7_checkbox2.isChecked():
            for i in range(self.points_coords_num):
                points_x = self.points2[str(i + 1)][3].text()
                points_y = self.points2[str(i + 1)][5].text()
                if points_x and points_y:
                    p2_sname = "\'" + self.points2[str(i + 1)][1].text() + "\'"
                    points_line = " ".join(["POINTS", p2_sname, points_x, points_y, "\n"])
                    self.input_lines.append(points_line)

        # ************************-----NGRID-----****************************
        if self.tab7_checkbox4.isChecked():
            g_sname = "\'" + self.tab7_linedit4.text() + "\'"
            xpn = self.tab7_linedit_bx1.text()
            ypn = self.tab7_linedit_by1.text()
            nx2 = int(self.tab7_linedit_bx2.text())
            ny2 = int(self.tab7_linedit_by2.text())
            ndx = int(self.tab7_linedit_bdx.text())
            ndy = int(self.tab7_linedit_bdy.text())
            alpn = '0'
            xlenn = str(nx2 - int(xpn))
            ylenn = str(ny2 - int(ypn))
            mxn = str((nx2 - int(xpn)) / ndx)
            myn = str((ny2 - int(ypn)) / ndy)
            frame_line = " ".join(["FRAME", g_sname, xpn, ypn, alpn, xlenn, ylenn, mxn, myn, "\n"])
            self.input_lines.append(frame_line)

        tbegtbl = self.tab7_datetime1.dateTime().toString("yyyyMMdd.hhmmss")
        delttbl = self.tab7_linedit_bt.text()
        time_unit3 = self.tab7_combox_b1.currentText()

        # ************************-----TABLE-----****************************
        vars_1 = ""
        for checkbox in self.output_frame_vars:
            if checkbox.isChecked():
                vars_1 = " ".join([vars_1, checkbox])
        if self.tab7_checkbox3.isChecked():
            f_fname = "\'" + self.tab7_linedit3.text() + "\'"
            table_line1 = " ".join(
                ["TABLE", f_sname, "INDEXED", f_fname, vars_1, "OUTPUT", tbegtbl, delttbl, time_unit3, "\n"])
            self.input_lines.append(table_line1)

        vars_2 = ""
        for checkbox in self.output_points_vars:
            if checkbox.isChecked():
                vars_2 = " ".join([vars_2, checkbox])
        if self.tab7_checkbox1.isChecked():
            for i in range(self.points_files_num):
                if self.points1[str(i + 1)][3].text():
                    p1_ffname = "\'" + self.points1[str(i + 1)][5].text() + "\'"
                    table_line2 = " ".join(["TABLE", p1_sname, "INDEXED", p1_ffname,
                                            vars_2, "OUTPUT", tbegtbl, delttbl, time_unit3, "\n"])
                    self.input_lines.append(table_line2)
        if self.tab7_checkbox2.isChecked():
            for i in range(self.points_coords_num):
                p2_ffname = "\'" + self.points2[str(i + 1)][7].text() + "\'"
                table_line2 = " ".join(["TABLE", p2_sname, "INDEXED", p2_ffname,
                                        vars_2, "OUTPUT", tbegtbl, delttbl, time_unit3, "\n"])
                self.input_lines.append(table_line2)

        # ************************-----NESTout-----****************************
        if self.tab7_checkbox4.isChecked():
            g_fname = "\'" + self.tab7_linedit5.text() + "\'"
            nestout_line = " ".join(["NESTout", g_sname, "INDEXED", g_fname,
                                     "OUTPUT", tbegtbl, delttbl, time_unit3, "\n"])

            self.input_lines.append(nestout_line)

    # ************************-----COMPute-----****************************
    def computeLine(self):
        if self.tab6_radiobutton3.isChecked():
            mode = 'STATionary'
            compute_line = " ".join(["COMPute", mode, "\n"])
        elif self.tab6_radiobutton4.isChecked():
            mode = 'NONSTATionary'
            tbegc = self.tab6_datetime1.dateTime().toString("yyyyMMdd.hhmmss")
            # print(tbegc)
            deltc = self.tab6_linedit2.text()
            tendc = self.tab6_datetime2.dateTime().toString("yyyyMMdd.hhmmss")
            time_unit2 = self.tab6_combox4.currentText()
            compute_line = " ".join(["COMPute", mode, tbegc, deltc, time_unit2, tendc, "\n"])
        else:
            compute_line = "!COMPute"
        self.input_lines.append(compute_line)

        with open("input", 'w') as f_out:
            f_out.writelines(self.input_lines)

    def conditionFile(self):
        condition_lines = []
        line1 = " ".join(["读取的原始geo文件名：", self.tab8_linedit1.text(), "\n"])
        line2 = " ".join(["横坐标范围：", self.tab8_linedit_x1.text(), self.tab8_linedit_x2.text(), "\n"])
        line3 = " ".join(["横坐标网格尺度：", self.tab8_linedit_dx.text(), "\n"])
        line4 = " ".join(["纵坐标范围：", self.tab8_linedit_y1.text(), self.tab8_linedit_y2.text(), "\n"])
        line5 = " ".join(["纵坐标网格尺度：", self.tab8_linedit_dy.text(), "\n"])
        line6 = " ".join(["生成的文件名：", self.tab8_linedit2.text(), "\n"])
        line7 = " ".join(["封闭岸线数目：", self.conditions[1].text(), "\n"])
        line8 = " ".join(["岸线文件名：", self.conditions[3].text(), "\n"])
        line9 = " ".join(["封闭港池数目：", self.conditions[5].text(), "\n"])
        line10 = " ".join(["港池文件名：", self.conditions[7].text(), "\n"])
        line11 = " ".join(["港池边界人工变宽宽度及坡比：", self.conditions[9].text(), self.conditions[11].text(), "\n"])
        line12 = " ".join(["封闭港池数目：", self.conditions[13].text(), "\n"])
        line13 = " ".join(["港池文件名：", self.conditions[15].text(), "\n"])
        line14 = " ".join(["港池边界人工变宽宽度及坡比：", self.conditions[17].text(), self.conditions[19].text(), "\n"])
        all_lines = [line1, line2, line3, line4, line5, line6, line7,
                     line8, line9, line10, line11, line12, line13, line14]
        for line in all_lines:
            condition_lines.append(line)

        filename = "condition.dat"
        with open(filename, 'w') as ff_out:
            ff_out.writelines(condition_lines)

    def caldep(self):
        from subprocess import call

        cur_dir = os.getcwd()
        # _dir = os.path.join(cur_dir, 'CAL_DEP')
        cmdline = "caldep.exe"
        call("start cmd /K " + cmdline, cwd=cur_dir, shell=True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    s = Swan()
    s.show()
    sys.exit(app.exec_())
