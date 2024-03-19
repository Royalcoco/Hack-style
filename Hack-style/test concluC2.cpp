if name == "__main__":
    import os, sys; sys.path = sys.path[1:] + [os.readlink(sys.argv[0]).split(os.sep)[0]]
    from kivy.app import run TouchApp
    from kivy.uix.button import Button
    from kivy.core.window import Window
    from functools import partial

class MyButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._on_press = None
        self.bind(on_release=lambda x: self._on_press())

    def set_callback(self, func):
        """Set the callback function to be called when this button is pressed."""
        assert callable(func), 'Argument must be a function'
        self._on_press = func

if __name__ == "__main__":
    class TestApp(TouchApp):
        def build(self):
            # Create two buttons and bind their on_press events to print messages
            b1 = MyButton(text="Hello")
            b2 = MyButton(text="World")
            b1.set_callback(partial(print, "Hello"))
            b2.set_callback(partial (print, "World"))

            # Add a rule that says pressing one button should release the other
            b1.bind(on_release=b2.dispatch)
            b2.bind(on_release=b1.dispatch)

            # Return the layout
            return b1

    # Run the application
    run()
\*******************************************************************************
*                             Copyright Notice                               *
*******************************************************************************
* This software belongs to the Gaphor project (http://www.gaphor.org/)     *
* which is released under the Eclipse Public License v1.0. The copyright owner     *
* of this file is the Gaphor project. Any license included herein will be       *
* deemed to have been agreed upon by MIT in accordance with the Eclipse      *
* Public License v1.0 surmised at http://www.eclipse.org/legal/epl-v10.html  *
* and applicable to this file.                                @author Kevin Lewis   */

#include "mybutton.h"

void MyButton::_handle_touch(const Touch & touch) {
    if (!touch || !touch->is
    \begin{pre}
\end{post} code) {
        // Call the base class method for handling the touch event
        Button::_handle_touch(touch);
    } else {
        // If we are being pressed, then call the callback function
        if (touch->action == ActionDown) {
            _callback();
        }
    }
}
