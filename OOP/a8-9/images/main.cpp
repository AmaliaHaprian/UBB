#include "a9_try.h"
#include <QtWidgets/QApplication>
#include <qlabel.h>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    a9_try w;
    w.show();
    return a.exec();
}
