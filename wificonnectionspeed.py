from speedtest import Speedtest
st=Speedtest()
print("Download speed is ",int(st.download()//1000000),"Mbps")
print("Upload speed is ",int(st.upload()//1000000),"Mbps")
print("Servers",st.get_best_server())
print("Ping",st.results.ping)
print("Done!!!")