import matplotlib
matplotlib.use('Agg')  # Use the 'Agg' backend which doesn't require a GUI
import matplotlib.pyplot as plt
import io
import base64

def generate_diagram(query):
    # Create a new figure
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Generate a simple plot (you can customize this based on the query)
    x = [1, 2, 3, 4]
    y = [1, 4, 2, 3]
    ax.plot(x, y)
    
    ax.set_title(f"Diagram for: {query}")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    
    # Save the plot to a bytes buffer
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    
    # Encode the image to base64
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')
    
    # Clear the current figure
    plt.close(fig)
    
    return graphic