import { useMemo, useState } from 'react';

interface ParsedRow {
  source_row: number;
  detected_type: string;
  ticker?: string | null;
  trade_date?: string | null;
  quantity?: number | null;
  price?: number | null;
  amount?: number | null;
  notes?: string | null;
}

const sampleRows: ParsedRow[] = [
  {
    source_row: 1,
    detected_type: 'DIVIDEND',
    ticker: 'AAPL',
    trade_date: '2024-03-01',
    amount: 24.56,
    notes: 'Sample data from parser',
  },
  {
    source_row: 2,
    detected_type: 'BUY',
    ticker: 'MSFT',
    trade_date: '2024-02-15',
    quantity: 10,
    price: 320.12,
    amount: -3201.2,
    notes: 'Sample data from parser',
  },
];

const ImportReview = () => {
  const [rows] = useState<ParsedRow[]>(sampleRows);
  const [selectedIds, setSelectedIds] = useState<number[]>(sampleRows.map((row) => row.source_row));

  const toggleRow = (rowId: number) => {
    setSelectedIds((prev) =>
      prev.includes(rowId) ? prev.filter((id) => id !== rowId) : [...prev, rowId]
    );
  };

  const summary = useMemo(() => {
    const total = rows.length;
    const included = rows.filter((row) => selectedIds.includes(row.source_row)).length;
    return { total, included };
  }, [rows, selectedIds]);

  return (
    <div className="min-h-screen bg-slate-50 py-10">
      <div className="mx-auto max-w-6xl space-y-8 px-4">
        <header className="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
          <div>
            <p className="text-sm font-semibold uppercase tracking-wide text-brand">Import Preview</p>
            <h1 className="text-3xl font-bold text-slate-900">Review parsed transactions</h1>
            <p className="mt-2 max-w-2xl text-sm text-slate-600">
              Confirm the transactions below before they are added to your portfolio. You can deselect any
              rows that should be ignored or adjust the detected fields.
            </p>
          </div>
          <div className="rounded-lg border border-slate-200 bg-white p-4 shadow-sm">
            <p className="text-sm font-medium text-slate-500">Summary</p>
            <p className="text-2xl font-semibold text-slate-900">{summary.included} / {summary.total}</p>
            <p className="text-xs text-slate-500">transactions will be imported</p>
          </div>
        </header>

        <section className="rounded-lg border border-slate-200 bg-white shadow-sm">
          <div className="overflow-x-auto">
            <table className="min-w-full divide-y divide-slate-200 text-sm">
              <thead className="bg-slate-100">
                <tr>
                  <th className="px-4 py-3 text-left text-xs font-medium uppercase tracking-wide text-slate-600">
                    Include
                  </th>
                  <th className="px-4 py-3 text-left text-xs font-medium uppercase tracking-wide text-slate-600">
                    Type
                  </th>
                  <th className="px-4 py-3 text-left text-xs font-medium uppercase tracking-wide text-slate-600">
                    Ticker
                  </th>
                  <th className="px-4 py-3 text-left text-xs font-medium uppercase tracking-wide text-slate-600">
                    Date
                  </th>
                  <th className="px-4 py-3 text-left text-xs font-medium uppercase tracking-wide text-slate-600">
                    Quantity
                  </th>
                  <th className="px-4 py-3 text-left text-xs font-medium uppercase tracking-wide text-slate-600">
                    Price
                  </th>
                  <th className="px-4 py-3 text-left text-xs font-medium uppercase tracking-wide text-slate-600">
                    Amount
                  </th>
                  <th className="px-4 py-3 text-left text-xs font-medium uppercase tracking-wide text-slate-600">
                    Notes
                  </th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-200 bg-white">
                {rows.map((row) => {
                  const included = selectedIds.includes(row.source_row);

                  return (
                    <tr key={row.source_row} className={!included ? 'bg-slate-100/50' : undefined}>
                      <td className="px-4 py-3">
                        <input
                          type="checkbox"
                          className="h-4 w-4 rounded border-slate-300 text-brand focus:ring-brand"
                          checked={included}
                          onChange={() => toggleRow(row.source_row)}
                        />
                      </td>
                      <td className="px-4 py-3 font-medium text-slate-900">{row.detected_type}</td>
                      <td className="px-4 py-3 text-slate-700">{row.ticker ?? '—'}</td>
                      <td className="px-4 py-3 text-slate-700">{row.trade_date ?? '—'}</td>
                      <td className="px-4 py-3 text-slate-700">{row.quantity ?? '—'}</td>
                      <td className="px-4 py-3 text-slate-700">{row.price ?? '—'}</td>
                      <td className="px-4 py-3 text-slate-700">{row.amount ?? '—'}</td>
                      <td className="px-4 py-3 text-slate-500">{row.notes ?? '—'}</td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>
        </section>

        <footer className="flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
          <div className="text-sm text-slate-500">
            Need to adjust columns? <span className="font-medium text-brand">Upload mapping template</span>
          </div>
          <div className="flex items-center gap-3">
            <button className="rounded-md border border-slate-300 px-4 py-2 text-sm font-medium text-slate-700 hover:bg-slate-100">
              Cancel
            </button>
            <button className="rounded-md bg-brand px-4 py-2 text-sm font-semibold text-white shadow-sm hover:bg-brand-dark">
              Confirm & Import
            </button>
          </div>
        </footer>
      </div>
    </div>
  );
};

export default ImportReview;
