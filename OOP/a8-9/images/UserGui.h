#pragma once  
#include <qwidget.h>  
#include "UserService.h"  
#include <qlistwidget.h>  
#include <qlineedit.h>  
#include <qpushbutton.h>  
#include <qmessagebox.h>  
#include <QtNetwork/QNetworkReply>  
#include <QtNetwork/QNetworkRequest>  
#include <QtNetwork/QNetworkAccessManager>  
#include <qlabel.h>  
#include <qpixmap.h>  
#include <qurl.h>  
#include "Chart.h"
#include <qcheckbox.h>

class UserGui : public QWidget  
{
	Q_OBJECT
private:  

UserService* userserv;  
QPushButton* seeDogsButton;  
QPushButton* seeAdoptionListButton;  
QPushButton* searchBreed;  
QPushButton* exitButton;  
QPushButton* chartButton;  
QNetworkAccessManager* networkManager;  
QCheckBox* csvBox;
QCheckBox* htmlBox;

public:  
UserGui(QWidget* parent = nullptr, UserService* userserv = nullptr);  
void initGui();  
void seeDogsButtonHandler();  
void seeAdoptionListButtonHandler();  
void searchBreedHandler();  
void exitButtonHandler();  
void chartButtonHandler();  
void connectSignalsAndSLots();
void adoptionListHandler(int type);
};
