# -*- coding: utf-8 -*-

import sys
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
        tab3hbox = QHBoxLayout()
        tab3hbox.addWidget(self.tab3listwidget)
        tab3hbox.addWidget(self.tab3stack)
        tab3.setLayout(tab3hbox)
        self.connect(self.tab3listwidget, SIGNAL("currentRowChanged(int)"), self.tab3stack,
                     SLOT("setCurrentIndex(int)"))

        self.boundarySet()
        tab4_hbox = QHBoxLayout()
        tab4_hbox.addWidget(self.tab4_groupbox1)
        tab4_hbox.addWidget(self.tab4_groupbox2)
        tab4_hbox.addWidget(self.tab4_groupbox3)
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
        label11 = QLabel(u'起始点')
        label12 = QLabel(u'终点')
        label13 = QLabel(u'步长')
        x0 = QLabel('x0')
        y0 = QLabel('y0')
        x1 = QLabel('x1')
        y1 = QLabel('y1')
        dx = QLabel('dx')
        dy = QLabel('dy')
        linedit5 = QLineEdit()
        linedit6 = QLineEdit()
        linedit7 = QLineEdit()
        linedit8 = QLineEdit()
        linedit9 = QLineEdit()
        linedit10 = QLineEdit()
        grid2 = QGridLayout()
        grid2.addWidget(x0, 0, 1)
        grid2.addWidget(y0, 0, 2)
        grid2.addWidget(label11, 1, 0)
        grid2.addWidget(linedit5, 1, 1)
        grid2.addWidget(linedit6, 1, 2)
        grid2.addWidget(x1, 2, 1)
        grid2.addWidget(y1, 2, 2)
        grid2.addWidget(label12, 3, 0)
        grid2.addWidget(linedit7, 3, 1)
        grid2.addWidget(linedit8, 3, 2)
        grid2.addWidget(dx, 4, 1)
        grid2.addWidget(dy, 4, 2)
        grid2.addWidget(label13, 5, 0)
        grid2.addWidget(linedit9, 5, 1)
        grid2.addWidget(linedit10, 5, 2)
        self.groupbox_rec.setLayout(grid2)
        self.groupbox_rec.setVisible(False)
        # if self.radiobutton1.isChecked():
        #     self.groupbox_rec.setVisible(True)
        self.connect(self.tab2_radiobutton1, SIGNAL("clicked()"), self.groupbox_rec.show)
        self.connect(self.tab2_radiobutton2, SIGNAL("clicked()"), self.groupbox_rec.hide)

        grid3 = QGridLayout()
        grid3.addWidget(label10, 0, 0)
        grid3.addWidget(self.tab2_radiobutton1, 0, 1)
        grid3.addWidget(self.groupbox_rec, 0, 2)
        grid3.addWidget(self.tab2_radiobutton2, 1, 1)
        self.tab2groupbox.setLayout(grid3)

    def inputParameters(self):
        self.tab3listwidget = QListWidget()
        self.tab3listwidget.insertItem(0, u"非定常变量")
        self.tab3listwidget.insertItem(1, u"定常输入")

        self.tab3stack = QStackedWidget()

        tab3table = QTableWidget(7, 2)
        index1 = QLabel(u'要素')
        self.tab3_checkbox1 = QCheckBox(u'地形')
        self.tab3_checkbox2 = QCheckBox(u'水位')
        self.tab3_checkbox3 = QCheckBox(u'风')
        self.tab3_checkbox4 = QCheckBox(u'流')
        self.tab3_checkbox5 = QCheckBox(u'摩阻系数')
        self.tab3_checkbox6 = QCheckBox(u'植被')
        boxes1 = [index1, self.tab3_checkbox1, self.tab3_checkbox2, self.tab3_checkbox3,
                  self.tab3_checkbox4, self.tab3_checkbox5, self.tab3_checkbox6]
        for i, box in enumerate(boxes1):
            tab3table.setCellWidget(i, 0, box)
        index2 = QLabel(u'时变')
        tab3table.setCellWidget(0, 1, index2)
        for i in range(1, 7):
            checkbox7 = QCheckBox(u'是')
            tab3table.setCellWidget(i, 1, checkbox7)

        tab3groupbox = QGroupBox()
        index3 = QLabel(u'时序设置')
        index4 = QLabel(u'选择文件')
        tab3label1 = QLabel(u'起始时间:')
        tab3label2 = QLabel(u'终止时间:')
        tab3label5 = QLabel(u'时间步长:')
        tab3linedit1 = QLineEdit()
        tab3combobox = QComboBox()
        tab3combobox.addItems(['min', 'sec', 'hr'])
        self.tab3datetime1 = QDateTimeEdit()
        self.tab3datetime2 = QDateTimeEdit()
        self.tab3datetime1.setDateTime(QDateTime.currentDateTime())
        self.tab3datetime2.setDateTime(QDateTime.currentDateTime())
        tab3button1 = QPushButton(u'读入地形')
        tab3button2 = QPushButton(u'读入风场')

        gridlayout = QGridLayout()
        gridlayout.addWidget(index3, 0, 0)
        gridlayout.addWidget(tab3label1, 1, 0)
        gridlayout.addWidget(self.tab3datetime1, 1, 1)
        gridlayout.addWidget(tab3label2, 2, 0)
        gridlayout.addWidget(self.tab3datetime2, 2, 1)
        gridlayout.addWidget(tab3label5, 3, 0)
        gridlayout.addWidget(tab3linedit1, 3, 1)
        gridlayout.addWidget(tab3combobox, 3, 2)
        gridlayout.addWidget(index4, 0, 3)
        gridlayout.addWidget(tab3button1, 1, 3)
        gridlayout.addWidget(tab3button2, 2, 3)
        tab3groupbox.setLayout(gridlayout)

        hbox = QHBoxLayout()
        hbox.addWidget(tab3table)
        hbox.addWidget(tab3groupbox)

        tab3groupbox2 = QGroupBox()
        tab3groupbox2.setLayout(hbox)

        tab3groupbox3 = QGroupBox()

        tab3label6 = QLabel(u'定常风')
        tab3label7 = QLabel(u'风速:')
        tab3label8 = QLabel(u'm/s')
        tab3label9 = QLabel(u'风向:')
        tab3label10 = QLabel(u'°')
        tab3label11 = QLabel(u'拖曳力系数:')
        self.tab3_linedit2 = QLineEdit()
        self.tab3_linedit3 = QLineEdit()
        tab3linedit4 = QLineEdit(u'0.0015')
        tab3label12 = QLabel(u'摩阻系数')
        tab3label13 = QLabel(u'JONswap')
        tab3radiobutton1 = QRadioButton(u'恒定')
        tab3radiobutton1.setChecked(True)
        self.tab3linedit5 = QLineEdit(u'0.0007')
        tab3radiobutton2 = QRadioButton(u'变化')
        tab3radiobutton2.toggled.connect(self.tab3linedit5.setDisabled)

        gridlayout2 = QGridLayout()
        gridlayout2.addWidget(tab3label6, 0, 0)
        gridlayout2.addWidget(tab3label7, 1, 0)
        gridlayout2.addWidget(self.tab3_linedit2, 1, 1)
        gridlayout2.addWidget(tab3label8, 1, 2)
        gridlayout2.addWidget(tab3label9, 2, 0)
        gridlayout2.addWidget(self.tab3_linedit3, 2, 1)
        gridlayout2.addWidget(tab3label10, 2, 2)
        gridlayout2.addWidget(tab3label11, 3, 0)
        gridlayout2.addWidget(tab3linedit4, 3, 1)
        gridlayout2.addWidget(tab3label12, 4, 0)
        gridlayout2.addWidget(tab3label13, 5, 0)
        gridlayout2.addWidget(tab3radiobutton1, 5, 1)
        gridlayout2.addWidget(self.tab3linedit5, 5, 2)
        gridlayout2.addWidget(tab3radiobutton2, 6, 1)
        tab3groupbox3.setLayout(gridlayout2)

        self.tab3stack.addWidget(tab3groupbox2)
        self.tab3stack.addWidget(tab3groupbox3)

    def boundarySet(self):
        self.tab4_groupbox1 = QGroupBox()
        self.tab4_groupbox2 = QGroupBox("边界参数")
        self.tab4_groupbox3 = QGroupBox("嵌入边界")

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

        tab4_button1 = QPushButton("读入边界文件")
        tab4_vbox1 = QVBoxLayout()
        tab4_vbox1.addWidget(tab4_button1)
        self.tab4_groupbox3.setLayout(tab4_vbox1)

    def source_sink_termSet(self):
        self.tab5_groupbox = QGroupBox()
        tab5_gridlayout1 = QGridLayout()
        # (["风浪模式","波浪作用","其他","水生植物影响","水工建筑物"])
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

        tab5_groupbox1 = QGroupBox("水生植物影响")
        tab5_label5 = QLabel("高度:")
        self.tab5_linedit2 = QLineEdit()
        tab5_label6 = QLabel("diamtr:")
        self.tab5_linedit3 = QLineEdit()
        tab5_label7 = QLabel("nstems:")
        self.tab5_linedit4 = QLineEdit()
        tab5_label8 = QLabel("拖曳力:")
        self.tab5_linedit5 = QLineEdit()
        self.tab5_checkbox6 = QCheckBox("波浪增水")
        tab5_gridlayout2 = QGridLayout()
        tab5_gridlayout2.addWidget(tab5_label5, 0, 0)
        tab5_gridlayout2.addWidget(self.tab5_linedit2, 0, 1)
        tab5_gridlayout2.addWidget(tab5_label6, 0, 2)
        tab5_gridlayout2.addWidget(self.tab5_linedit3, 0, 3)
        tab5_gridlayout2.addWidget(tab5_label7, 0, 4)
        tab5_gridlayout2.addWidget(self.tab5_linedit4, 0, 5)
        tab5_gridlayout2.addWidget(tab5_label8, 1, 0)
        tab5_gridlayout2.addWidget(self.tab5_linedit5, 1, 1)
        tab5_gridlayout2.addWidget(self.tab5_checkbox6, 1, 2)
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
        tab5_gridlayout1.addWidget(tab5_groupbox1, 3, 0, 1, 6)
        tab5_gridlayout1.addWidget(tab5_groupbox2, 4, 0, 1, 6)

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
        self.tab7_listwidget.insertItem(1, u"输出域")
        self.tab7_listwidget.insertItem(2, u"输出变量")
        self.tab7_listwidget.insertItem(3, u"嵌套输出")
        self.tab7_stack = QStackedWidget()

        tab7_left_groupbox = QGroupBox("输出点")
        tab7_mid_groupbox = QGroupBox("输出域")
        tab7_right_groupbox = QGroupBox("输出变量")

        self.tab7_checkbox1 = QCheckBox("读入点位文件")
        self.tab7_pushbutton1 = QPushButton("+")
        self.tab7_pushbutton1.clicked.connect(self.addPointsFiles)
        self.tab7_checkbox2 = QCheckBox("输入点位坐标")
        self.tab7_pushbutton2 = QPushButton("+")
        self.tab7_pushbutton2.clicked.connect(self.addPointsCoordinates)

        self.points_files_num = 1
        self.points1 = {}
        self.points1[str(self.points_files_num)] = [QLabel("点位名:"),
                                                    QLineEdit(),
                                                    QLabel("点位文件名:"),
                                                    QLineEdit()]
        self.tab7_grid1 = QGridLayout()
        for i, widget in enumerate(self.points1[str(self.points_files_num)]):
            self.tab7_grid1.addWidget(widget, self.points_files_num - 1, i)
        tab7_groupbox1 = QGroupBox()
        tab7_groupbox1.setLayout(self.tab7_grid1)

        self.points_coords_num = 1
        self.points2 = {}
        self.points2[str(self.points_coords_num)] = [QLabel("点位名:"),
                                                     QLineEdit(),
                                                     QLabel("X:"),
                                                     QLineEdit(),
                                                     QLabel("Y:"),
                                                     QLineEdit()]
        self.tab7_grid2 = QGridLayout()
        for i, widget in enumerate(self.points2[str(self.points_coords_num)]):
            self.tab7_grid2.addWidget(widget, self.points_coords_num - 1, i)
        tab7_groupbox2 = QGroupBox()
        tab7_groupbox2.setLayout(self.tab7_grid2)

        tab7_1_grid = QGridLayout()
        tab7_1_grid.addWidget(self.tab7_checkbox1, 0, 0)
        tab7_1_grid.addWidget(self.tab7_pushbutton1, 0, 1)
        tab7_1_grid.addWidget(tab7_groupbox1, 1, 0, 1, 2)
        tab7_1_grid.addWidget(self.tab7_checkbox2, 2, 0)
        tab7_1_grid.addWidget(self.tab7_pushbutton2, 2, 1)
        tab7_1_grid.addWidget(tab7_groupbox2, 3, 0, 1, 2)
        tab7_left_groupbox.setLayout(tab7_1_grid)

        tab7_checkbox8 = QCheckBox("矩形域")
        tab7_label_m1 = QLabel("左下角坐标:")
        tab7_label_mx1 = QLabel("X1:")
        tab7_linedit_mx1 = QLineEdit()
        tab7_label_my1 = QLabel("Y1:")
        tab7_linedit_my1 = QLineEdit()
        tab7_label_m2 = QLabel("右上角坐标:")
        tab7_label_mx2 = QLabel("X2:")
        tab7_linedit_mx2 = QLineEdit()
        tab7_label_my2 = QLabel("Y2:")
        tab7_linedit_my2 = QLineEdit()
        tab7_label_m3 = QLabel("步长:")
        tab7_label_mdx = QLabel("DX:")
        tab7_linedit_mdx = QLineEdit()
        tab7_label_mdy = QLabel("DY:")
        tab7_linedit_mdy = QLineEdit()
        tab7_grid2 = QGridLayout()
        tab7_grid2.addWidget(tab7_label_m1, 0, 0)
        tab7_grid2.addWidget(tab7_label_mx1, 0, 1)
        tab7_grid2.addWidget(tab7_linedit_mx1, 0, 2)
        tab7_grid2.addWidget(tab7_label_my1, 0, 3)
        tab7_grid2.addWidget(tab7_linedit_my1, 0, 4)
        tab7_grid2.addWidget(tab7_label_m2, 1, 0)
        tab7_grid2.addWidget(tab7_label_mx2, 1, 1)
        tab7_grid2.addWidget(tab7_linedit_mx2, 1, 2)
        tab7_grid2.addWidget(tab7_label_my2, 1, 3)
        tab7_grid2.addWidget(tab7_linedit_my2, 1, 4)
        tab7_grid2.addWidget(tab7_label_m3, 2, 0)
        tab7_grid2.addWidget(tab7_label_mdx, 2, 1)
        tab7_grid2.addWidget(tab7_linedit_mdx, 2, 2)
        tab7_grid2.addWidget(tab7_label_mdy, 2, 3)
        tab7_grid2.addWidget(tab7_linedit_mdy, 2, 4)
        tab7_mid_groupbox1 = QGroupBox()
        tab7_mid_groupbox1.setLayout(tab7_grid2)

        tab7_checkbox9 = QCheckBox("输出所有点位")
        tab7_vbox2 = QVBoxLayout()
        tab7_vbox2.addWidget(tab7_checkbox8)
        tab7_vbox2.addWidget(tab7_mid_groupbox1)
        tab7_vbox2.addWidget(tab7_checkbox9)
        tab7_mid_groupbox.setLayout(tab7_vbox2)

        tab7_grid3 = QGridLayout()
        output_vars = ["HSIGN", "HSWELL", "DIR", "PDIR", "TDIR", "TM01", "RTM01", "RTP", "TM02", "FSPR", "DSPR", "VEL",
                       "FRCOEF", "WIND", "DISSIP", "QB", "TRANSP", "FORCE", "UBOT", "URMS", "WLEN", "STEEPNESS",
                       "DHSIGN", "DRTM01", "LEAK", "TSEC", "XP", "YP", "DIST", "SETUP", "TMM10", "RTMM10", "DEPTH",
                       "TMBOT", "QP", "BFI", "NPLANT", " WATLEV ", "BOTLEV", "TPS", "DISBOT", " DISSURF ", " DISWCAP",
                       "GENE", "GENW", "REDI", "REDQ", "REDT", "PROPA", "PROPX", "PROPT", "PROPS", "RADS", " LWAVP"]
        for i in range(len(output_vars)):
            tab7_right_checkbox = QCheckBox(output_vars[i])
            # quotient = num // 6
            # remainder = i % 6
            tab7_grid3.addWidget(tab7_right_checkbox, i // 6, i % 6)
        tab7_right_groupbox.setLayout(tab7_grid3)

        tab7_bottom_checkbox = QCheckBox("嵌套输出")
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
        tab7_grid4 = QGridLayout()
        tab7_grid4.addWidget(tab7_label_bx1, 0, 0)
        tab7_grid4.addWidget(tab7_linedit_bx1, 0, 1)
        tab7_grid4.addWidget(tab7_label_by1, 0, 2)
        tab7_grid4.addWidget(tab7_linedit_by1, 0, 3)
        tab7_grid4.addWidget(tab7_label_bx2, 1, 0)
        tab7_grid4.addWidget(tab7_linedit_bx2, 1, 1)
        tab7_grid4.addWidget(tab7_label_by2, 1, 2)
        tab7_grid4.addWidget(tab7_linedit_by2, 1, 3)
        tab7_grid4.addWidget(tab7_label_bdx, 2, 0)
        tab7_grid4.addWidget(tab7_linedit_bdx, 2, 1)
        tab7_grid4.addWidget(tab7_label_bdy, 2, 2)
        tab7_grid4.addWidget(tab7_linedit_bdy, 2, 3)
        tab7_bottom_groupbox1 = QGroupBox()
        tab7_bottom_groupbox1.setLayout(tab7_grid4)

        tab7_label_t1 = QLabel(u'起始时间:')
        tab7_label_dt = QLabel(u'时间步长:')
        tab7_linedit_bt = QLineEdit()
        tab7_combox_b1 = QComboBox()
        tab7_combox_b1.addItems(['MIN', 'SEC', 'HR'])
        self.tab7_datetime1 = QDateTimeEdit()
        self.tab7_datetime1.setDateTime(QDateTime.currentDateTime())
        tab7_grid5 = QGridLayout()
        tab7_grid5.addWidget(tab7_label_t1, 0, 0)
        tab7_grid5.addWidget(self.tab7_datetime1, 0, 1)
        tab7_grid5.addWidget(tab7_label_dt, 2, 0)
        tab7_grid5.addWidget(tab7_linedit_bt, 2, 1)
        tab7_grid5.addWidget(tab7_combox_b1, 2, 2)
        tab7_bottom_groupbox2 = QGroupBox()
        tab7_bottom_groupbox2.setLayout(tab7_grid5)

        tab7_grid6 = QVBoxLayout()
        tab7_grid6.addWidget(tab7_bottom_checkbox)
        tab7_grid6.addWidget(tab7_bottom_groupbox1)
        tab7_grid6.addWidget(tab7_bottom_groupbox2)
        self.tab7_bottom_groupbox = QGroupBox()
        self.tab7_bottom_groupbox.setLayout(tab7_grid6)

        self.tab7_stack.addWidget(tab7_left_groupbox)
        self.tab7_stack.addWidget(tab7_mid_groupbox)
        self.tab7_stack.addWidget(tab7_right_groupbox)
        self.tab7_stack.addWidget(self.tab7_bottom_groupbox)

    def addPointsFiles(self):
        self.points_files_num += 1
        self.points1[str(self.points_files_num)] = [QLabel("点位名:"),
                                                    QLineEdit(),
                                                    QLabel("点位文件名:"),
                                                    QLineEdit()]
        for i, widget in enumerate(self.points1[str(self.points_files_num)]):
            self.tab7_grid1.addWidget(widget, self.points_files_num - 1, i)

    def addPointsCoordinates(self):
        self.points_coords_num += 1
        self.points2[str(self.points_coords_num)] = [QLabel("点位名:"),
                                                     QLineEdit(),
                                                     QLabel("X:"),
                                                     QLineEdit(),
                                                     QLabel("Y:"),
                                                     QLineEdit()]
        for i, widget in enumerate(self.points2[str(self.points_coords_num)]):
            self.tab7_grid2.addWidget(widget, self.points_coords_num - 1, i)

    def calculate_input_file(self):
        self.tab8_groupbox = QGroupBox()

        tab8_combox = QComboBox()
        tab8_combox.addItems(["dat文件", "geo文件"])
        tab8_pushbutton1 = QPushButton("打开")
        tab8_label1 = QLabel("最大散点距离:")
        tab8_linedit1 = QLineEdit()
        tab8_label2 = QLabel("m")

        tab8_label_x1 = QLabel("X1:")
        tab8_linedit_x1 = QLineEdit()
        tab8_label_y1 = QLabel("Y1:")
        tab8_linedit_y1 = QLineEdit()
        tab8_label_x2 = QLabel("X2:")
        tab8_linedit_x2 = QLineEdit()
        tab8_label_y2 = QLabel("Y2:")
        tab8_linedit_y2 = QLineEdit()
        tab8_label_dx = QLabel("DX:")
        tab8_linedit_dx = QLineEdit()
        tab8_label_dy = QLabel("DY:")
        tab8_linedit_dy = QLineEdit()
        tab8_grid1 = QGridLayout()
        tab8_grid1.addWidget(tab8_label_x1, 0, 0)
        tab8_grid1.addWidget(tab8_linedit_x1, 0, 1)
        tab8_grid1.addWidget(tab8_label_y1, 0, 2)
        tab8_grid1.addWidget(tab8_linedit_y1, 0, 3)
        tab8_grid1.addWidget(tab8_label_x2, 1, 0)
        tab8_grid1.addWidget(tab8_linedit_x2, 1, 1)
        tab8_grid1.addWidget(tab8_label_y2, 1, 2)
        tab8_grid1.addWidget(tab8_linedit_y2, 1, 3)
        tab8_grid1.addWidget(tab8_label_dx, 2, 0)
        tab8_grid1.addWidget(tab8_linedit_dx, 2, 1)
        tab8_grid1.addWidget(tab8_label_dy, 2, 2)
        tab8_grid1.addWidget(tab8_linedit_dy, 2, 3)
        tab8_groupbox1 = QGroupBox()
        tab8_groupbox1.setLayout(tab8_grid1)

        tab8_label3 = QLabel("输出文件名:")
        tab8_linedit2 = QLineEdit()
        tab8_pushbutton2 = QPushButton("运行")

        tab8_grid2 = QGridLayout()
        tab8_grid2.addWidget(tab8_combox, 0, 0)
        tab8_grid2.addWidget(tab8_pushbutton1, 0, 1)
        tab8_grid2.addWidget(tab8_label1, 1, 0)
        tab8_grid2.addWidget(tab8_linedit1, 1, 1)
        tab8_grid2.addWidget(tab8_label2, 1, 2)
        tab8_grid2.addWidget(tab8_groupbox1, 2, 0, 1, 2)
        tab8_grid2.addWidget(tab8_label3, 3, 0)
        tab8_grid2.addWidget(tab8_linedit2, 3, 1)
        tab8_grid2.addWidget(tab8_pushbutton2, 4, 0)
        self.tab8_groupbox.setLayout(tab8_grid2)

    def writeFile(self):
        input_lines = []

        # ************************-----PROJECT-----****************************
        name = self.tab1_linedit1.text()
        nr = self.tab1_linedit2.text()
        project_line = " ".join(["PROJect", "\'" + name + "\'", "\'" + nr + "\'", "\n"])
        print(project_line)
        input_lines.append(project_line)

        # ************************-----SET-----****************************
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
            # print(self.tab1_combobox1.currentText())
            inrhog = '1'
        else:
            # print(self.tab1_combobox1.currentText())
            inrhog = '0'
        # hsrerr = '0.10'
        convention = 'CARTesian'
        pwtail = '4'
        froudmax = '0.8'
        printf = '4'
        prtest = '4'
        set_line = " ".join(['SET', level, nor, depmin, maxmes, maxerr, grav, rho,
                             cdcap, inrhog, convention, pwtail, froudmax, printf, prtest, "\n"])
        print(set_line)
        input_lines.append(set_line)

        # ************************-----MODE-----****************************
        if self.tab1_combobox2.currentIndex():
            mode = 'NONSTATionary'
        else:
            mode = 'STATionary'
        dimension = 'TWODimensional'
        mode_line = " ".join(["MODE", mode, dimension, "\n"])
        print(mode_line)
        input_lines.append(mode_line)

        # ************************-----COORDINATES-----****************************
        coordinate_index = self.tab1_combobox3.currentIndex()
        if coordinate_index is 0:
            coordinate = 'CARTesian'
        elif coordinate_index is 1:
            coordinate = 'SPHErical CCM'
        else:
            coordinate = 'SPHErical QC'
        coordinate_line = " ".join(["COORDINATES", coordinate, "\n"])
        print(coordinate_line)
        input_lines.append(coordinate_line)

        # ************************-----CGRID-----****************************
        if self.tab2_radiobutton2.isChecked():
            shape = 'UNSTRUCtured CIRcle'
        else:
            shape = 'REGular'
        mdc = '36'
        flow = '0.04'
        fhigh = '2'
        cgrid_line = " ".join(["CGRID", shape, mdc, flow, fhigh, "\n"])
        input_lines.append(cgrid_line)

        # ************************-----READgrid-----****************************
        readgrid_line = " ".join(["READgrid", "UNSTRUCtured", "ADCirc", "\n"])
        input_lines.append(readgrid_line)

        # ************************-----INPgrid-----****************************
        inpgrid_line = " ".join(["INPgrid"])
        input_lines.append(inpgrid_line)

        # ************************-----READinp-----****************************
        readinp_line = " ".join(["READinp"])
        input_lines.append(readinp_line)

        # ************************-----WIND-----****************************
        vel = self.tab3_linedit2.text()
        dir_ = self.tab3_linedit3.text()
        wind_line = " ".join(["WIND", vel, dir_, "\n"])
        input_lines.append(wind_line)

        # ************************-----BOUNd SHAPespec-----****************************
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
        input_lines.append(bound_shapespec_line)

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
        input_lines.append(boundspec_line)

        # ************************-----INITial-----****************************
        if self.tab6_combox1.currentIndex() is 0:
            initial = 'DAEFault'
        elif self.tab6_combox1.currentIndex() is 1:
            initial = 'ZERO'
        else:
            initial = " ".join(["PAR", hs, per, dir, dd])
        initial_line = " ".join(["INITial", initial, "\n"])
        input_lines.append(initial_line)

        # ************************-----GEN3-----****************************
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
        input_lines.append(gen3_line)

        # ************************-----WCAP-----****************************
        wcap_line = " ".join(["WCAP", self.tab5_combox2.currentText(), "\n"])
        input_lines.append(wcap_line)

        # ************************-----QUADrupl-----****************************
        if self.tab5_checkbox1.isChecked():
            quadrupl_line = 'QUADrupl \n'
        else:
            quadrupl_line = '!QUADrupl \n'
        input_lines.append(quadrupl_line)

        # ************************-----BREaking-----****************************
        breaking_line = " ".join(["BREaking", self.tab5_combox3.currentText(), "\n"])
        input_lines.append(breaking_line)

        # ************************-----FRICtion-----****************************
        if self.tab5_checkbox5.isChecked():
            if self.tab5_combox4.currentText() is "JONswap":
                friction_line = " ".join(["FRICtion JONswap", "CONstant 0.067 \n"])
            elif self.tab5_combox4.currentText() is "COLLins":
                friction_line = " ".join(["FRICtion COLLins 0.015 \n"])
            else:
                friction_line = " ".join(["FRICtion MADsen 0.05 \n"])
        else:
            friction_line = " ".join(["!FRICtion \n"])
        input_lines.append(friction_line)

        # ************************-----TRIad-----****************************
        if self.tab5_checkbox3.isChecked():
            triad_line = 'TRIad \n'
        else:
            triad_line = '!TRIad \n'
        input_lines.append(triad_line)

        # ************************-----VEGEtation-----****************************
        height = self.tab5_linedit2.text()
        diamtr = self.tab5_linedit3.text()
        nstems = self.tab5_linedit4.text()
        drag = self.tab5_linedit5.text()
        if height and diamtr and nstems and drag:
            vegetation_line = " ".join(["VEGEtation", height, diamtr, nstems, drag])
        else:
            vegetation_line = "!VEGEtation \n"
        input_lines.append(vegetation_line)

        # ************************-----LIMiter-----****************************
        if self.tab5_checkbox2.isChecked():
            limiter_line = 'LIMiter \n'
        else:
            limiter_line = '!LIMiter \n'
        input_lines.append(limiter_line)

        # ************************-----OBSTacle-----****************************
        if self.obs_num == 0:
            obstacle_line = "!OBSTacle"
            input_lines.append(obstacle_line)
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
                input_lines.append(obstacle_line)

        # ************************-----SETUP-----****************************

        # ************************-----DIFFRACtion-----****************************
        if self.tab5_checkbox4.isChecked():
            diffraction_line = " ".join(["DIFFRACtion 1 0 0 1\n"])
        else:
            diffraction_line = " ".join(["!DIFFRACtion\n"])
        input_lines.append(diffraction_line)

        # ************************-----PROP-----****************************
        if self.tab6_radiobutton1.isChecked():
            prop_line = "PROP BSBT\n"
        elif self.tab6_radiobutton2.isChecked():
            waveage = self.tab6_linedit1.text()
            time_unit = self.tab6_combox2.currentText()
            prop_line = " ".join(["PROP GSE", waveage, time_unit, "\n"])
        else:
            prop_line = "!PROP"
        input_lines.append(prop_line)

        # ************************-----NUMeric-----****************************
        if self.tab6_combox3.currentIndex():
            numeric_line = "NUMeric STOPC\n"
        else:
            numeric_line = "NUMeric ACCUR\n"
        input_lines.append(numeric_line)

        # ************************-----POINTS-----****************************
        if self.tab7_checkbox1.isChecked():
            for i in range(self.points_files_num):
                if self.points1[str(self.points_files_num)][3].text():
                    sname = "\'" + self.points1[str(self.points_files_num)][1].text() + "\'"
                    fname = "\'" + self.points1[str(self.points_files_num)][3].text() + "\'"
                    points_line = " ".join(["POINTS", sname, "FILE", fname, "\n"])
                    input_lines.append(points_line)
        if self.tab7_checkbox2.isChecked():
            for i in range(self.points_coords_num):
                points_x = self.points1[str(self.points_coords_num)][3].text()
                points_y = self.points1[str(self.points_coords_num)][3].text()
                if points_x and points_y:
                    sname = "\'" + self.points1[str(self.points_coords_num)][1].text() + "\'"
                    points_line = " ".join(["POINTS", sname, points_x, points_y, "\n"])
                    input_lines.append(points_line)

        # ************************-----COMPute-----****************************
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
        input_lines.append(compute_line)

        with open("input", 'w') as f_out:
            f_out.writelines(input_lines)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    s = Swan()
    s.show()
    sys.exit(app.exec_())
