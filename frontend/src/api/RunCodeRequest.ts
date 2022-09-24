const TIMEOUT_SECONDS = 30;

const timeout = () => {
  return new Promise((_, reject) => {
    setTimeout(() => {
      reject(
        new Error(
          `Request took too long! Timeout after ${TIMEOUT_SECONDS} seconds`
        )
      );
    }, TIMEOUT_SECONDS * 1000);
  });
};

export const RunCodeRequest = async (code: string) => {
  try {
    const API_END_POINT = process.env.REACT_APP_API_URL;
    
    const fetchPromise = fetch(API_END_POINT ?? "./", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ code: code }),
    });

    const response: any = await Promise.race(
      [fetchPromise, timeout()]
    );

    const data = await response.json();
    
    return {
      output: data.output,
      error: data.error
    };

  } catch (error) {
    throw error;
  }
};
