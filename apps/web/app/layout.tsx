import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "VideoGen | Studio & English Practice",
  description: "Local creative workflow and English/Bangla phrase practice",
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return <html lang="en"><body>{children}</body></html>;
}
