
# built-in
import sys

# third-party
from PySide6 import QtWidgets, QtGui

# internal
from client import PSNCache


class TitlesView(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.client = PSNCache.CLIENT
        self.psnawp = PSNCache.PSNAWP

        self.setWindowTitle("PSN Titles View")

        self.main_layout = QtWidgets.QHBoxLayout()
        self.setLayout(self.main_layout)

        self.view = QtWidgets.QTreeView(self)
        self.view.setSortingEnabled(True)
        self.view_layout = QtWidgets.QVBoxLayout()
        self.view_layout.addWidget(self.view)
        self.main_layout.addLayout(self.view_layout)

        self.model = QtGui.QStandardItemModel()
        self.model.setHorizontalHeaderLabels(
            ["name", "playtime", "first played", "last played"]
        )
        self.model_root_item = self.model.invisibleRootItem()

        self.view.setModel(self.model)

        self.populate_title()

    def populate_title(self):
        for title_stat in self.client.title_stats():
            name = QtGui.QStandardItem(title_stat.name)

            play_duration = QtGui.QStandardItem(str(title_stat.play_duration))
            first_played = QtGui.QStandardItem(str(title_stat.first_played_date_time))
            last_played = QtGui.QStandardItem(str(title_stat.last_played_date_time))

            self.model_root_item.appendRow([name, play_duration, first_played, last_played])


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    view = TitlesView()
    view.show()
    app.exec()
