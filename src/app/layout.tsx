import './globals.css'
import { Inter } from 'next/font/google'
import { Amplify } from 'aws-amplify';
import config from '../aws-exports';

// Configure Amplify only on the client side to avoid SSR issues
if (typeof window !== "undefined" && config) {
  Amplify.configure(config);
}

const inter = Inter({ subsets: ['latin'] })

export const metadata = {
  title: 'Amplify Next.js App',
  description: 'Generated Amplify Next.js template',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className={inter.className}>{children}</body>
    </html>
  )
}