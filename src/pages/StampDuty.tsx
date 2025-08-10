import { useState } from "react";
import SEO from "@/components/SEO";
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Link } from "react-router-dom";

const STAMP_DUTY_RATE = 0.15; // 0.15%
const MIN_STAMP_DUTY = 1000;   // ₹1,000
const MAX_STAMP_DUTY = 2500000; // ₹25,00,000

const calculateStampDuty = (amount: number): number => {
  if (isNaN(amount) || amount <= 0) return 0;
  const duty = Math.ceil((amount * STAMP_DUTY_RATE) / 100);
  return Math.min(Math.max(duty, MIN_STAMP_DUTY), MAX_STAMP_DUTY);
};

const StampDuty = () => {
  const [amount, setAmount] = useState<string>("");
  const [result, setResult] = useState<number | null>(null);

  const handleCalculate = () => {
    const amountNum = parseFloat(amount);
    if (isNaN(amountNum) || amountNum <= 0) {
      setResult(null);
      return;
    }
    
    const duty = calculateStampDuty(amountNum);
    setResult(duty);
  };

  return (
    <div className="container mx-auto py-10">
      <SEO 
        title="Stamp Duty Calculator — PWD Tools" 
        description="Calculate stamp duty for work orders and agreements." 
      />
      <header className="mb-6">
        <div className="flex justify-between items-center">
          <div>
            <h1 className="text-3xl font-bold">Stamp Duty Calculator</h1>
            <p className="text-muted-foreground">Calculate stamp duty for work orders and agreements</p>
          </div>
          <Link 
            to="/" 
            className="inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 bg-primary text-primary-foreground hover:bg-primary/90 h-10 px-4 py-2"
          >
            ← Back to Dashboard
          </Link>
        </div>
      </header>
      <Card className="elevated max-w-2xl mx-auto">
        <CardHeader>
          <CardTitle>Stamp Duty Calculation</CardTitle>
          <CardDescription>
            Rate: {STAMP_DUTY_RATE}% (Min: ₹{MIN_STAMP_DUTY.toLocaleString('en-IN')}, Max: ₹{MAX_STAMP_DUTY.toLocaleString('en-IN')})
          </CardDescription>
        </CardHeader>
        <CardContent className="space-y-6">
          <div className="grid gap-2">
            <Label htmlFor="amount">Work Order/Agreement Amount (₹)</Label>
            <div className="flex gap-2">
              <Input
                id="amount"
                type="number"
                min="0"
                step="1"
                placeholder="Enter amount in INR"
                value={amount}
                onChange={(e) => setAmount(e.target.value)}
                onKeyDown={(e) => e.key === 'Enter' && handleCalculate()}
                className="text-base"
              />
            </div>
          </div>

          {result !== null && (
            <div className="p-4 border rounded-lg bg-muted/20">
              <div className="flex justify-between items-center">
                <span className="font-medium">Stamp Duty:</span>
                <span className="text-2xl font-bold">₹ {result.toLocaleString('en-IN')}</span>
              </div>
              <div className="mt-2 text-sm text-muted-foreground">
                Calculated at {STAMP_DUTY_RATE}% of ₹{parseFloat(amount).toLocaleString('en-IN')}
              </div>
            </div>
          )}
        </CardContent>
      </Card>
      
      <div className="mt-8 flex justify-center">
        <Link 
          to="/" 
          className="inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 border border-input bg-background hover:bg-accent hover:text-accent-foreground h-10 px-4 py-2"
        >
          ← Back to Dashboard
        </Link>
      </div>
    </div>
  );
};

export default StampDuty;
