import SEO from "@/components/SEO";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/components/ui/card";
import { Link } from "react-router-dom";

const EMDRefund = () => {
  const handlePrintFirstPage = () => {
    const iframe = document.getElementById("emd-iframe") as HTMLIFrameElement | null;
    if (!iframe) return;
    const win = iframe.contentWindow;
    const doc = iframe.contentDocument || win?.document || null;
    if (!win || !doc) return;

    const style = doc.createElement("style");
    style.setAttribute("media", "print");
    style.textContent = `
      @page { size: A4 portrait; margin: 12mm; }
      html, body { height: auto !important; }
      body { overflow: hidden !important; }
      /* Cap printable area to one page */
      #root, main, .container, .wrapper, .sheet, .page, .pages { max-height: 297mm; overflow: hidden !important; }
    `;
    doc.head.appendChild(style);

    win.focus?.();
    win.print?.();
    win.addEventListener?.("afterprint", () => style.remove(), { once: true });
  };

  return (
    <div className="container mx-auto py-10">
      <SEO title="EMD Refund — Integrated PWD Tools" description="Track and process EMD refunds using the embedded tool." />
      <header className="mb-6">
        <h1 className="text-3xl font-bold">EMD Refund</h1>
        <p className="text-muted-foreground">Live tool embedded below.</p>
      </header>
      <Card className="elevated">
        <CardHeader>
          <CardTitle>Interactive Tool</CardTitle>
          <CardDescription>Powered by pwd-tools.pages.dev</CardDescription>
        </CardHeader>
        <CardContent className="space-y-4">
          <div className="w-full overflow-hidden rounded-md border">
            <iframe
              id="emd-iframe"
              src="/tools/EmdRefund.html"
              title="EMD Refund tool (PWD Tools)"
              className="w-full h-[70vh]"
              loading="lazy"
            />
          </div>
          <div className="flex gap-3">
            <Button onClick={handlePrintFirstPage}>Print Page 1</Button>
            <Button asChild variant="secondary"><a href="/tools/EmdRefund.html" target="_blank" rel="noopener noreferrer">Open full page</a></Button>
            <Button asChild><Link to="/">Back to Dashboard</Link></Button>
          </div>
        </CardContent>
      </Card>
    </div>
  );
};

export default EMDRefund;
