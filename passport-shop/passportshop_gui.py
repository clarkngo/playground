import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import ImageTk

from image_loader import ImageLoader
from face_detector import FaceDetector
from image_cropper import ImageCropper
from background_cleaner import BackgroundCleaner
from image_resizer import ImageResizer

class PassportShopGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("PassportShop")
        self.master.geometry("800x600")

        # --- GUI Elements ---
        self.upload_btn = tk.Button(master, text="Upload Photo", command=self.upload_photo)
        self.upload_btn.pack(pady=10)

        self.process_btn = tk.Button(master, text="Process Photo", command=self.process_photo, state=tk.DISABLED)
        self.process_btn.pack(pady=10)

        self.save_btn = tk.Button(master, text="Save Passport Photo", command=self.save_photo, state=tk.DISABLED)
        self.save_btn.pack(pady=10)

        self.image_label = tk.Label(master)
        self.image_label.pack(pady=10)

        self.pil_image = None  # Original uploaded image
        self.processed_image = None  # Final passport photo

    # --- Upload Image ---
    def upload_photo(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.jpg *.jpeg *.png")])
        if file_path:
            self.pil_image = ImageLoader.load_image(file_path)
            self.show_image(self.pil_image)
            self.process_btn.config(state=tk.NORMAL)

    # --- Process Image ---
    def process_photo(self):
        try:
            image_np = ImageLoader.to_numpy(self.pil_image)
            face_box = FaceDetector.detect_face(image_np)
            cropped_image = ImageCropper.crop_face(image_np, face_box, margin_ratio=0.3)
            cleaned_image = BackgroundCleaner.clean_background(cropped_image)
            self.processed_image = ImageResizer.resize_for_passport(cleaned_image)
            self.show_image(self.processed_image)
            self.save_btn.config(state=tk.NORMAL)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # --- Save Processed Image ---
    def save_photo(self):
        if self.processed_image:
            save_path = filedialog.asksaveasfilename(
                defaultextension=".jpg",
                filetypes=[("JPEG Image", "*.jpg")])
            if save_path:
                self.processed_image.save(save_path, dpi=(300, 300))
                messagebox.showinfo("Saved", f"Passport photo saved to:\n{save_path}")

    # --- Display Image in Tkinter ---
    def show_image(self, pil_image):
        max_size = (400, 400)
        display_image = pil_image.copy()
        display_image.thumbnail(max_size)
        tk_image = ImageTk.PhotoImage(display_image)
        self.image_label.configure(image=tk_image)
        self.image_label.image = tk_image  # Keep reference

# --- Run GUI ---
if __name__ == "__main__":
    root = tk.Tk()
    app = PassportShopGUI(root)
    root.mainloop()
