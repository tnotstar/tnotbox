
#include <gtk/gtk.h>

void
on_hello (void) {
    g_print("Hello, world!\n");
}

void
on_destroy (void) {
    g_print("Destroying...\n");
    gtk_main_quit();
}

int
main (int argc, char *argv[]) {

    GtkWidget *window;

    gtk_init(&argc, &argv);

    window = gtk_window_new(GTK_WINDOW_TOPLEVEL);
    g_signal_connect(window, "destroy", G_CALLBACK(on_destroy), NULL);
    gtk_widget_show(window);

    gtk_main();

    return 0;
}

