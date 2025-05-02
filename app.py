from main import app
import layout
import callbacks


# App Layout -----------------------------------------------------------------------------------------------------------
app.layout = layout.create_layout()
callbacks.register_callbacks(app)

# Run ------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)