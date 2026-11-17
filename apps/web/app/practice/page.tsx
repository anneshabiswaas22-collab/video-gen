import type { Metadata } from "next";
import PracticeRoom from "../../../../features/english-speaking-friend/web/PracticeRoom";

export const metadata: Metadata = {
  title: "English practice | VideoGen",
  description: "A gentle place to practise English and Bangla example phrases, with clear learning and privacy limits.",
};

export default function PracticePage() {
  return <PracticeRoom />;
}
