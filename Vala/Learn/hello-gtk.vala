//
// hello-gtk.vala - a `hello world` Gtk+ program in vala
//
// compile with:
//   $ valac --pkg gtk+-3.0 hello-gtk.vala
//

using Gtk;

int
main(string[] args) {

    Gtk.init(ref args);

    var win = new Window();
    win.title = "Hello, Gtk+!";
    win.border_width = 10;
    win.window_position = WindowPosition.CENTER;
    win.set_default_size(350, 70);
    win.destroy.connect(Gtk.main_quit);

    var label = new Label("Hello, world!");
    win.add(label);
    win.show_all();

    Gtk.main();

    return 0;
}

// EOF
