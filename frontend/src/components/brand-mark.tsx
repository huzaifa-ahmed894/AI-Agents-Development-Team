export function BrandMark({ size = 28, className = "" }: { size?: number; className?: string }) {
  return <svg className={`brand-mark ${className}`} width={size} height={size} viewBox="0 0 40 40" fill="none" aria-hidden="true">
    <path d="M12 4.5h11.8L35.5 16v11.8L23.8 39.5H12L.5 27.8V16L12 4.5Z" transform="translate(2 0) scale(.9)" fill="currentColor" />
    <path d="M13 27V13h5.1l8.9 9V13" stroke="white" strokeWidth="2.7" strokeLinecap="round" strokeLinejoin="round" />
    <circle cx="27" cy="27" r="2.2" fill="white" />
  </svg>;
}
