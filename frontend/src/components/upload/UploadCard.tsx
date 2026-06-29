import { useState } from "react";
import { Upload } from "lucide-react";
import { uploadDocument } from "../../api/document";

export default function UploadCard() {
  const [loading, setLoading] = useState(false);

  async function handleChange(
    e: React.ChangeEvent<HTMLInputElement>
  ) {
    if (!e.target.files?.length) return;

    try {
      setLoading(true);

      const result = await uploadDocument(e.target.files[0]);

      console.log("Upload Success:", result);

      alert("✅ Upload Successful");
    } catch (err: any) {
      console.error("Upload Error:", err);

      if (err.response) {
        console.log("Status:", err.response.status);
        console.log("Response:", err.response.data);
      } else if (err.request) {
        console.log("No response received:", err.request);
      } else {
        console.log("Message:", err.message);
      }

      alert("❌ Upload Failed");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="border border-slate-700 rounded-xl p-8">
      <label className="cursor-pointer flex flex-col items-center gap-4">
        <Upload size={42} />

        <span>
          {loading ? "Uploading..." : "Click to Upload PDF"}
        </span>

        <input
          type="file"
          accept=".pdf"
          hidden
          onChange={handleChange}
        />
      </label>
    </div>
  );
}