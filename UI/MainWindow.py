# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(785, 578)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(30, 10, 741, 531))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setObjectName("tabWidget")
        self.tabRegistros = QtWidgets.QWidget()
        self.tabRegistros.setObjectName("tabRegistros")
        self.label_14 = QtWidgets.QLabel(self.tabRegistros)
        self.label_14.setGeometry(QtCore.QRect(10, 30, 60, 16))
        self.label_14.setObjectName("label_14")
        self.comboBoxSalasRegistro = QtWidgets.QComboBox(self.tabRegistros)
        self.comboBoxSalasRegistro.setGeometry(QtCore.QRect(60, 20, 201, 26))
        self.comboBoxSalasRegistro.setObjectName("comboBoxSalasRegistro")
        self.label_15 = QtWidgets.QLabel(self.tabRegistros)
        self.label_15.setGeometry(QtCore.QRect(290, 30, 60, 16))
        self.label_15.setObjectName("label_15")
        self.comboBoxAlunoRegistro = QtWidgets.QComboBox(self.tabRegistros)
        self.comboBoxAlunoRegistro.setGeometry(QtCore.QRect(340, 20, 191, 26))
        self.comboBoxAlunoRegistro.setObjectName("comboBoxAlunoRegistro")
        self.label_16 = QtWidgets.QLabel(self.tabRegistros)
        self.label_16.setGeometry(QtCore.QRect(10, 60, 191, 16))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.tabRegistros)
        self.label_17.setGeometry(QtCore.QRect(210, 60, 16, 16))
        self.label_17.setObjectName("label_17")
        self.pushButton_Emprestar = QtWidgets.QPushButton(self.tabRegistros)
        self.pushButton_Emprestar.setGeometry(QtCore.QRect(340, 60, 113, 32))
        self.pushButton_Emprestar.setObjectName("pushButton_Emprestar")
        self.pushButton_Devolver = QtWidgets.QPushButton(self.tabRegistros)
        self.pushButton_Devolver.setGeometry(QtCore.QRect(460, 60, 113, 32))
        self.pushButton_Devolver.setObjectName("pushButton_Devolver")
        self.tableWidgetRegistros = QtWidgets.QTableWidget(self.tabRegistros)
        self.tableWidgetRegistros.setGeometry(QtCore.QRect(10, 110, 721, 371))
        self.tableWidgetRegistros.setObjectName("tableWidgetRegistros")
        self.tableWidgetRegistros.setColumnCount(6)
        self.tableWidgetRegistros.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetRegistros.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetRegistros.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetRegistros.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetRegistros.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetRegistros.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetRegistros.setHorizontalHeaderItem(5, item)
        self.tabWidget.addTab(self.tabRegistros, "")
        self.tabAlunos = QtWidgets.QWidget()
        self.tabAlunos.setObjectName("tabAlunos")
        self.label = QtWidgets.QLabel(self.tabAlunos)
        self.label.setGeometry(QtCore.QRect(20, 20, 60, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tabAlunos)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 60, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tabAlunos)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 60, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tabAlunos)
        self.label_4.setGeometry(QtCore.QRect(20, 150, 60, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tabAlunos)
        self.label_5.setGeometry(QtCore.QRect(20, 190, 60, 16))
        self.label_5.setObjectName("label_5")
        self.lineEditAlunoNome = QtWidgets.QLineEdit(self.tabAlunos)
        self.lineEditAlunoNome.setGeometry(QtCore.QRect(70, 20, 391, 21))
        self.lineEditAlunoNome.setObjectName("lineEditAlunoNome")
        self.comboBoxCurso = QtWidgets.QComboBox(self.tabAlunos)
        self.comboBoxCurso.setGeometry(QtCore.QRect(70, 60, 281, 26))
        self.comboBoxCurso.setObjectName("comboBoxCurso")
        self.comboBoxCurso.addItem("")
        self.comboBoxCurso.addItem("")
        self.comboBoxCurso.addItem("")
        self.comboBoxCurso.addItem("")
        self.comboBoxCurso.addItem("")
        self.comboBoxCurso.addItem("")
        self.comboBoxCurso.addItem("")
        self.comboBoxCurso.addItem("")
        self.comboBoxCurso.addItem("")
        self.lineEditMatricula = QtWidgets.QLineEdit(self.tabAlunos)
        self.lineEditMatricula.setGeometry(QtCore.QRect(90, 110, 201, 21))
        self.lineEditMatricula.setObjectName("lineEditMatricula")
        self.lineEditTelefone = QtWidgets.QLineEdit(self.tabAlunos)
        self.lineEditTelefone.setGeometry(QtCore.QRect(90, 150, 141, 21))
        self.lineEditTelefone.setObjectName("lineEditTelefone")
        self.lineEditEmail = QtWidgets.QLineEdit(self.tabAlunos)
        self.lineEditEmail.setGeometry(QtCore.QRect(70, 190, 221, 21))
        self.lineEditEmail.setObjectName("lineEditEmail")
        self.pushButtonAdicionarAluno = QtWidgets.QPushButton(self.tabAlunos)
        self.pushButtonAdicionarAluno.setGeometry(QtCore.QRect(10, 250, 113, 32))
        self.pushButtonAdicionarAluno.setObjectName("pushButtonAdicionarAluno")
        self.pushButtonRemoverAluno = QtWidgets.QPushButton(self.tabAlunos)
        self.pushButtonRemoverAluno.setGeometry(QtCore.QRect(130, 250, 113, 32))
        self.pushButtonRemoverAluno.setObjectName("pushButtonRemoverAluno")
        self.listWidgetAlunos = QtWidgets.QListWidget(self.tabAlunos)
        self.listWidgetAlunos.setGeometry(QtCore.QRect(490, 20, 241, 261))
        self.listWidgetAlunos.setObjectName("listWidgetAlunos")
        self.pushButtonEditarAluno = QtWidgets.QPushButton(self.tabAlunos)
        self.pushButtonEditarAluno.setGeometry(QtCore.QRect(250, 250, 113, 32))
        self.pushButtonEditarAluno.setObjectName("pushButtonEditarAluno")
        self.pushButtonVerDados = QtWidgets.QPushButton(self.tabAlunos)
        self.pushButtonVerDados.setGeometry(QtCore.QRect(370, 250, 113, 32))
        self.pushButtonVerDados.setObjectName("pushButtonVerDados")
        self.tabWidget.addTab(self.tabAlunos, "")
        self.tabProfessores = QtWidgets.QWidget()
        self.tabProfessores.setObjectName("tabProfessores")
        self.label_6 = QtWidgets.QLabel(self.tabProfessores)
        self.label_6.setGeometry(QtCore.QRect(29, 50, 61, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tabProfessores)
        self.label_7.setGeometry(QtCore.QRect(19, 100, 61, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tabProfessores)
        self.label_8.setGeometry(QtCore.QRect(40, 150, 51, 16))
        self.label_8.setObjectName("label_8")
        self.lineEditProfNome = QtWidgets.QLineEdit(self.tabProfessores)
        self.lineEditProfNome.setGeometry(QtCore.QRect(80, 50, 321, 21))
        self.lineEditProfNome.setObjectName("lineEditProfNome")
        self.lineEditProfTelefone = QtWidgets.QLineEdit(self.tabProfessores)
        self.lineEditProfTelefone.setGeometry(QtCore.QRect(80, 100, 201, 21))
        self.lineEditProfTelefone.setObjectName("lineEditProfTelefone")
        self.lineEditProfEmail = QtWidgets.QLineEdit(self.tabProfessores)
        self.lineEditProfEmail.setGeometry(QtCore.QRect(80, 150, 201, 21))
        self.lineEditProfEmail.setObjectName("lineEditProfEmail")
        self.listWidgetProf = QtWidgets.QListWidget(self.tabProfessores)
        self.listWidgetProf.setGeometry(QtCore.QRect(480, 50, 241, 221))
        self.listWidgetProf.setObjectName("listWidgetProf")
        self.pushButtonProfAdicionar = QtWidgets.QPushButton(self.tabProfessores)
        self.pushButtonProfAdicionar.setGeometry(QtCore.QRect(0, 240, 113, 32))
        self.pushButtonProfAdicionar.setObjectName("pushButtonProfAdicionar")
        self.pushButtonProfRemover = QtWidgets.QPushButton(self.tabProfessores)
        self.pushButtonProfRemover.setGeometry(QtCore.QRect(120, 240, 113, 32))
        self.pushButtonProfRemover.setObjectName("pushButtonProfRemover")
        self.pushButtonProfEditar = QtWidgets.QPushButton(self.tabProfessores)
        self.pushButtonProfEditar.setGeometry(QtCore.QRect(240, 240, 113, 32))
        self.pushButtonProfEditar.setObjectName("pushButtonProfEditar")
        self.pushButtonProfVerDados = QtWidgets.QPushButton(self.tabProfessores)
        self.pushButtonProfVerDados.setGeometry(QtCore.QRect(360, 240, 113, 32))
        self.pushButtonProfVerDados.setObjectName("pushButtonProfVerDados")
        self.tabWidget.addTab(self.tabProfessores, "")
        self.tabSalas = QtWidgets.QWidget()
        self.tabSalas.setObjectName("tabSalas")
        self.label_9 = QtWidgets.QLabel(self.tabSalas)
        self.label_9.setGeometry(QtCore.QRect(10, 10, 131, 16))
        self.label_9.setObjectName("label_9")
        self.label_11 = QtWidgets.QLabel(self.tabSalas)
        self.label_11.setGeometry(QtCore.QRect(10, 270, 51, 16))
        self.label_11.setObjectName("label_11")
        self.listWidgetSalaAluno = QtWidgets.QListWidget(self.tabSalas)
        self.listWidgetSalaAluno.setGeometry(QtCore.QRect(10, 300, 171, 151))
        self.listWidgetSalaAluno.setObjectName("listWidgetSalaAluno")
        self.pushButtonAddAlunoSala = QtWidgets.QPushButton(self.tabSalas)
        self.pushButtonAddAlunoSala.setGeometry(QtCore.QRect(10, 460, 141, 32))
        self.pushButtonAddAlunoSala.setObjectName("pushButtonAddAlunoSala")
        self.lineEditIdSala = QtWidgets.QLineEdit(self.tabSalas)
        self.lineEditIdSala.setGeometry(QtCore.QRect(150, 10, 191, 21))
        self.lineEditIdSala.setObjectName("lineEditIdSala")
        self.listWidgetSalaProf = QtWidgets.QListWidget(self.tabSalas)
        self.listWidgetSalaProf.setGeometry(QtCore.QRect(10, 110, 171, 111))
        self.listWidgetSalaProf.setObjectName("listWidgetSalaProf")
        self.label_12 = QtWidgets.QLabel(self.tabSalas)
        self.label_12.setGeometry(QtCore.QRect(10, 80, 171, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.tabSalas)
        self.label_13.setGeometry(QtCore.QRect(210, 270, 131, 16))
        self.label_13.setObjectName("label_13")
        self.listWidgetSalaAlunoAssociados = QtWidgets.QListWidget(self.tabSalas)
        self.listWidgetSalaAlunoAssociados.setGeometry(QtCore.QRect(200, 300, 161, 151))
        self.listWidgetSalaAlunoAssociados.setObjectName("listWidgetSalaAlunoAssociados")
        self.pushButtonAddProfSala = QtWidgets.QPushButton(self.tabSalas)
        self.pushButtonAddProfSala.setGeometry(QtCore.QRect(10, 230, 141, 32))
        self.pushButtonAddProfSala.setObjectName("pushButtonAddProfSala")
        self.pushButtonDelAlunoSala = QtWidgets.QPushButton(self.tabSalas)
        self.pushButtonDelAlunoSala.setGeometry(QtCore.QRect(210, 460, 111, 32))
        self.pushButtonDelAlunoSala.setObjectName("pushButtonDelAlunoSala")
        self.label_18 = QtWidgets.QLabel(self.tabSalas)
        self.label_18.setGeometry(QtCore.QRect(390, 10, 201, 16))
        self.label_18.setObjectName("label_18")
        self.pushButtonAdicionarSala = QtWidgets.QPushButton(self.tabSalas)
        self.pushButtonAdicionarSala.setGeometry(QtCore.QRect(210, 40, 113, 31))
        self.pushButtonAdicionarSala.setObjectName("pushButtonAdicionarSala")
        self.spinBoxNumeroChaves = QtWidgets.QSpinBox(self.tabSalas)
        self.spinBoxNumeroChaves.setGeometry(QtCore.QRect(520, 0, 51, 31))
        self.spinBoxNumeroChaves.setObjectName("spinBoxNumeroChaves")
        self.listWidgetSalaProfAssociados = QtWidgets.QListWidget(self.tabSalas)
        self.listWidgetSalaProfAssociados.setGeometry(QtCore.QRect(200, 110, 161, 111))
        self.listWidgetSalaProfAssociados.setObjectName("listWidgetSalaProfAssociados")
        self.label_10 = QtWidgets.QLabel(self.tabSalas)
        self.label_10.setGeometry(QtCore.QRect(200, 80, 151, 16))
        self.label_10.setObjectName("label_10")
        self.pushButtonDelProfSala = QtWidgets.QPushButton(self.tabSalas)
        self.pushButtonDelProfSala.setGeometry(QtCore.QRect(200, 230, 121, 31))
        self.pushButtonDelProfSala.setObjectName("pushButtonDelProfSala")
        self.listWidgetSalasCadastradas = QtWidgets.QListWidget(self.tabSalas)
        self.listWidgetSalasCadastradas.setGeometry(QtCore.QRect(460, 110, 191, 361))
        self.listWidgetSalasCadastradas.setObjectName("listWidgetSalasCadastradas")
        self.label_19 = QtWidgets.QLabel(self.tabSalas)
        self.label_19.setGeometry(QtCore.QRect(500, 80, 131, 16))
        self.label_19.setObjectName("label_19")
        self.tabWidget.addTab(self.tabSalas, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 785, 22))
        self.menubar.setObjectName("menubar")
        self.menuArquivo = QtWidgets.QMenu(self.menubar)
        self.menuArquivo.setObjectName("menuArquivo")
        self.menuSobre = QtWidgets.QMenu(self.menubar)
        self.menuSobre.setObjectName("menuSobre")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSalvar = QtWidgets.QAction(MainWindow)
        self.actionSalvar.setObjectName("actionSalvar")
        self.actionExportar_Relatorio = QtWidgets.QAction(MainWindow)
        self.actionExportar_Relatorio.setObjectName("actionExportar_Relatorio")
        self.actionCarregar = QtWidgets.QAction(MainWindow)
        self.actionCarregar.setObjectName("actionCarregar")
        self.actionSair = QtWidgets.QAction(MainWindow)
        self.actionSair.setObjectName("actionSair")
        self.menuArquivo.addAction(self.actionSalvar)
        self.menuArquivo.addAction(self.actionExportar_Relatorio)
        self.menuArquivo.addAction(self.actionCarregar)
        self.menuArquivo.addAction(self.actionSair)
        self.menubar.addAction(self.menuArquivo.menuAction())
        self.menubar.addAction(self.menuSobre.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_14.setText(_translate("MainWindow", "Sala:"))
        self.label_15.setText(_translate("MainWindow", "Aluno"))
        self.label_16.setText(_translate("MainWindow", "Número de chaves Disponiveis:"))
        self.label_17.setText(_translate("MainWindow", "0"))
        self.pushButton_Emprestar.setText(_translate("MainWindow", "Emprestar"))
        self.pushButton_Devolver.setText(_translate("MainWindow", "Devolver"))
        item = self.tableWidgetRegistros.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Sala"))
        item = self.tableWidgetRegistros.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Aluno"))
        item = self.tableWidgetRegistros.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Status"))
        item = self.tableWidgetRegistros.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Data"))
        item = self.tableWidgetRegistros.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Hora Emprestimo"))
        item = self.tableWidgetRegistros.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Hora Devolução"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabRegistros), _translate("MainWindow", "Registros"))
        self.label.setText(_translate("MainWindow", "Nome:"))
        self.label_2.setText(_translate("MainWindow", "Curso:"))
        self.label_3.setText(_translate("MainWindow", "Matricula:"))
        self.label_4.setText(_translate("MainWindow", "Telefone:"))
        self.label_5.setText(_translate("MainWindow", "Email:"))
        self.comboBoxCurso.setItemText(0, _translate("MainWindow", "Sistemas de Informação"))
        self.comboBoxCurso.setItemText(1, _translate("MainWindow", "Licenciatura em Computação"))
        self.comboBoxCurso.setItemText(2, _translate("MainWindow", "Engenharia Ambiental"))
        self.comboBoxCurso.setItemText(3, _translate("MainWindow", "Engenharia Cartográfica e Agrimensura"))
        self.comboBoxCurso.setItemText(4, _translate("MainWindow", "Agronomia"))
        self.comboBoxCurso.setItemText(5, _translate("MainWindow", "Engenharia de Pesca"))
        self.comboBoxCurso.setItemText(6, _translate("MainWindow", "Engenharia Florestal"))
        self.comboBoxCurso.setItemText(7, _translate("MainWindow", "Medicina Veterinária"))
        self.comboBoxCurso.setItemText(8, _translate("MainWindow", "Zootecnia"))
        self.pushButtonAdicionarAluno.setText(_translate("MainWindow", "Adicionar"))
        self.pushButtonRemoverAluno.setText(_translate("MainWindow", "Remover"))
        self.pushButtonEditarAluno.setText(_translate("MainWindow", "Editar"))
        self.pushButtonVerDados.setText(_translate("MainWindow", "Ver Dados"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabAlunos), _translate("MainWindow", "Alunos"))
        self.label_6.setText(_translate("MainWindow", "Nome:"))
        self.label_7.setText(_translate("MainWindow", "Telefone:"))
        self.label_8.setText(_translate("MainWindow", "Email:"))
        self.pushButtonProfAdicionar.setText(_translate("MainWindow", "Adicionar"))
        self.pushButtonProfRemover.setText(_translate("MainWindow", "Remover"))
        self.pushButtonProfEditar.setText(_translate("MainWindow", "Editar"))
        self.pushButtonProfVerDados.setText(_translate("MainWindow", "Ver Dados"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabProfessores), _translate("MainWindow", "Professores"))
        self.label_9.setText(_translate("MainWindow", "Identificacao da Sala:"))
        self.label_11.setText(_translate("MainWindow", "Alunos "))
        self.pushButtonAddAlunoSala.setText(_translate("MainWindow", "Adicionar Aluno"))
        self.label_12.setText(_translate("MainWindow", "Professores "))
        self.label_13.setText(_translate("MainWindow", "Alunos associados"))
        self.pushButtonAddProfSala.setText(_translate("MainWindow", "Adicionar Professor"))
        self.pushButtonDelAlunoSala.setText(_translate("MainWindow", "Remover"))
        self.label_18.setText(_translate("MainWindow", "Numero de Chaves:"))
        self.pushButtonAdicionarSala.setText(_translate("MainWindow", "Adicionar Sala"))
        self.label_10.setText(_translate("MainWindow", "Professores associados"))
        self.pushButtonDelProfSala.setText(_translate("MainWindow", "Remover"))
        self.label_19.setText(_translate("MainWindow", "Salas Cadastradas"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSalas), _translate("MainWindow", "Salas"))
        self.menuArquivo.setTitle(_translate("MainWindow", "Arquivo"))
        self.menuSobre.setTitle(_translate("MainWindow", "Sobre"))
        self.actionSalvar.setText(_translate("MainWindow", "Salvar"))
        self.actionExportar_Relatorio.setText(_translate("MainWindow", "Exportar Relatorio"))
        self.actionCarregar.setText(_translate("MainWindow", "Carregar"))
        self.actionSair.setText(_translate("MainWindow", "Sair"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
