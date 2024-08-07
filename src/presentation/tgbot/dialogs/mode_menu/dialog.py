from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.common import sync_scroll
from aiogram_dialog.widgets.kbd import Row, ScrollingGroup, Select, PrevPage, NextPage, CurrentPage, Button
from aiogram_dialog.widgets.text import Format, List

from src.domain.entities.menu import MODES, ID_LIST_SCROLL
from src.presentation.tgbot.dialogs.dialog_extras.i18n.format import I18nFormat
from src.presentation.tgbot.dialogs.mode_menu.getters import getter
from src.presentation.tgbot.dialogs.mode_menu.handlers import on_click_back_to_main, on_click_select_mode
from src.presentation.tgbot.states.user import ModeMenu


def mode_menu() -> Dialog:
    return Dialog(
        Window(
            List(
                Format("{item.message}"),
                items=MODES,
                id=ID_LIST_SCROLL,
                page_size=1,
            ),
            ScrollingGroup(
                Select(
                    Format("{item.mode}"),
                    id="ms",
                    items=MODES,
                    item_id_getter=lambda item: item.id,
                    on_click=on_click_select_mode
                ),
                width=1,
                height=1,
                hide_pager=True,
                id="scroll_no_pager",
                on_page_changed=sync_scroll(ID_LIST_SCROLL)
            ),
            Row(
                PrevPage(scroll="scroll_no_pager", text=Format("←")),
                CurrentPage(scroll='scroll_no_pager', text=Format("{current_page1} / {data[len]}")),
                NextPage(scroll="scroll_no_pager", text=Format("→")),
            ),
            Button(I18nFormat('back-to-main-btn'), id='back_to_main', on_click=on_click_back_to_main),
            state=ModeMenu.GENERATE
        ),
        getter=getter,
    )
