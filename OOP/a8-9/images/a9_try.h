#pragma once

#include <QtWidgets/QMainWindow>
#include "ui_a9_try.h"
#include <qwidget.h>
#include "Service.h"
#include <qlistwidget.h>
#include <qlineedit.h>
#include <qpushbutton.h>
#include "Repository.h"
#include "AdminGui.h"
#include "UserService.h"
#include "UserGui.h"
#include "AdoptionList.h"
class a9_try : public QMainWindow
{
    Q_OBJECT

public:
    a9_try(QWidget *parent = nullptr);
    QWidget* central;
    QPushButton* userButton;
    QPushButton* adminButton;
	QPushButton* exitButton;

    Repository* repo;
    Service* serv;
    AdminGui* adminGui;
	UserGui* userGui;
    ~a9_try();

private:
    Ui::a9_tryClass ui;
    void initGUI();
    void adminButtonHandler();
    void userButtonHandler();
};
