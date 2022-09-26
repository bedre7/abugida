import React, { useState, FC, SetStateAction, Dispatch } from "react";

export interface IContext {
  code: string;
  lines: number[];
  output: string[];
  error: string[];
  isRunning: boolean;
  terminalIsVisible: boolean;
  setCode: Dispatch<SetStateAction<string>>;
  setLines: Dispatch<SetStateAction<number[]>>;
  setTerminalIsVisible: Dispatch<SetStateAction<boolean>>;
  runCodeHandler: (code:string) => void;
}

export const CodeContext = React.createContext<IContext | null>(null);
