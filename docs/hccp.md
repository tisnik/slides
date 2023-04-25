# HCC Proxy: a Proof of Concept

---

## Architecture of HCC Proxy

![full image](images/hccp_basic.png)

---

## Fine-grained configuration

![full image](images/hccp_tree.png)

---

## HCC Proxy as on/off switch

![full image](images/hccp_enabled_state.png)

---

## HCC Proxy as on/off switch

![full image](images/hccp_disabled_state.png)

---

## Controlling HCC Proxy through console

![full image](images/hccp_on_off.png)

---

## HCCP Console (PoC)

![full image](images/hccp_console.png)

---

## Live demo

Settings:

* Redirection flow to HCC Proxy
* HCC Proxy started
* HCC Console started
* Accessing www.redhat.com periodically
* HCC Console used as on/off switch

---

## Network config

```
ptisnovs@ptisnovs:~$ cat /etc/hosts
127.0.0.1       localhost
127.0.1.1       ptisnovs
127.0.0.1       www.redhat.com
127.0.0.1       console.redhat.com

# The following lines are desirable for IPv6 capable hosts
::1     ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
```

---

## Proxy startup

```
./hccp_proxy
```

---

## Accessing www.redhat.com periodically

```
ptisnovs@ptisnovs:~$ watch curl console.redhat.com
```

---

## On/off switch on HCCP Console

(live demo)
