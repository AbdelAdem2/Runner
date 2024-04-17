from views.Router import Router, DataStrategyEnum
from views.index_view import IndexView
from views.profile_view import ProfileView
from views.settings_view import SettingsView
from views.data_view import DataView
from views.home_view import HomeView
from views.login_view import LoginView
from views.history_view import HistoryView

router = Router(DataStrategyEnum.QUERY)

router.routes = {
  "/": IndexView,
  "/home": HomeView,
  "/login": LoginView,
  "/history": HistoryView,
}