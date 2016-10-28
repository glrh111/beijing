"use strict";

export class LazyPromise<T> extends Promise<T> {
    public static [Symbol.species] = Promise;

    private _resolve: (value: T | PromiseLike<T>) => void;
    private _reject: (reason: any) => void;
    private _executor: (resolve: (value: T | PromiseLike<T>) => void, reject: (reason: any) => void) => void;

    public constructor(executor: (resolve: (value: T | PromiseLike<T>) => void, reject: (reason: any) => void) => void) {
        let resolver: (value: T | PromiseLike<T>) => void;
        let rejecter: (reason: any) => void;
        super((resolve, reject) => { resolver = resolve; rejecter = reject; });
        this._resolve = resolver;
        this._reject = rejecter;
        this._executor = executor;
    }

    public then<TResult>(onfulfilled?: (value: T) => TResult | PromiseLike<TResult>, onrejected?: (reason: any) => TResult | PromiseLike<TResult>): Promise<TResult> {
        this._lazyExecute();
        return super.then(onfulfilled, onrejected);
    }

    private _lazyExecute() {
        if (this._executor) {
            let executor = this._executor, resolve = this._resolve, reject = this._reject;
            delete this._executor;
            delete this._resolve;
            delete this._reject;
            try {
                executor(resolve, reject);
            }
            catch (e) {
                reject(e);
            }
        }
    }
}

export function sleep(msec: number) {
    return new Promise<void>(resolve => setTimeout(resolve, msec));
}

export function formatMessage(text: string, firstLineWidth: number, remainingLinesWidth?: number) {
    if (remainingLinesWidth === undefined) remainingLinesWidth = firstLineWidth;
    let pattern = /(\r\n?|\n)|(\s)|(\S+)/g;
    let match: RegExpMatchArray;
    let lines: string[] = [];
    let line: string = "";
    let leadingWhiteSpace: string = "";
    let width = firstLineWidth;
    while (match = pattern.exec(text)) {
        if (match[1]) {
            lines.push(line);
            width = remainingLinesWidth;
            line = "";
            leadingWhiteSpace = "";
        }
        else if (match[2]) {
            leadingWhiteSpace += match[2];
        }
        else if (match[3]) {
            let token = match[3];
            let lineLengthWithWhitespace = line.length + leadingWhiteSpace.length;
            let lineLengthWithText = lineLengthWithWhitespace + token.length;
            if (token.length > width) {
                // If there is room, append the first chunk of the long line to the
                // current line.
                let offset = 0;
                if (lineLengthWithWhitespace < width) {
                    let chunk = token.substr(offset, width - lineLengthWithWhitespace);
                    line += leadingWhiteSpace + chunk;
                    offset += chunk.length;
                }

                // Push the current line.
                if (line) {
                    lines.push(line);
                    width = remainingLinesWidth;
                    line = "";
                }

                leadingWhiteSpace = "";

                // Append lines for each chunk longer than one line.
                while (token.length - offset > width) {
                    lines.push(token.substr(offset, width));
                    width = remainingLinesWidth;
                    offset += width;
                }

                // Append the remaining text to the current line.
                if (token.length - offset > 0) {
                    line = token.substr(offset);
                }
                else {
                    line = "";
                }
            }
            else if (lineLengthWithText > width) {
                lines.push(line);
                width = remainingLinesWidth;
                line = token;
                leadingWhiteSpace = "";
            }
            else {
                line += leadingWhiteSpace + token;
                leadingWhiteSpace = "";
            }
        }
    }

    if (line) {
        lines.push(line);
    }

    return lines;
}