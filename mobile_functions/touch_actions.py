from appium.webdriver.mobilecommand import MobileCommand as Command
import copy

class TouchAction(object):
    def __init__(self, driver=None):
        self._driver = driver
        self._actions = []

    def tap(self, element=None, x=None, y=None, count=1):
        opts = self._get_opts(element, x, y)
        opts['count'] = count
        self._add_action('tap', opts)

        return self

    def press(self, el=None, x=None, y=None):
        self._add_action('press', self._get_opts(el, x, y))
        return self

    def long_press(self, el=None, x=None, y=None, duration=1000):
        self._add_action('long_press', self._get_opts(el, x, y, duration ))

        return self

    def wait(self, ms=0):
        if ms is None:
            ms = 0

        opts = {'ms': ms}
        self._add_action('wait', opts)

        return self

    def move_to(self, el=None, x=None, y=None):
        self._add_action('move_to', self._get_opts(el, x, y))
        return self

    def release(self):
        self._add_action('release', {})
        return self

    def perform(self):
        params = {'action': self._actions}
        self._driver.execute(Command.TOUCH_ACTION, params)
        self._actions = []

        return self

    @property
    def json_wire_gesture(self):
        gestures = []
        for action in self._actions:
            gestures.append(copy.deepcopy(action))
        return gestures

    def _add_action(self, action, options):
        gesture = {
            'action': action,
            'options': options,
        }
        self._actions.append(gesture)

    def _get_opts(self, element, x, y, duration = None):
        opts = {}
        if element is not None:
            opts['element'] = element.id

        if x is None or y is None:
            x, y = None, None
        opts['x'] = x
        opts['y'] = y

        if duration is not None:
            opts['duration'] = duration

        return opts