import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "VideoGen | Local Mock Studio",
  description: "Original VideoGen creative studio — M0 CPU mock demonstration",
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return <html lang="en"><body>{children}</body></html>;
}
