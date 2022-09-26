import React, { SetStateAction, Dispatch } from "react";

export interface ICode {
  code: string;
  lines: number[];
  output: string[];
  error: string[];
  isRunning: boolean;
  terminalIsVisible: boolean;
  setCode: Dispatch<SetStateAction<string>>;
  setLines: Dispatch<SetStateAction<number[]>>;
  setTerminalIsVisible: Dispatch<SetStateAction<boolean>>;
  runCodeHandler: (code: string) => void;
}

export const CodeContext = React.createContext<ICode | null>(null);
